import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
from chatbot.model import handle_query
from chatbot.data import faq_data, bursary_data, registry_data, courses_data

# Initialize Firebase app
if not firebase_admin._apps:
    cred = credentials.Certificate("babcock-6b68d-firebase-adminsdk-zakzq-be757502db.json")
    default_app = firebase_admin.initialize_app(cred)

# Get a list of predefined questions from the FAQ data
predefined_questions = list(faq_data.keys())
bursary_predefined_questions = list(bursary_data.keys())
registry_predefined_questions = list(registry_data.keys())
courses_predefined_questions = list(courses_data.keys())

def welcome_user():
    st.title("Babcock FAQ Chatbot")

def display_answer(topic):
    response = handle_query(topic)
    st.write(f"**Answer:** {response}")

def qa_bot():
    # Display predefined questions as a selectbox or multiselect
    courses_question = st.selectbox("Some questions people ask about Courses", courses_predefined_questions)
    if courses_question:
        display_answer(courses_question)
   
    # Display predefined questions as a selectbox or multiselect
    bursary_question = st.selectbox("Some questions people ask about Bursary", bursary_predefined_questions)
    if bursary_question:
        display_answer(bursary_question)

    user_query = st.text_input("Ask a question")
    if user_query:
        display_answer(user_query)

def login(email, password):
    def authenticate_user():
        try:
            user = auth.get_user_by_email(email)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.is_user_logged_in = True
            st.success("Login Successful")
            qa_bot()
            # Display signup button
            if st.button('Sign Up'):
                # Call function to display signup form
                display_signup_form()
        except Exception as e:
            st.warning('Login Failed')
            st.error(f"Error: {e}")
    return authenticate_user()

def display_signup_form():
    username = st.text_input("Enter your unique username")
    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')
    if st.button('Create my account'):
        try:
            auth.create_user(email=email, password=password, uid=username)
            st.success('Account created successfully!')
            st.markdown('Please Login using your email and password')
            st.balloons()
        except Exception as e:
            st.warning("User creation failed!")
            st.error(f"Error: {e}")

def main():
    welcome_user()
    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')
    if st.button('Login', on_click=lambda: login(email, password)):
        pass

if __name__ == "__main__":
    main()
