st.markdown("""
# ❤️ Tum Mere JIGRI YAAR Ho ❤️

💖 Tum meri zindagi ka bohat khoobsurat hissa ho.

💖 Tum sirf dost nahi ho.

💖 Tum mere sab se pyare JIGRI YAAR ho.

💖 Tum jaisa dost har kisi ko nahi milta.

💖 Main Allah ka shukar ada karta hoon ke tum meri zindagi mein aaye.

💖 Tumhari dosti mere liye ek qeemti tohfa hai.

💖 Jab bhi udaas hota hoon, tum yaad aate ho.

💖 Tumhari muskurahat dil ko sukoon deti hai.

💖 Tumhari har baat dil ko achi lagti hai.

💖 Main dua karta hoon ke tum hamesha khush raho.

💖 Allah tumhari har dua qabool kare.

💖 Allah tumhein lambi aur khush zindagi de.

💖 Kabhi bhi apni muskurahat mat khona.

💖 Tum meri taqat ho.

💖 Tum meri khushi ho.

💖 Tum meri duaon ka hissa ho.

💖 Hamari dosti hamesha salamat rahe.

💖 Main hamesha tumhare saath hoon.

💖 Chahe kitni bhi mushkilein aa jayein.

💖 Main kabhi tumhara saath nahi chhorunga.

💖 Tum mere liye bohat khaas ho.

💖 Tum meri izzat ho.

💖 Tum mera fakhar ho.

💖 Tum meri zindagi ki sab se khoobsurat yaad ho.

💖 Tumhari dosti meri sab se badi daulat hai.

💖 Main hamesha tumhari izzat karunga.

💖 Tum hamesha mere JIGRI YAAR rahoge.

💖 Hamari dosti duniya ki sab se pyari dosti hai.

💖 Kisi ki nazar na lage.

💖 Allah hamari dosti ko hamesha qaim rakhe.

🌹 تم صرف میرے دوست نہیں ہو۔

🌹 تم میرے سب سے پیارے جگری یار ہو۔

🌹 اللہ تمہیں ہمیشہ خوش رکھے۔

🌹 اللہ تمہیں ہر کامیابی عطا کرے۔

🌹 تمہاری ہر خواہش پوری ہو۔

🌹 تمہاری زندگی خوشیوں سے بھر جائے۔

🌹 تم ہمیشہ مسکراتے رہو۔

🌹 تمہاری دوستی میرے لیے فخر ہے۔

🌹 تم ہمیشہ میرے دل میں رہو گے۔

🌹 میں ہمیشہ تمہارا ساتھ دوں گا۔

🌹 کبھی بھی خود کو اکیلا مت سمجھنا۔

🌹 میں ہر مشکل میں تمہارے ساتھ ہوں۔

🌹 ہماری دوستی ہمیشہ قائم رہے گی۔

🌹 اللہ ہمیں ہمیشہ خوش رکھے۔

🌹 تم میرے دل کے بہت قریب ہو۔

🌹 تم میری زندگی کی سب سے خوبصورت نعمت ہو۔

🌹 تم ہمیشہ میرے جگری یار رہو گے۔

❤️ Thank You For Everything.

❤️ Stay Happy Forever.

❤️ I Respect You.

❤️ You Are My Best Friend.

❤️ I Am Lucky To Have You.

❤️ Forever Friends.

# ❤️ From: ASAD KHAN ❤️
password = st.text_input("🔑 Enter Password", type="password")

if st.button("Unlock ❤️"):
    if password == "JIGRI YAAR ASAD خان AND CHAND":
        st.session_state.login = True
        st.rerun()
    else:
        st.error("❌ Wrong Password! Try Again.")import streamlit as st
import base64

def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    b64 = base64.b64encode(data).decode()

    md = f
    <audio autoplay loop controls>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    

    st.markdown(md, unsafe_allow_html=True)

# Password unlock ke baad ye line chalao
autoplay_audio("love.mp3")
