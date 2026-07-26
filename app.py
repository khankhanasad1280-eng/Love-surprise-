import streamlit as st

st.set_page_config(page_title="❤️ Secret Love Surprise ❤️", page_icon="❤️")

PASSWORD = "chand123"

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("🔒 Secret Surprise")
    st.write("❤️ Enter the password to open the surprise ❤️")

    password = st.text_input("Password", type="password")

    if st.button("Unlock ❤️"):
        if password == PASSWORD:
            st.session_state.login = True
            st.rerun()
        else:
            st.error("❌ Wrong Password!")

    st.stop()

st.balloons()

st.title("❤️ A Special Surprise ❤️")
st.markdown("# 🌙 Dear Chand (Mokadam) 🌙")

st.write("💖 Every day with you feels more beautiful.")
st.write("💖 You are the most special person in my life.")
st.write("💖 Thank you for always making me smile.")
st.write("💖 I Love You Forever ❤️")

st.markdown("---")
st.markdown("## 👑 From: ASAD خان 👑")

st.snow()

if st.button("❤️ Click for a Surprise ❤️"):
    st.balloons()
    st.success("🌹 No matter what happens, you will always be my Chand. I Love You Forever ❤️")
