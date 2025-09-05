Automated B2B Supplier Onboarding Workflow

1. Project Summary
This project is a functional, proof-of-concept implementation of an automated B2B supplier onboarding system. It was developed to address the common operational inefficiencies found in manual procurement and finance workflows, such as long onboarding times, manual data entry errors, and a lack of process visibility.

The system provides a simple web interface for suppliers to submit their information. This data is then processed by a serverless backend that performs validation and, upon success, triggers a real-time notification in a designated Slack channel to initiate the internal approval process.

2. Live Demonstration
The fully deployed application can be accessed and tested at the following links:

Frontend Web Form: https://supplier-onboarding-automation.vercel.app/frontend/

Approval Notifications Channel: View in Slack (Note: Access may be required)

3. Core Features
Web-Based Data Entry: A clean, user-friendly HTML form for suppliers to submit their name and GSTIN.

Serverless Backend API: A robust Python backend built with Flask and deployed on Vercel as a serverless function for scalability and cost-efficiency.

Automated Data Validation: The backend includes logic to validate incoming data (e.g., ensuring GSTIN format is correct) and rejects invalid submissions.

Real-time Internal Notifications: Successful submissions trigger an automated message to a pre-configured Slack channel, alerting the relevant team to begin the approval process.

Secure Configuration: Sensitive information, such as the Slack Webhook URL, is handled securely using environment variables and is not exposed in the source code.

Unit Tested: The backend logic is supported by a suite of unit tests written with pytest to ensure reliability and facilitate future development.

4. Technology Stack
Area

Technology / Service

Frontend

HTML5, CSS3, JavaScript (ES6+)

Backend

Python 3.9, Flask

Platform

Vercel (Serverless Functions & Static Hosting)

Testing

pytest, pytest-mock

Integration

Slack (via Incoming Webhooks)

5. Project Structure
The project is organized into distinct frontend, backend, and testing directories for clarity and maintainability.

/
├── api/
│   ├── __init__.py
│   └── onboard.py         # Serverless backend logic
│
├── frontend/
│   ├── index.html         # The HTML form
│   ├── style.css          # Styling for the form
│   └── script.js          # Form submission logic
│
├── tests/
│   └── test_onboard.py    # Unit tests for the API
│
├── .gitignore             # Git ignore configuration
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies

6. Local Development and Testing
Prerequisites
Python 3.9+ and pip

Node.js and npm (to install the Vercel CLI)

A Vercel account

Setup Instructions
Clone the repository:

git clone <your-repository-url>
cd supplier-onboarding-automation

Create and activate a Python virtual environment:

python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`

Install Python dependencies:

pip install -r requirements.txt

Install the Vercel CLI:

npm i -g vercel

Run the local development server:
To simulate the Vercel environment locally, use the vercel dev command. This will start a server that runs both your frontend and your Python backend.

vercel dev

Running the Unit Tests
To verify the integrity of the backend logic, run the test suite using pytest.

python -m pytest
