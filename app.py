import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from chatbot.model import handle_query
from chatbot.data import faq_data, bursary_data, registry_data, courses_data, exam_schedule_data, school_fees_data




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
    # if "DM" in response:
    #     st.write(f"**Answer:** All of our staffs are busy, someone will get back to you shortly")
    #     # send topic to staff


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
            # auth.verify_password(email=email, password=password)
            print(user.uuid)
            # st.session_state.user_id = user.uid
            # st.session_state.user_email = user.email
            # st.session_state.is_user_logged_in = True
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.is_user_logged_in = True
            st.success("Login Successful")
            qa_bot()

            # st.session_state.username = user.uid
            # st.session_state.user_email = user.email
            # st.session_state.signed_out = True
            # st.session_state.sign_out = True
            # st.write("Login Successful")
        except:
            st.warning('Login Failed')
    return authenticate_user()


# def display_login_signup():
#     choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
#     email = st.text_input('Email Address')
#     password = st.text_input('Password', type='password')

#     if choice == 'Sign up':
#         username = st.text_input("Enter your unique username")
#         if st.button('Create my account'):
#           try:
#             auth.create_user(email=email, password=password, uid=username)
#             st.success('Account created successfully!')
#             st.markdown('Please Login using your email and password')
#             st.balloons()
#           except:
#             st.warning("User already exists!")

#     else:
#         st.button('Login', on_click=lambda: login(email, password))




def main():
  welcome_user()
  qa_bot()
    # display_login_signup()
    # display_user_info()




  

if __name__ == "__main__":
    main()