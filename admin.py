import streamlit as st
from db import get_pending_enquiries, get_all_feedbacks, save_enquiry_answer

enquiries = get_pending_enquiries()
feedbacks = get_all_feedbacks()

for each in feedbacks:
    print(each)

def get_question_items(enquiries):
    html = ""
    for enquiry in enquiries:
        html += f'<div class="question-item"><p>{enquiry["enquiry"]}</p><button>Answer</button></div>'
    return html


def get_feedback_items(feedbacks):
    html = ""
    for feedback in feedbacks:
        html += f'<div class="feedback-item"><p>{feedback["feedback"]}</p><button>View</button></div>'
    return html


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
    </style>
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