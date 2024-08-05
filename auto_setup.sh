# Create and activate venv
python3 -m venv venv
source venv/bin/activate

# Go to backend folder
cd backend/simpleproject

# Install requirements
pip install -r requirements.txt

# Use migrate and start backend
python manage.py migrate
python manage.py runserver

# go to frontend folder
cd ..
cd ..
cd frontend

# Install vue
npm install

# Start frontend
npm run dev