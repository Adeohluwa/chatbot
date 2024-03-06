import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
from bot import qa_bot
from admin import html_content

# Initialize Firebase app
if not firebase_admin._apps:
    cred = credentials.Certificate("babcock-6b68d-firebase-adminsdk-zakzq-be757502db.json")
    default_app = firebase_admin.initialize_app(cred)


def display_answer(topic):
    response = handle_query(topic)
    st.write(f"**Answer:** {response}")


def login_page():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            user = auth.get_user_by_email(email)
            firebase_user = auth.get_user_by_email_and_password(email, password)
            st.success("Login successful!")
            return True
            # st.experimental_rerun()  # Rerun the Streamlit script with the new state
        except Exception as e:
            st.error(f"Invalid email or password{e}")

    st.markdown("Don't have an account? [Sign Up](#signup)")


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

    st.markdown("Already have an account? [Login](#login)")


def admin_page():
    st.markdown(html_content, unsafe_allow_html=True)



def main():
    if "is_user_logged_in" not in st.session_state:
        st.session_state["is_user_logged_in"] = False

    if st.session_state["is_user_logged_in"]:
        qa_bot()
    else:
        pages = {
            "Login": login_page,
            "Sign Up": signup_page,
            "Admin": admin_page,
        }

        st.sidebar.title("Navigation")
        selection = st.sidebar.radio("Go to", list(pages.keys()))

        pages[selection]()


if __name__ == "__main__":
    main()
