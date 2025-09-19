<h1>Me API Playground 🚀</h1>

<p>This is the backend API for an assessment portfolio website, built with Django and Django REST Framework. It serves all the necessary data for my professional profile, including project details, skills, and contact information.</p>

<hr>

<h2>🌐 Live Links</h2>
<ul>
    <li><strong>Frontend URL</strong>: <a href="https://me-api-playground-frontend-m54p.onrender.com/index.html">https://me-api-playground-frontend-m54p.onrender.com/index.html</a></li>
    <li><strong>Backend API URL</strong>: <a href="https://me-api-backend-ie05.onrender.com/">https://me-api-backend-ie05.onrender.com/</a></li>
</ul>

<hr>

<h2>🏗️ Architecture</h2>
<p>The project uses a modern, decoupled architecture. The backend and frontend are separate applications, and the database is a managed service.</p>
<ul>
    <li><strong>Frontend</strong>: A static website built with HTML, CSS, and vanilla JavaScript. The code for the frontend is located in a separate repository.<br>
        <em>Deployment</em>: Deployed as a <strong>Static Site</strong> on Render.</li>
    <li><strong>Backend</strong>: A RESTful API built with Django and Django REST Framework.<br>
        <em>Deployment</em>: Deployed as a <strong>Web Service</strong> on Render, running on a Gunicorn server.</li>
    <li><strong>Database</strong>: A PostgreSQL database to store all portfolio data.<br>
        <em>Deployment</em>: Deployed as a managed <strong>PostgreSQL</strong> instance on Render.</li>
</ul>

<hr>

<h2>⚙️ Setup and Installation</h2>
<h3>Local Development</h3>
<p><strong>Prerequisites</strong>:</p>
<ul>
    <li>Python 3.10+</li>
    <li>PostgreSQL</li>
    <li>Git</li>
</ul>
<p><strong>1. Clone the repository</strong>:</p>
<pre><code>git clone https://github.com/Ary778/me-api-playground.git
cd me-api-playground</code></pre>
<p><strong>2. Set up a virtual environment and install dependencies</strong>:</p>
<pre><code>python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt</code></pre>
<p><strong>3. Configure Environment Variables</strong>:<br>
Create a <code>.env</code> file in the project root and add your local database credentials and a secret key:</p>
<pre><code>SECRET_KEY='your-strong-secret-key'
DB_NAME='your_db_name'
DB_USER='your_db_user'
DB_PASSWORD='your_db_password'</code></pre>
<p><strong>4. Run Database Migrations</strong>:</p>
<pre><code>python manage.py migrate</code></pre>
<p><strong>5. Run the development server</strong>:</p>
<pre><code>python manage.py runserver</code></pre>
<p>The API will be available at <code>http://127.0.0.1:8000/</code>.</p>

<h3>Production (Render)</h3>
<p>Deployment is automated via Render. The <code>render.yaml</code> file and the <code>build.sh</code> script in the repository handle the entire process. Key steps include:</p>
<ul>
    <li>Installing dependencies from <code>requirements.txt</code>.</li>
    <li>Running <code>collectstatic</code> to gather all static files.</li>
    <li>Running <code>migrate</code> to apply database schema changes.</li>
    <li>Starting the server with the <code>gunicorn core.wsgi</code> command.</li>
</ul>
<p>Environment variables like <code>DATABASE_URL</code> and <code>SECRET_KEY</code> are configured securely in the Render dashboard.</p>

<hr>

<h2>🗄️ Database Schema</h2>
<p>The API is centered around a single <strong>Profile</strong> model which has one-to-many relationships with all other models.</p>
<ul>
    <li><strong>Profile</strong>: The core model for personal information.
        <ul>
            <li><code>name</code> (CharField)</li>
            <li><code>email</code> (EmailField)</li>
            <li><code>bio</code> (TextField)</li>
            <li><code>github_url</code> (URLField)</li>
            <li><code>linkedin_url</code> (URLField)</li>
            <li><code>portfolio_url</code> (URLField)</li>
        </ul>
    </li>
    <li><strong>Skill</strong>: A skill linked to a profile.
        <ul>
            <li><code>profile</code> (ForeignKey to Profile)</li>
            <li><code>name</code> (CharField)</li>
            <li><code>level</code> (CharField, e.g., "Intermediate")</li>
        </ul>
    </li>
    <li><strong>Project</strong>: A project linked to a profile.
        <ul>
            <li><code>profile</code> (ForeignKey to Profile)</li>
            <li><code>title</code> (CharField)</li>
            <li><code>description</code> (TextField)</li>
            <li><code>github_link</code> (URLField)</li>
            <li><code>live_url</code> (URLField)</li>
        </ul>
    </li>
    <li><strong>Experience</strong>: A work experience entry linked to a profile.
        <ul>
            <li><code>profile</code> (ForeignKey to Profile)</li>
            <li><code>company</code> (CharField)</li>
            <li><code>position</code> (CharField)</li>
            <li><code>start_date</code> (DateField)</li>
            <li><code>end_date</code> (DateField, nullable)</li>
        </ul>
    </li>
    <li><strong>Education</strong>: An education entry linked to a profile.
        <ul>
            <li><code>profile</code> (ForeignKey to Profile)</li>
            <li><code>school</code> (CharField)</li>
            <li><code>degree</code> (CharField)</li>
            <li><code>start_date</code> (DateField)</li>
            <li><code>end_date</code> (DateField, nullable)</li>
        </ul>
    </li>
    <li><strong>Certification</strong>: A certification linked to a profile.
        <ul>
            <li><code>profile</code> (ForeignKey to Profile)</li>
            <li><code>name</code> (CharField)</li>
            <li><code>issuing_organization</code> (CharField)</li>
            <li><code>issue_date</code> (DateField)</li>
        </ul>
    </li>
    <li><strong>Award</strong>: An award linked to a profile.
        <ul>
            <li><code>profile</code> (ForeignKey to Profile)</li>
            <li><code>name</code> (CharField)</li>
            <li><code>year</code> (IntegerField)</li>
        </ul>
    </li>
</ul>

<hr>

<h2>📟 API Usage (cURL Examples)</h2>
<p>Here are a few examples of how to interact with the API.</p>
<p><strong>Get All Profile Information</strong></p>
<pre><code>curl https://me-api-backend-ie05.onrender.com/api/profile/</code></pre>
<p><strong>Get an Individual Profile by ID</strong></p>
<pre><code>curl https://me-api-backend-ie05.onrender.com/api/profile/[id]/</code></pre>

<hr>

<h2>⚠️ Known Limitations</h2>
<ul>
    <li><strong>No Authentication</strong>: All API endpoints are public and do not require authentication. This is intentional for a public portfolio but would need to be added for a multi-user application.</li>
    <li><strong>Rate Limiting</strong>: No rate limiting is currently implemented.</li>
    <li><strong>Free Tier Performance</strong>: The application is deployed on Render's free tier. Services may "spin down" after a period of inactivity, causing a delay of up to 30 seconds on the first request.</li>
</ul>

<hr>

<h2>📫 Contact & Resume</h2>
<ul>
    <li><strong>Resume</strong>: <a href="https://drive.google.com/file/d/17_eFRMvHZO9W0DeLpoNdTZQ-d1Ea_nRO/view?usp=drive_link">View My Resume</a></li>
    <li><strong>LinkedIn</strong>: <a href="https://linkedin.com/in/aryansuthar">linkedin.com/in/aryansuthar</a></li>
    <li><strong>Email</strong>: <a href="mailto:aryansuthar71@gmail.com">aryansuthar71@gmail.com</a></li>
</ul>
