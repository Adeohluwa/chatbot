import streamlit as st
from auth_lib import sign_up, sign_in
import db
from db import auth
# from firebase_admin import credentials, auth, firestore
from bot import qa_bot
from admin import html_content
import time

# Firebase app initialization
# This block of code checks if the Firebase app has been initialized
# If not, it initializes the app using the provided credentials
# if not firebase_admin._apps:
#     cred = credentials.Certificate("babcock-6b68d-firebase-adminsdk-zakzq-be757502db.json")
#     default_app = firebase_admin.initialize_app(cred)


# db = firestore.client()


# Admin credentials
# These are the email and password for the admin user
ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "admin_password"

# Login page function
# This function creates a login page for users
def login_page():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            user = sign_in(email, password)
            st.session_state["user"] = user
            # print(st.session_state)
            # decoded_token = auth.verify_id_token(user["idToken"])
            # uid = decoded_token['uid'] 
            # print(uid)
            st.success("Login successful!")
            time.sleep(2)
            st.rerun()
        except Exception as e:
            st.error(f"Invalid email or password{e}")

    st.markdown("Don't have an account? [Sign Up](#signup)")

# Signup page function
# This function creates a signup page for users
def signup_page():
    st.title("Sign Up")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if password == confirm_password:
            try:
                user = auth.create_user(email=email, password=password)
                st.success(f"User {user.email} created successfully!")
                st.balloons()
                # Redirect to the login page after successful sign-up
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("Passwords do not match")

    st.markdown("Already have an account? [Login](/)")

# Admin page function
# This function creates an admin page that can only be accessed by the admin user
def admin_page():
    if "is_admin" not in st.session_state or not st.session_state["is_admin"]:
        admin_login_page()
    else:
        st.markdown(html_content, unsafe_allow_html=True)
        if st.button("Logout"):
            del st.session_state["is_admin"]
            st.success("Logout successful!")
            time.sleep(2)
            st.rerun()

# Admin login page function
# This function creates a login page for the admin user
def admin_login_page():
    st.title("Admin Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            st.session_state["is_admin"] = True
            st.success("Login successful!")
            time.sleep(2)
            st.rerun()
        else:
            st.error("Invalid email or password")




# Main function
# This function is the entry point of the application
# It checks if a user is logged in and displays the appropriate page
def main():
    if "user" not in st.session_state:
        pages = {
            "Login": login_page,
            "Sign Up": signup_page,
            "Admin": admin_page,
        }

        st.sidebar.title("Navigation")
        selection = st.sidebar.radio("Go to", list(pages.keys()))

        pages[selection]()
    else:
        qa_bot()

if __name__ == "__main__":
    main()