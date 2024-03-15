import time
from db import auth, save_feedback, save_enquiry
import streamlit as st
from streamlit_star_rating import st_star_rating

from chatbot.model import handle_query
from chatbot.data import faq_data, bursary_data, registry_data, courses_data




# Get a list of predefined questions from the data
predefined_questions = list(faq_data.keys())
bursary_predefined_questions = list(bursary_data.keys())
registry_predefined_questions = list(registry_data.keys())
courses_predefined_questions = list(courses_data.keys())
hostel_predefined_questions = list(courses_data.keys())
# hostel_predefined_questions =




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

    registry_question = st.selectbox("Some questions people ask about Registry", registry_predefined_questions)
    if registry_question:
        display_answer(registry_question)

    hostel_question = st.selectbox("Some questions people ask about Hostels", hostel_predefined_questions)
    if hostel_question:
        display_answer(hostel_question)

    user_query = st.text_input("Ask a question")
    if user_query:
        display_answer(user_query)

# Ask Admin button
    if st.button("Ask Admin") or st.session_state.get("ask_admin"):
        st.session_state["ask_admin"] = True
        st.write("What would you like to ask the administrative staff?")
        enquiry_text = st.text_area("Enquiry")

        if st.button("Send Message"):
            user = st.session_state["user"]
            decoded_token = auth.verify_id_token(user["idToken"])
            uid = decoded_token['uid'] 
            print(uid)
           
            save_enquiry(uid, enquiry_text)

            st.success("Message received, a staff will reach out to you shortly!")
            time.sleep(2)
            st.session_state["ask_admin"] = False
            del enquiry_text
            st.rerun()





    # Star rating
    stars = st_star_rating("Please take some time to rate your experience", maxValue=5, defaultValue=3, key="rating")

    # Track whether the stars have been clicked
    if stars != 3:
        # User feedback form
        st.write("Please provide your feedback:")
        feedback_text = st.text_area("Feedback")

        # Submit button
        if st.button("Submit Feedback"):
            user = st.session_state["user"]
            decoded_token = auth.verify_id_token(user["idToken"])
            uid = decoded_token['uid'] 
            print(uid)
           
            save_feedback(uid, feedback_text, stars)
            st.success("Thank you for your feedback!")




    # Logout button
    if st.button("Logout"):
        del st.session_state["user"]
        st.warning("You have been logged out")
        time.sleep(2)
        st.rerun()
