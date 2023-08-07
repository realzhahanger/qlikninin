import streamlit as st

def main():

    page_bg_color = '#000080'
    text_color = 'white'
    st.markdown(f"""
    <style>
        .reportview-container {{
            background-color: {page_bg_color};
            color: {text_color};
        }}
    </style>
    """, unsafe_allow_html=True)

    #
    logo_path = "C:\\Users\\User\\Desktop\\stream\\logo.png"
    #st.image(logo_path)  
    st.markdown("# Информационные системы Агетства РК по финансовому мониторингу")

    # Adding buttons
    
    st.markdown("<a href='https://websfm.kz/' target='_blank'>WEBSFM</a>", unsafe_allow_html=True)
    st.markdown("<a href='https://www.gov.kz/memleket/entities/afm?lang=ru' target='_blank'>Сайт Агентства</a>", unsafe_allow_html=True)

def open_link(url):
    js = f"window.open('{url}')" 
    html = f"<script>{js}</script>"
    st.markdown(html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
