html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>University Admin Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
        }
        .dashboard-card {
            width: 30%;
            padding: 20px;
            margin: 10px;
            float: left;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            text-align: center;
        }
        .question-list {
            width: 100%;
            padding: 20px;
            margin: 10px;
            float: left;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        }
        .question-item {
            margin-bottom: 10px;
        }
        .news-list {
            width: 100%;
            padding: 20px;
            margin: 10px;
            float: left;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        }
        .news-item {
            margin-bottom: 10px;
        }
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
          <div class="question-item">
              <p>What type of halls are available to students in the main campus?</p>
              <button>Answer</button>
          </div>
          <div class="question-item">
              <p>How is hostel accommodation assigned to students?</p>
              <button>Answer</button>
          </div>
          <div class="question-item">
              <p>What are the costs of different types of hostel accommodation?</p>
              <button>Answer</button>
          </div>
          <div class="question-item">
              <p>Can parents visit the hostel facilities before the academic year begins?</p>
              <button>Answer</button>
          </div>
          <div class="question-item">
              <p>Are there any specific requirements or documentation needed for hostel registration?</p>
              <button>Answer</button>
          </div>
          <div class="question-item">
              <p>What amenities are provided in the hostel rooms?</p>
              <button>Answer</button>
          </div>
          <div class="question-item">
              <p>Is there a separate hostel for male and female students?</p>
              <button>Answer</button>
          </div>
          <div class="question-item">
              <p>What security measures are in place within the hostel premises?</p>
              <button>Answer</button>
          </div>
          <div class="question-item">
              <p>Are laundry services been rendered to students in the hostel?</p>
              <button>Answer</button>
          </div>
          <div class="question-item">
              <p>How are maintenance issues and repairs addressed in the hostel?</p>
              <button>Answer</button>
          </div>
          <!-- Add more questions as needed -->
      </div>

        
</body>
</html>
"""