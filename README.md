# Online-Judge-using-django
Code submission and evaluation plaform that remotely, securely runs the user code and judges if the given code is correct/wrong/inefficient. Uses Docker for isolation to provide security and scalability.

# Getting Started

1. Make sure you have python and docker installed on your machine.
2. Setup and start virtual environment. If you don't have python3, replace with python.

 ```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies and migrate

```
pip install -r requirements.txt
python manage.py migrate
```

4. Run server and open localhost:8000 in a browser

```
python manage.py runserver
```
