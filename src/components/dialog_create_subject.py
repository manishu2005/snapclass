import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):

    st.markdown("""
    <style>
        /* dialog container */
        div[role="dialog"]{
            border-radius:24px !important;
            background:#F8FAFC !important;
            border:2px solid #E0E7FF !important;
        }

        /* dialog title */
        div[role="dialog"] h2{
            color:#111827 !important;
            font-family:'Outfit',sans-serif !important;
            font-size:2rem !important;
            font-weight:800 !important;
        }

        /* labels */
        div[role="dialog"] label p{
            color:#111827 !important;
            font-weight:600 !important;
            font-size:1rem !important;
        }

        /* input fields */
        div[role="dialog"] input{
            background:white !important;
            color:#111827 !important;
            border-radius:14px !important;
            border:2px solid #C7D2FE !important;
            padding:12px !important;
        }

        /* placeholder */
        div[role="dialog"] input::placeholder{
            color:#6B7280 !important;
        }

        /* button */
        div[role="dialog"] button[kind="primary"]{
            background:#EB459E !important;
            color:white !important;
            border:none !important;
            border-radius:18px !important;
            font-weight:700 !important;
            padding:12px 18px !important;
            transition:0.2s ease-in-out !important;
        }

        div[role="dialog"] button[kind="primary"]:hover{
            transform:scale(1.02);
            background:#d63384 !important;
        }

        /* helper text */
        div[role="dialog"] p{
            color:#374151 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    st.write("Enter the details of new subject")

    sub_id = st.text_input(
        "Subject Code",
        placeholder="CS101"
    )

    sub_name = st.text_input(
        "Subject Name",
        placeholder="Introduction to Computer Science"
    )

    sub_section = st.text_input(
        "Section",
        placeholder="A"
    )

    if st.button(
        "Create Subject Now",
        type="primary",
        width="stretch"
    ):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(
                    sub_id,
                    sub_name,
                    sub_section,
                    teacher_id
                )

                st.toast(
                    "Subject Created Successfully!",
                    icon="✅"
                )

                st.rerun()

            except Exception as e:
                st.error(f"Error: {str(e)}")

        else:
            st.warning("Please fill all the fields")