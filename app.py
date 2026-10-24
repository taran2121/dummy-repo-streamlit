import streamlit as st

st.set_page_config(page_title="Dummy Streamlit App", page_icon="🚀")
st.title("Dummy Streamlit App")
st.write("This is a minimal app for testing Streamlit Cloud deployment.")

with st.form("demo_form"):
    name = st.text_input("Your name", placeholder="Jane Doe")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if name:
            st.success(f"Hello, {name}! Your app is running correctly.")
        else:
            st.success("Hello! Your app is running correctly.")

st.metric("Status", "Healthy")
