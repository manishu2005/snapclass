import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            .stApp{
                background: #5865F2 !important;
            }
            
            .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
            }
            .stApp div[data-testid="stColumn"] *{
    color:black !important;
}


        </style>

        """, unsafe_allow_html=True)
    
def style_background_dashboard():
    st.markdown("""
        <style>
                .stApp{
                background: #E0E3FF !important;
                }
        </style>

        """, unsafe_allow_html=True)
    

def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Outfit:wght@100..900&display=swap');

                /*Hide top bar of streamlit*/

                MainMenu {
                    visibility: hidden;
                }

                header[data-testid="stHeader"] {
                    visibility: hidden;
                    height: 0;
                }

                div[data-testid="stToolbar"] {
                    visibility: hidden;
                    height: 0;
                }

                footer {
                    visibility: hidden;
                }

               .block-container {
            padding-top: 1.5rem !important;
        }

        .stApp {
            background: #E0E3FF !important;
        }
                
                    h1, h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            color: #111827 !important;
            line-height: 1 !important;
        }

        h3, h4, p, span {
            font-family: 'Outfit', sans-serif;
        }
                button{
                    border-radius: 1.5rem !important;
                    background-color: #5865F2 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button[kind="secondary"]{
                    border-radius: 1.5rem !important;
                    background-color: #EB459E !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button[kind="tertiary"]{
    border-radius: 1.5rem !important;
    background-color: #E0E3FF !important;
    color: #111827 !important;
    padding: 10px 20px !important;
    border: 1px solid #111827 !important;
    transition: transform 0.25s ease-in-out !important;
}
              

                .stTextInput input::placeholder {
                    color: #555 !important;
                }

                /* headings */
               .teacher-auth-title{
    color:#111827 !important;
    text-align:center !important;
    font-size:2.4rem !important;
    font-weight:800 !important;
    margin-top:1rem !important;
    margin-bottom:1.25rem !important;
    font-family:'Outfit', sans-serif !important;
    letter-spacing:-0.02em !important;
}

/* input labels */
div[data-testid="stTextInput"] label p{
    color:#111827 !important;
    font-weight:700 !important;
    font-size:1rem !important;
    margin-bottom:0.35rem !important;
}
                /* input field */
                div[data-testid="stTextInput"] input{
    color:#111827 !important;
    background:#ffffff !important;
    border-radius:1rem !important;
    border:2px solid #c7cdfd !important;
    caret-color:#5865F2 !important;
    box-shadow:none !important;
    padding:0.85rem 1rem !important;
    transition: all 0.2s ease !important;

    div[data-testid="stTextInput"] input:focus{
    border-color:#5865F2 !important;
    box-shadow:0 0 0 4px rgba(88, 101, 242, 0.18) !important;
    outline:none !important;
}
}
                /* placeholder */
                div[data-testid="stTextInput"] input::placeholder{
    color:#6b7280 !important;
    opacity:1 !important;
}

                div[data-testid="stTextInput"] input::selection{
    background:rgba(88,101,242,0.22) !important;
}


                /* password eye button fix */
               button[title="Show password text"]{
    background:#5865F2 !important;
    color:white !important;
    border-radius:0.9rem !important;
}


                /* success + error messages */
                div[data-testid="stAlert"]{
                    color:#111827 !important;
                    font-weight:600 !important;
                }

                /* success/error text specifically */
                div[data-testid="stAlert"] p{
                    color:#111827 !important;
                }

                /* divider */
                hr{
                    border-color:rgba(0,0,0,0.15) !important;
                }

              [data-testid="stToast"] {
    background: white !important;
    color: #111827 !important;
    border: 2px solid #d6dbff !important;
    border-radius: 1rem !important;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08) !important;
}

/* toast text */
[data-testid="stToast"] p {
    color: #111827 !important;
    font-weight: 600 !important; 
} 
                
                /* Spinner text */
div[data-testid="stSpinner"] p{
    color:#111827 !important;
    font-weight:600 !important;
    font-size:1rem !important;
}

/* optional spinner container */
div[data-testid="stSpinner"]{
    color:#111827 !important;
}
        </style>

        """, unsafe_allow_html=True)
    
    