import streamlit as st

st.set_page_config(page_title="❤️ Secret Love Surprise ❤️", page_icon="❤️")

PASSWORD = "JIGRI YAAR ASAD خان AND CHAND"

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("🔐 Secret Surprise ❤️")
    st.write("Password enter karo ❤️")

    password = st.text_input("Password", type="password")

    if st.button("Unlock ❤️"):
        if password == PASSWORD:
            st.session_state.login = True
            st.rerun()
        else:
            st.error("❌ Wrong Password")

    st.stop()

st.balloons()

st.title("❤️ JIGRI YAAR ❤️")

messages = [
"🌹 Tum mera sab se pyara dost ho.",
"🌹 Tum mera JIGRI YAAR ho.",
"🌹 Tumhari dosti meri zindagi ki sab se badi khushi hai.",
"🌹 Allah tumhe hamesha khush rakhe.",
"🌹 Main hamesha tumhare saath hoon.",
"🌹 Tum bohat special ho.",
"🌹 Tumhari smile sab se best hai.",
"🌹 Never change yourself.",
"🌹 You are amazing.",
"🌹 You are my best friend.",
"🌹 Stay happy forever.",
"🌹 Stay blessed.",
"🌹 You make everyone smile.",
"🌹 Your friendship is priceless.",
"🌹 Thank you for everything.",
"🌹 Friends forever.",
"🌹 You are a real hero.",
"🌹 Believe in yourself.",
"🌹 Keep shining.",
"🌹 Always stay strong.",
"❤️ میری دعا ہے کہ تم ہمیشہ خوش رہو۔",
"❤️ تم میری زندگی کا خوبصورت حصہ ہو۔",
"❤️ تم جیسا دوست قسمت والوں کو ملتا ہے۔",
"❤️ تم ہمیشہ کامیاب رہو۔",
"❤️ اللہ تمہیں ہر خوشی دے۔",
"❤️ تمہاری دوستی پر فخر ہے۔",
"❤️ ہمیشہ مسکراتے رہو۔",
"❤️ تم بہت اچھے انسان ہو۔",
"❤️ کبھی بدلنا مت۔",
"❤️ تم میری طاقت ہو۔",
"✨ دوستی وہ خزانہ ہے جو کبھی ختم نہیں ہوتا۔",
"✨ تم جیسا یار ہر کسی کو نہیں ملتا۔",
"✨ ہماری دوستی ہمیشہ قائم رہے۔",
"✨ تمہاری عزت ہمیشہ میرے دل میں رہے گی۔",
"✨ تم میرے بھائی جیسے ہو۔",
"📜 شعر:",
"دوستی نام ہے وفا کا،",
"دوستی نام ہے دعا کا۔",
"دوستی نام ہے مسکراہٹ کا،",
"دوستی نام ہے محبت کا۔",
"💖 You are unforgettable.",
"💖 Thank you for being my friend.",
"💖 Best Friends Forever.",
"💖 Stay healthy.",
"💖 Stay successful.",
"💖 Never give up.",
"💖 You are my JIGRI YAAR.",
"💖 I respect you.",
"💖 I wish you all the happiness.",
"👑 From: ASAD خان ❤️"
]

for line in messages:
    st.markdown(f"## {line}")

st.success("❤️ JIGRI YAAR FOREVER ❤️")
