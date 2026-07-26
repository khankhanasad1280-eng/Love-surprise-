import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="Brother Samad ❤️", page_icon="🌹")

PASSWORD = "BROTHER SAMAD"

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("🔒 Secret Message")
    password = st.text_input("🔑 Enter Password", type="password")

    if st.button("Unlock ❤️"):
        if password == PASSWORD:
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Wrong Password!")

    st.stop()

components.html("""
<style>
body{
background:#fff8f0;
overflow:hidden;
}
h1{
text-align:center;
color:#d63384;
animation:zoom 2s infinite alternate;
}
.item{
position:fixed;
font-size:35px;
animation:float 8s linear infinite;
}
@keyframes float{
0%{transform:translateY(100vh);}
100%{transform:translateY(-120px);}
}
@keyframes zoom{
from{transform:scale(0.9);}
to{transform:scale(1.1);}
}
</style>

<h1>🌸 WELCOME BROTHER SAMAD 🌸</h1>

<div class="item" style="left:5%">🌹</div>
<div class="item" style="left:20%;animation-delay:1s">🌼</div>
<div class="item" style="left:35%;animation-delay:2s">🐝</div>
<div class="item" style="left:50%;animation-delay:3s">🌹</div>
<div class="item" style="left:65%;animation-delay:4s">🌼</div>
<div class="item" style="left:80%;animation-delay:5s">🐝</div>
""", height=400)

time.sleep(4)

st.balloons()

st.title("❤️ Dear Brother SAMAD ❤️")

st.markdown("""
## My Dear Brother,

You are not only my brother,
you are my strength,
my support,
and my biggest blessing.

Thank you for always caring for me.

May Allah bless you with happiness,
success and good health.

Never stop believing in yourself.

Always smile.

Always pray.

Always stay kind.

### اردو پیغام

پیارے بھائی سماد،

آپ میری زندگی کی سب سے بڑی نعمت ہیں۔

اللہ تعالیٰ آپ کو ہمیشہ
خوش رکھے،
صحت دے،
کامیابی دے،
اور ہر خوشی عطا فرمائے۔

### شاعری

بھائی وہ رشتہ ہے،
جو ہر مشکل میں ساتھ دیتا ہے۔

اللہ آپ کو ہمیشہ اپنی امان میں رکھے۔

❤️ From: ASAD KHAN ❤️
""")

st.success("🤲 Allah Bless You Always ❤️")
