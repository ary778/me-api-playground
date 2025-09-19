Me API Playground:
This is the backend API for my personal portfolio website, built with Django and Django REST Framework. It serves all the necessary data for my professional profile, including project details, skills, and contact information.

🌐 Live Links
Frontend URL: [https://me-api-playground-frontend-m54p.onrender.com/index.html]

Backend API URL: [https://me-api-backend-ie05.onrender.com/]

🏗️ Architecture
The project uses a modern, decoupled architecture. The backend and frontend are separate applications, and the database is a managed service.

Frontend: A static website built with HTML, CSS, and vanilla JavaScript. The code for the frontend is located in a separate repository.

Deployment: Deployed as a Static Site on Render.

Backend: A RESTful API built with Django and Django REST Framework.

Deployment: Deployed as a Web Service on Render, running on a Gunicorn server.

Database: A PostgreSQL database to store all portfolio data.

Deployment: Deployed as a managed PostgreSQL instance on Render.

⚙️ Setup and Installation
Local Development
Prerequisites:

Python 3.10+

PostgreSQL

Git

Clone the repository:

Bash

git clone https://github.com/Ary778/me-api-playground.git
cd me-api-playground
Set up a virtual environment and install dependencies:

Bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the project root and add your local database credentials and a secret key:

Code snippet

SECRET_KEY='your-strong-secret-key'
DB_NAME='your_db_name'
DB_USER='your_db_user'
DB_PASSWORD='your_db_password'
Run Database Migrations:

Bash

python manage.py migrate
Run the development server:

Bash

python manage.py runserver
The API will be available at http://127.0.0.1:8000/.

Production (Render)
Deployment is automated via Render. The render.yaml file and the build.sh script in the repository handle the entire process. Key steps include:

Installing dependencies from requirements.txt.

Running collectstatic to gather all static files.

Running migrate to apply database schema changes.

Starting the server with the gunicorn core.wsgi command.

Environment variables like DATABASE_URL and SECRET_KEY are configured securely in the Render dashboard.

🗄️ Database Schema
The API is centered around a single Profile model which has one-to-many relationships with all other models.

Profile: The core model for personal information.

name (CharField)

email (EmailField)

bio (TextField)

github_url (URLField)

linkedin_url (URLField)

portfolio_url (URLField)

Skill: A skill linked to a profile.

profile (ForeignKey to Profile)

name (CharField)

level (CharField, e.g., "Intermediate")

Project: A project linked to a profile.

profile (ForeignKey to Profile)

title (CharField)

description (TextField)

github_link (URLField)

live_url (URLField)

Experience: A work experience entry linked to a profile.

profile (ForeignKey to Profile)

company (CharField)

position (CharField)

start_date (DateField)

end_date (DateField, nullable)

Education: An education entry linked to a profile.

profile (ForeignKey to Profile)

school (CharField)

degree (CharField)

start_date (DateField)

end_date (DateField, nullable)

Certification: A certification linked to a profile.

profile (ForeignKey to Profile)

name (CharField)

issuing_organization (CharField)

issue_date (DateField)

Award: An award linked to a profile.

profile (ForeignKey to Profile)

name (CharField)

year (IntegerField)

📟 API Usage (cURL Examples)
Here are a few examples of how to interact with the API.

Get Profile Information

Bash

curl https://me-api-backend-ie05.onrender.com/api/profile/

For Individual Profile Information

Bash 

curl https://me-api-backend-ie05.onrender.com/api/profile/[id]/

⚠️ Known Limitations
No Authentication: All API endpoints are public and do not require authentication. This is intentional for a public portfolio but would need to be added for a multi-user application.

Rate Limiting: No rate limiting is currently implemented.

Free Tier Performance: The application is deployed on Render's free tier. Services may "spin down" after a period of inactivity, causing a delay of up to 30 seconds on the first request.

📫 Contact & Resume
Resume: [https://drive.google.com/file/d/17_eFRMvHZO9W0DeLpoNdTZQ-d1Ea_nRO/view?usp=drive_link]

LinkedIn: [https://linkedin.com/in/aryansuthar]

Email: [aryansuthar71@gmail.com]
