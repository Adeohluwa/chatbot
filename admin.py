import time
import streamlit as st
from chatbot.db import get_pending_enquiries, get_all_feedbacks, save_enquiry_answer


enquiries = get_pending_enquiries()
feedbacks = get_all_feedbacks()


# enquiries_list = list(bursary_data.keys())
enquiries_list = [each for each in enquiries]
# print(enquiries_list)


# Admin credentials
# These are the email and password for the admin user
ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "admin_password"


# Admin page function
# This function creates an admin page that can only be accessed by the admin user
def admin_page():
    if "is_admin" not in st.session_state or not st.session_state["is_admin"]:
        admin_login_page()
    else:
        st.markdown(html_content, unsafe_allow_html=True)
        respond_to_enquiry()
        # Logout button
        if st.button("Logout"):
            del st.session_state["is_admin"]
            st.warning("You have been logged out")
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





def get_question_items(enquiries):
    html = ""
    if enquiries:
        for enquiry in enquiries:
            html += f"""<div class="question-item"><p>{enquiry["enquiry"]}</p><button>Answer</button></div>"""
        return html
    return '<div class="question-item"><p>None for now</p></div>'


def get_feedback_items(feedbacks):
    html = ""
    if feedbacks:
        for feedback in feedbacks:
            html += f'<div class="feedback-item"><p>Feedback: {feedback["feedback"]}\n Rating: {feedback["rating"]} stars</p><button>View</button></div>'
        return html
    return f'<div class="feedback-item"><p>Feedback: None for now\n</p><button>View</button></div>'


def get_enquiry_id(text):
    uid = [entry["id"] for entry in enquiries_list if entry["enquiry"] == text][0]
    return uid


def respond_to_enquiry():
    st.title("Admin Response Section")
    enquiry = st.selectbox("Respond to specific questions students have asked", [each["enquiry"] for each in enquiries_list])
    if enquiry:
        uid = get_enquiry_id(enquiry)
        response = st.text_area("Response")
        submit_button = st.button("Submit Response")
        if submit_button:
            save_enquiry_answer(uid, response)
            st.success("Response submitted!")
            time.sleep(3)
            st.rerun()

# print(get_enquiry_id("why is there no rail transport?"))

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Babcock Admin Dashboard</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
        }}
        .container {{
            width: 80%;
            margin: auto;
            overflow: hidden;
        }}
        .dashboard-card {{
            width: 30%;
            padding: 20px;
            margin: 10px;
            float: left;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            text-align: center;
        }}
        .question-list {{
            width: 100%;
            padding: 20px;
            margin: 10px;
            float: left;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        }}
        .question-item {{
            margin-bottom: 10px;
        }}
        .feedback-list {{
            width: 100%;
            padding: 20px;
            margin: 10px;
            float: left;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        }}
        .feedback-item {{
            margin-bottom: 10px;
        }}

</head>
<body>
    <div class="container">
        <h1>Babcock Admin Dashboard</h1>
        <div class="dashboard-card">
            <h2>New Students</h2>
            <p>150</p>
        </div>
        <div class="dashboard-card">
            <h2>Total Courses</h2>
            <p>250</p>
        </div>
        <div class="dashboard-card">
            <h2>Total Faculty</h2>
            <p>100</p>
        </div>
        <div class="dashboard-card">
            <h2>New Applications</h2>
            <p>50</p>
        </div>
        <div class="question-list">
            <h2>New Unanswered Questions</h2>
            {get_question_items(enquiries)}
        </div>
        <div class="feedback-list">
            <h2>All Feedbacks</h2>
            {get_feedback_items(feedbacks)}
        </div>
    </div>


</body>
</html>

"""