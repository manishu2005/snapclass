# SnapClass

SnapClass is a Streamlit attendance application that uses AI-assisted face and voice recognition to help teachers take attendance faster. Teachers can create subjects, share class join links or QR codes, run face analysis from uploaded class photos, and review attendance records. Students can sign in with Face ID, register their profile, enroll in subjects, and optionally add a voice profile for voice-based attendance.

## Features

- Student and teacher portals built with Streamlit
- Teacher registration and login with hashed passwords
- Subject creation, management, and sharing through join links and QR codes
- Student Face ID login and profile registration
- Face-recognition attendance from uploaded classroom photos
- Optional voice enrollment and voice-based attendance
- Supabase-backed storage for teachers, students, subjects, enrollments, and attendance logs
- Attendance summaries for students and teacher-side attendance records

## Tech Stack

- Python
- Streamlit
- Supabase
- dlib and face recognition models
- scikit-learn
- SpeechBrain, TorchAudio, and Librosa
- Segno for QR code generation
- Pandas and NumPy

## Project Structure

```text
.
|-- app.py
|-- base_layout.py
|-- requirements.txt
|-- pretrained_models/
|-- src/
|   |-- components/
|   |   |-- dialog_add_photo.py
|   |   |-- dialog_attendance_result.py
|   |   |-- dialog_auto_enroll.py
|   |   |-- dialog_create_subject.py
|   |   |-- dialog_enroll.py
|   |   |-- dialog_share_subject.py
|   |   |-- dialog_voice_attendance.py
|   |   |-- header.py
|   |   `-- subject_card.py
|   |-- database/
|   |   |-- config.py
|   |   `-- db.py
|   |-- pipelines/
|   |   |-- face_pipeline.py
|   |   `-- voice_pipeline.py
|   `-- screens/
|       |-- home_screen.py
|       |-- student_screen.py
|       `-- teacher_screen.py
`-- .streamlit/
    `-- secrets.toml
```

## Getting Started

### 1. Clone the project

```bash
git clone <your-repository-url>
cd SnapclassProject
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The project uses `dlib-bin` and face recognition models. If installation fails on your system, make sure your Python version is compatible with the available wheel for `dlib-bin`.

### 4. Configure Streamlit secrets

Create or update `.streamlit/secrets.toml`:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-supabase-anon-key"
SUPABASE_SERVICE_ROLE_KEY = "your-supabase-service-role-key"
```

`SUPABASE_SERVICE_ROLE_KEY` is used for privileged subject creation. Keep it private and do not commit real production secrets.

### 5. Run the app

```bash
streamlit run app.py
```

The app opens in your browser at the local Streamlit URL shown in the terminal.

## Supabase Tables

The app expects Supabase tables for:

- `teachers`
- `students`
- `subjects`
- `subject_students`
- `attendance_logs`

The database helper functions are defined in `src/database/db.py`. Make sure your table columns match the fields used by those functions, including teacher credentials, student embeddings, subject metadata, enrollments, timestamps, and attendance status.

## How It Works

1. A user chooses the Student or Teacher portal from the home screen.
2. Teachers can register, log in, create subjects, share class join codes, and take attendance.
3. Students can log in using Face ID or create a new profile with face and optional voice embeddings.
4. Teachers upload class photos for face-based attendance or use audio for voice-based attendance.
5. Attendance logs are saved in Supabase and shown in the app dashboards.

## Deployment

This project can be deployed to Streamlit Community Cloud or another Python hosting platform that supports Streamlit. Add the same Supabase values from `.streamlit/secrets.toml` to the deployment environment's secrets manager.

For Streamlit Community Cloud, set the entry point to:

```text
app.py
```

## Notes

- Voice models are downloaded and cached under `pretrained_models/`.
- Face and voice recognition quality depends on lighting, camera clarity, audio quality, and the number of enrolled samples.
- Do not commit `.env`, `.streamlit/secrets.toml`, or real Supabase credentials.
