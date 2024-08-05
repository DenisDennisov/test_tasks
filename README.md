# Project with Django(DRF) and Vue.js

## Requirements

- Python 3.8+
- Node.js
- npm

## Install and start project

### Auto Install
1. start auto_setup.sh;
2. Go to http://localhost:8000.

or...

### Install Django (DRF)

1. Go to the root of the project.
2. Create and activate a virtual environment.
   ```sh
   python3 -m venv venv
   source venv/bin/activate

3. Go to backend folder.
   ```sh
   cd backend/simpleproject

4. Install requirements.
   ```sh
   pip install -r requirements.txt

5. Use migrate and start backend.
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

### Vue
1. Go to frontend folder.
   ```sh
   cd frontend
   (go to back folder - cd ..)

2. Install Vue.js.
   ```sh
   npm install

3. Start frontend
   ```sh
   npm run dev

## Servers
Django starting on: http://127.0.0.1:8000; 
Vue.js starting on: http://localhost:8000.

#### Created by Denis Dennisov