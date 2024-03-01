![Babcock Chatbot]("babcockfaq.png")


# Streamlit Chatbot App

This project is a simple chatbot application built using Streamlit and Firebase Authentication.



## Table of Contents

- [Project Structure](#project-structure)
- [Getting started](#getting-started)
- [Prerequisites](#prerequisits)
- [Installation](#project-structure)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)



## Project Structure
```bash
$ .
├── app.py
├── babcock-6b68d-firebase-adminsdk-zakzq-be757502db.json
├── chatbot
│   ├── data.py
│   ├── __init__.py
│   ├── model.py
│   └── __pycache__
└── README.md
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python 3.6 or higher installed on your system. You can download it from the official Python website.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Adeohluwa/chatbot.git
```

```bash
cd chatbot
```

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate  # On Unix or MacOS
venv\Scripts\activate  # On Windows
```

```bash
pip install -r requirements.txt
```

```bash
streamlit run app.py
```

## Features
- [x] User authentication (login/signup)
- [x] Interactive chat interface
- [x] Predefined responses

## Contributing

Contributions to the Streamlit Chatbot App are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes to the branch (`git push origin feature/your-feature-name`).
5. Create a new pull request.

Please follow these guidelines when contributing:

- Make sure your code follows the project's coding standards.
- Provide detailed information in your pull request description.
- Test your changes thoroughly before submitting a pull request.

Thank you for contributing to the project!


## License
[MIT License](LICENSE)
