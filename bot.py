import streamlit as st
from chatbot.model import handle_query
from chatbot.data import faq_data, bursary_data, registry_data, courses_data




# Get a list of predefined questions from the data
predefined_questions = list(faq_data.keys())
bursary_predefined_questions = list(bursary_data.keys())
registry_predefined_questions = list(registry_data.keys())
courses_predefined_questions = list(courses_data.keys())





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
