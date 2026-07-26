import streamlit as st

st.set_page_config(page_title="❤️ Secret Surprise ❤️", page_icon="❤️")

PASSWORD = "JIGRI YAAR ASAD خان AND CHAND"

if "ok" not in st.session_state:
    st.session_state.ok = False

if not st.session_state.ok:
    st.title("🔒 Secret Surprise")
    st.write("Enter the password to continue ❤️")
    pwd = st.text_input("Password", type="password")
    if st.button("Unlock ❤️"):
        if pwd == PASSWORD:
            st.session_state.ok = True
            st.rerun()
        else:
            st.error("Wrong password!")
    st.stop()

st.balloons()
st.snow()

st.title("❤️ JIGRI YAAR ❤️")
st.markdown("## 🌹 Welcome to the Surprise 🌹")

messages = [
"💖 Tum mera JIGRI YAAR ho.",
"💖 Tumhari dosti meri zindagi ki sab se badi khushi hai.",
"💖 Allah tumhein hamesha khush rakhe.",
"💖 You are my best friend.",
"💖 Friends forever.",
"💖 Stay blessed.",
"💖 Never give up.",
"💖 You are special.",
"💖 Thank you for always being there.",
"💖 میری دعا ہے کہ تم ہمیشہ خوش رہو۔",
"💖 تم میرے سب سے پیارے جگری یار ہو۔",
"💖 اللہ تمہیں کامیاب کرے۔",
"🌹 شعر:",
"دوستی ایک خوبصورت رشتہ ہے۔",
"جو ہمیشہ دل میں رہتا ہے۔",
"👑 From: ASAD خان ❤️"
]

for m in messages:
    st.markdown(f"### {m}")

if st.button("🎁 Final Surprise"):
    st.balloons()
    st.success("❤️ JIGRI YAAR FOREVER ❤️")
        
