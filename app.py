import math
import streamlit as st

st.set_page_config(page_title="NemoCalc", page_icon="🧮", layout="centered")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🧮 NemoCalc")
st.caption("A cleaner calculator with quick math, safer division, and a small history panel.")

with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("First number", value=0.0, step=1.0, key="first_number")
    with col2:
        num2 = st.number_input("Second number", value=0.0, step=1.0, key="second_number")

    operation = st.selectbox(
        "Operation",
        ["Add", "Subtract", "Multiply", "Divide", "Power", "Modulus"],
    )

    calculate = st.button("Calculate", type="primary", use_container_width=True)

result = None
expression = None

if calculate:
    try:
        if operation == "Add":
            result = num1 + num2
            expression = f"{num1} + {num2}"
        elif operation == "Subtract":
            result = num1 - num2
            expression = f"{num1} - {num2}"
        elif operation == "Multiply":
            result = num1 * num2
            expression = f"{num1} × {num2}"
        elif operation == "Divide":
            expression = f"{num1} ÷ {num2}"
            if num2 == 0:
                st.error("Cannot divide by zero.")
            else:
                result = num1 / num2
        elif operation == "Power":
            result = math.pow(num1, num2)
            expression = f"{num1}^{num2}"
        elif operation == "Modulus":
            expression = f"{num1} % {num2}"
            if num2 == 0:
                st.error("Cannot mod by zero.")
            else:
                result = num1 % num2

        if result is not None:
            st.success(f"Result: {result}")
            st.session_state.history.insert(0, f"{expression} = {result}")
            st.session_state.history = st.session_state.history[:8]
    except Exception as exc:
        st.error(f"Something went wrong: {exc}")

with st.expander("Quick actions", expanded=True):
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        if st.button("Swap numbers", use_container_width=True):
            st.session_state["first_number"] = num2
            st.session_state["second_number"] = num1
            st.rerun()
    with col_b:
        if st.button("Clear history", use_container_width=True):
            st.session_state.history = []
            st.rerun()
    with col_c:
        st.metric("Saved calculations", len(st.session_state.history))

with st.expander("Recent calculations", expanded=True):
    if st.session_state.history:
        for item in st.session_state.history:
            st.write(f"- {item}")
    else:
        st.caption("No calculations yet.")
