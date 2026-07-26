import streamlit as st

st.set_page_config(
    page_title="PIP - Pak Investment Profit",
    page_icon="💰",
    layout="wide"
)

st.title("💰 PIP - Pak Investment Profit")
st.subheader("Demo Investment Dashboard")

menu = st.sidebar.selectbox(
    "Select Menu",
    [
        "Dashboard",
        "Investment Plans",
        "Deposit Request",
        "Withdraw Request",
        "Profit Calculator",
        "Profile"
    ]
)

if menu == "Dashboard":
    st.success("Welcome to PIP Demo")
    st.metric("Total Balance", "$0.00")
    st.metric("Total Profit", "$0.00")
    st.metric("Active Plans", "0")

elif menu == "Investment Plans":
    st.header("Investment Plans")

    st.info("Starter Plan")
    st.write("- Investment: $100")
    st.write("- Demo Profit: 5%")

    st.info("Premium Plan")
    st.write("- Investment: $500")
    st.write("- Demo Profit: 8%")

    st.info("VIP Plan")
    st.write("- Investment: $1000")
    st.write("- Demo Profit: 10%")

elif menu == "Deposit Request":
    st.header("Deposit Request (Demo Only)")

    amount = st.number_input("Enter Amount", min_value=0)

    method = st.selectbox(
        "Payment Method",
        ["JazzCash", "Easypaisa", "Bank Transfer"]
    )

    if st.button("Submit Deposit"):
        st.success("Demo deposit request submitted.")

elif menu == "Withdraw Request":
    st.header("Withdraw Request (Demo Only)")

    amount = st.number_input("Withdraw Amount", min_value=0)

    if st.button("Submit Withdraw"):
        st.success("Demo withdrawal request submitted.")

elif menu == "Profit Calculator":
    st.header("Profit Calculator")

    invest = st.number_input("Investment Amount", min_value=0.0)

    rate
