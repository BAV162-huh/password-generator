import streamlit as st
import random
import string

services = [
    "Email", "Facebook", "Instagram", "Twitter", "TikTok",
    "WhatsApp", "Telegram", "Snapchat", "YouTube", "Orange Money",
    "Vodafone Cash", "Etisalat", "We Pay", "Netflix", "Amazon",
    "Spotify", "Steam", "Discord", "Gmail", "General"
]

st.set_page_config(page_title="Smart Password Generator", page_icon="🔐")

# ✅ اسم صاحب الموقع
st.markdown("<h1 style='text-align: center; color: cyan;'>🔐 Smart Password Generator</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #00ffaa;'>by Bavly Hany Roushdy (B.H.R)</h3>", unsafe_allow_html=True)

st.write("## اختر الخدمة لتوليد كلمة مرور آمنة:")

selected_service = st.selectbox("الخدمة", services)

if st.button("توليد كلمة مرور"):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    password = ''.join(random.choice(chars) for _ in range(14))
    st.success(f"🔑 كلمة المرور لخدمة {selected_service}:\n\n`{password}`")
    st.code(password, language='bash')
