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
st.markdown("---")

st.header("💙 A Special Message")

english = [
"💙 My Dear Brother SAMAD,",
"💙 You are one of the greatest blessings in my life.",
"💙 Thank you for always supporting me.",
"💙 You always encourage me to become better.",
"💙 Your kindness inspires everyone around you.",
"💙 I pray that Allah grants you success.",
"💙 May every dream of yours come true.",
"💙 Stay humble and keep smiling.",
"💙 Never stop believing in yourself.",
"💙 I am proud to have a brother like you."
]

for line in english:
    st.write(line)
    time.sleep(0.2)

st.markdown("## 🌙 اردو پیغام")

urdu = [
"❤️ پیارے بھائی سماد،",
"🌹 آپ میری زندگی کی سب سے بڑی نعمت ہیں۔",
"🌹 اللہ تعالیٰ آپ کو ہمیشہ خوش رکھے۔",
"🌹 آپ کو صحت، عزت اور کامیابی عطا فرمائے۔",
"🌹 آپ کی ہر جائز دعا قبول ہو۔",
"🌹 آپ ہمیشہ مسکراتے رہیں۔",
"🌹 اللہ آپ کو ہر برائی سے محفوظ رکھے۔",
"🌹 میں ہمیشہ آپ کے لیے دعا گو رہوں گا۔"
]

for line in urdu:
    st.write(line)
    time.sleep(0.2)

st.markdown("## 🌹 Poetry")

st.markdown("""
> **A brother's love is pure and true,**  
> **A precious gift from Allah to you.**  
> **Through every joy and every test,**  
> **May Allah always give you the best.**
""")

st.markdown("## 🤲 Last Wish")

st.success("""
🌹 May Allah bless you with happiness,
good health, success and a long life.

❤️ Stay Happy Brother SAMAD ❤️
""")

st.balloons()
st.markdown("---")

st.header("💌 A Letter From My Heart")

letter = """
Dear Brother SAMAD,

Life becomes easier when we have a caring brother.

Thank you for your love.
Thank you for your support.
Thank you for always standing beside me.

May Allah always protect you.

Never lose hope.

Keep smiling.

Keep praying.

Keep believing in yourself.

I am proud to call you my brother.

❤️ Love You Brother ❤️
"""

st.info(letter)

st.markdown("## 🌸 Beautiful Wishes 🌸")

wishes = [
"🤲 May Allah bless you every day.",
"🌹 May every dream come true.",
"✨ May happiness always stay with you.",
"🌼 May success follow you everywhere.",
"🕊️ May your heart always remain peaceful.",
"💙 May your smile never fade.",
"🌟 May Allah protect you from every hardship.",
"❤️ May you always stay healthy."
]

for wish in wishes:
    st.success(wish)
    time.sleep(0.3)

st.markdown("## 📜 Final Urdu Poetry")

st.markdown("""
### 🌹

بھائی وہ دعا ہے،
جو ہر گھر کی رونق ہوتا ہے۔

بھائی وہ سایہ ہے،
جو ہر مشکل میں ساتھ کھڑا ہوتا ہے۔

اللہ کرے تمہاری زندگی
ہمیشہ خوشیوں سے بھری رہے۔

آمین 🤲
""")

st.markdown("## 👑 Final Wish")

st.success("""
❤️ Dear Brother SAMAD ❤️

May Allah always keep you safe,
healthy,
successful,
and happy.

Never stop smiling.

Never stop dreaming.

Always remember,

**You are the best brother in the world.** 🌍❤️
""")

st.snow()
st.balloons()

st.markdown(
"<h1 style='text-align:center;color:red;'>❤️ THANK YOU BROTHER SAMAD ❤️</h1>",
unsafe_allow_html=True,
)
