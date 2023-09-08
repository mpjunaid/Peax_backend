# PEAX Backend deployment instruction

The following are the requiremnt for the prerequsite for the deploymnet of the application

1. git
2. python

after you have these to files follow the intructions as below

## Deploying the Django Server

### Step 1: Clone the GitHub Repository

```bash
git clone https://github.com/mpjunaid/Peax_backend.git

cd Peax_backend
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Use 'source venv/bin/activate' on Unix-based systems
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
