import io
import sys
import numpy as np
import torch
import torchaudio
import librosa
import streamlit as st

TARGET_SR = 16000

def patch_speechbrain_lazy_imports():
    from speechbrain.utils.importutils import LazyModule

    if not getattr(LazyModule, "_snapclass_file_patch", False):
        original_getattr = LazyModule.__getattr__

        def safe_getattr(self, attr):
            if attr == "__file__":
                raise AttributeError()
            return original_getattr(self, attr)

        LazyModule.__getattr__ = safe_getattr
        LazyModule._snapclass_file_patch = True

    deprecated_modules = {
        "speechbrain.k2_integration",
        "speechbrain.wordemb",
        "speechbrain.lobes.models.huggingface_transformers",
        "speechbrain.lobes.models.spacy",
        "speechbrain.lobes.models.flair",
        "speechbrain.nnet.loss.transducer_loss",
    }

    for module_name in deprecated_modules:
        sys.modules.pop(module_name, None)

    modules_to_clean = {
        "speechbrain": ("k2_integration", "wordemb"),
        "speechbrain.lobes.models": ("huggingface_transformers", "spacy", "flair"),
        "speechbrain.nnet.loss": ("transducer_loss",),
    }

    for module_name, attrs in modules_to_clean.items():
        module = sys.modules.get(module_name)
        if module is not None:
            for attr in attrs:
                vars(module).pop(attr, None)

@st.cache_resource
def load_voice_encoder():
    __import__("speechbrain")
    patch_speechbrain_lazy_imports()

    from speechbrain.inference.classifiers import EncoderClassifier

    patch_speechbrain_lazy_imports()

    return EncoderClassifier.from_hparams(
        source="speechbrain/spkrec-ecapa-voxceleb",
        savedir="pretrained_models/spkrec-ecapa-voxceleb"
    )

def load_audio_tensor(audio_bytes, target_sr=TARGET_SR):
    audio_stream = io.BytesIO(audio_bytes)

    try:
        audio, sr = torchaudio.load(audio_stream)
        if audio.shape[0] > 1:
            audio = audio.mean(dim=0, keepdim=True)
        if sr != target_sr:
            audio = torchaudio.functional.resample(audio, sr, target_sr)
        return audio.float()
    except Exception:
        audio_stream.seek(0)
        audio, sr = librosa.load(audio_stream, sr=target_sr, mono=True)
        return torch.from_numpy(audio).float().unsqueeze(0)

def normalize_embedding(emb):
    emb = np.asarray(emb, dtype=np.float32).flatten()
    norm = np.linalg.norm(emb)
    if norm == 0:
        return emb
    return emb / norm
def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()
        wav = load_audio_tensor(audio_bytes)

        with torch.no_grad():
            embedding = encoder.encode_batch(wav)

        embedding = embedding.squeeze().cpu().numpy()
        embedding = embedding / (np.linalg.norm(embedding) + 1e-12)
        return embedding.tolist()

    except Exception as e:
        st.error(f"Voice recog error: {e}")
        return None
    
    
def identify_speaker(new_embedding, candidates_dict, threshold=0.65):
    if new_embedding is None or not candidates_dict:
        return None, 0.0

    new_embedding = normalize_embedding(new_embedding)

    best_sid = None
    best_score = -1.0

    for sid, stored_embedding in candidates_dict.items():
        if stored_embedding is not None and len(stored_embedding) > 0:
            stored_embedding = normalize_embedding(stored_embedding)

            # same logic as your original code: similarity via dot product
            similarity = float(np.dot(new_embedding, stored_embedding))

            if similarity > best_score:
                best_score = similarity
                best_sid = sid

    if best_score >= threshold:
        return best_sid, best_score

    return None, best_score

def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.65):
    try:
        encoder = load_voice_encoder()

        # load full audio
        wav = load_audio_tensor(audio_bytes)
        audio = wav.squeeze(0).cpu().numpy()

        segments = librosa.effects.split(audio, top_db=30)
        identify_result = {}

        for start, end in segments:
            if (end - start) < TARGET_SR * 0.5:
                continue

            segment_audio = audio[start:end]
            segment_wav = torch.from_numpy(segment_audio).float().unsqueeze(0)

            with torch.no_grad():
                embeddings = encoder.encode_batch(segment_wav)

            embeddings = embeddings.squeeze().cpu().numpy().tolist()

            sid, score = identify_speaker(embeddings, candidates_dict, threshold)

            if sid:
                if sid not in identify_result or score > identify_result[sid]:
                    identify_result[sid] = score

        return identify_result

    except Exception as e:
        st.error(f"Bulk process error: {e}")
        return {}
