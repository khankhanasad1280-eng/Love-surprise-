import streamlit as st

st.set_page_config(page_title="💙 Best Friend 💙", page_icon="🤝")

PASSWORD = "IKRAM FRIEND"

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("🔒 Secret Friendship")
    st.write("💙 Please Enter Password")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Unlock 🤝"):
        if password == PASSWORD:
            st.session_state.login = True
            st.rerun()
        else:
            st.error("❌ Wrong Password!")

    st.stop()

st.balloons()

st.title("🤝 A Special Message For IKRAM 🤝")

st.markdown("""
# 💙 Dear IKRAM 💙

🌹 A true friend is one of life's greatest blessings.

🌹 You have always been a kind and sincere friend.

🌹 Your friendship means more than words can describe.

🌹 Never stop believing in yourself.

🌹 Keep smiling because your smile inspires others.

🌹 Stay humble, stay honest and always help people.

🌹 Success comes to those who never give up.

🌹 Always respect your parents and teachers.

🌹 Keep your heart clean and your intentions pure.

🌹 A real friend stands beside you in every situation.

## ✨ Poetry

**Friends like you are rare to find,  
Kind at heart and strong in mind.  
Through every joy and every pain,  
True friendship will always remain.**

## 🌹 Advice

💙 Believe in yourself.

💙 Never lose hope.

💙 Keep learning every day.

💙 Respect everyone.

💙 Pray to Allah and stay thankful.

## 🌙 اردو پیغام

تم صرف ایک دوست نہیں،
بلکہ ایک سچے اور مخلص انسان ہو۔

اللہ تمہیں ہمیشہ خوش رکھے،
تمہاری ہر دعا قبول ہو،
اور تم زندگی میں ہمیشہ کامیاب رہو۔

## 🌹 اردو شاعری

دوستی کا رشتہ انمول ہوتا ہے،
ہر دل کے بہت قریب ہوتا ہے۔

وقت بدل جائے تو بدل جائے،
سچا دوست ہمیشہ نصیب ہوتا ہے۔

💙 ہمیشہ خوش رہو، مسکراتے رہو۔

## 👑 From: ASAD KHAN
""")

st.success("🤝 Friendship Forever 🤝")
