# PEAX Backend Deployment Instructions

To successfully deploy the PEAX application backend, ensure you meet the following prerequisites:

1. Git
2. Python

Once you have these prerequisites in place, follow the instructions below for deployment.

## Deploying the Django Server

### Step 1: Clone the GitHub Repository

```bash
git clone https://github.com/mpjunaid/Peax_backend.git
cd Peax_backend
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Use 'venv\Scripts\activate' on Windows
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Migrate the Database

```bash
python manage.py migrate
```

### Step 5: Run the Django Server

```bash
python manage.py runserver
```

The hosted backend will be available at the following URL:

http://localhost:8000

## Project Backend Documentation

The backend primarily operates as an API, with detailed API documentation provided for testing in Postman. You can find the Postman collection file named "PEAX.postman_collection" in the project folder.

Authentication in the backend is implemented using JSON Web Tokens (JWT), where the username (i.e., email) and password are hashed and stored in the database. The authentication process utilizes server-side sessions, and a cookie is sent to the frontend browser.

Password and email validation is enforced; for example, passwords must include at least one lowercase letter, one uppercase letter, one digit, and one special character.

Additionally, the backend performs input validation for various data types, both on the backend and frontend sides.
