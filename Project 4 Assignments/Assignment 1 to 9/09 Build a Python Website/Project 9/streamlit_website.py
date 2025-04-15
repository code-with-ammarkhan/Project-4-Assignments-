import streamlit as st

# Sidebar navigation
st.set_page_config(page_title="My Streamlit Website", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Home Page
if page == "Home":
    st.title("🏠 Welcome to My Python Website")
    st.write("""
        This is a basic multi-page website built with **Streamlit**.  
        You can explore different sections using the sidebar.
    """)
    st.image("https://source.unsplash.com/800x300/?technology,code", caption="Powered by Python", use_container_width=True)

# About Page
elif page == "About":
    st.title("👨‍💻 About This Project")
    st.write("""
        This website is made using **Streamlit**, a Python library for creating interactive web apps.  
        It demonstrates navigation, page layout, and customization.
    """)
    st.markdown("### 🔧 Features")
    st.markdown("- Simple UI with Sidebar Navigation")
    st.markdown("- Built using Python and Streamlit")
    st.markdown("- Fast and lightweight")

# Contact Page
elif page == "Contact":
    st.title("📬 Contact Us")
    st.write("We'd love to hear from you! Fill out the form below:")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")

    if st.button("Send"):
        if name and email and message:
            st.success("Thanks for reaching out! We'll get back to you soon.")
        else:
            st.warning("Please fill in all fields before sending.")
