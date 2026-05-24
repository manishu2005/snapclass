import streamlit as st
import segno
import io

@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):

    st.markdown("""
    <style>

        /* dialog box */
        div[role="dialog"]{
            border-radius:24px !important;
            background:#F8FAFC !important;
            border:2px solid #E0E7FF !important;
            padding:10px !important;
        }

        /* title */
        div[role="dialog"] h1,
        div[role="dialog"] h2,
        div[role="dialog"] h3{
            color:#111827 !important;
            font-family:'Outfit',sans-serif !important;
            font-weight:800 !important;
        }

        /* all text */
        div[role="dialog"] p,
        div[role="dialog"] span,
        div[role="dialog"] label{
            color:#374151 !important;
        }

        /* code blocks */
        div[role="dialog"] pre{
            background:#EEF2FF !important;
            border-radius:14px !important;
            border:1px solid #C7D2FE !important;
            padding:12px !important;
        }

        div[role="dialog"] code{
            color:#4338CA !important;
            font-weight:600 !important;
        }

        /* info box */
        div[data-testid="stAlert"]{
            background:#FCE7F3 !important;
            border-radius:16px !important;
            border:none !important;
        }

        div[data-testid="stAlert"] p{
            color:#9D174D !important;
            font-weight:600 !important;
        }

        /* image styling */
        img{
            border-radius:20px !important;
            border:3px solid #E0E7FF !important;
            padding:10px !important;
            background:white !important;
        }

    </style>
    """, unsafe_allow_html=True)

    app_domain = "snapclass-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header(f"Join {subject_name}")

    qr = segno.make(join_url)

    out = io.BytesIO()
    qr.save(out, kind="png", scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Copy Link")

        st.code(join_url, language="text")

        st.markdown("### Subject Code")

        st.code(subject_code, language="text")

        st.info(
            "Copy this link and share it through WhatsApp, Email, or Classroom groups."
        )

    with col2:
        st.markdown("### Scan QR Code")

        st.image(
            out.getvalue(),
            caption="QR Code for class joining",
            use_container_width=True
        )