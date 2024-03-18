import streamlit as st
from auth_lib import sign_up, sign_in
import db
from db import auth
# from firebase_admin import credentials, auth, firestore
from bot import qa_bot
from admin import html_content, admin_page
import time






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