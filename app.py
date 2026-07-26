import streamlit.components.v1 as components

components.html("""
<style>
body{
    background:linear-gradient(135deg,#fff8dc,#e6ffe6);
    overflow:hidden;
}

.welcome{
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#d63384;
    animation:zoom 2s ease-in-out infinite alternate;
}

.item{
    position:fixed;
    font-size:35px;
    animation:float 10s linear infinite;
}

@keyframes zoom{
    from{transform:scale(0.9);}
    to{transform:scale(1.1);}
}

@keyframes float{
    0%{transform:translateY(100vh);}
    100%{transform:translateY(-120px);}
}
</style>

<div class="welcome">🌸 Welcome Brother SAMAD 🌸</div>

<div class="item" style="left:10%;animation-delay:0s;">🌹</div>
<div class="item" style="left:25%;animation-delay:2s;">🌼</div>
<div class="item" style="left:40%;animation-delay:4s;">🐝</div>
<div class="item" style="left:55%;animation-delay:1s;">🌹</div>
<div class="item" style="left:70%;animation-delay:3s;">🌼</div>
<div class="item" style="left:85%;animation-delay:5s;">🐝</div>


""", height=350)
