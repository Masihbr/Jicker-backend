# Jicker-backend
jicker a basic tweer

# Run
```py
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
// if ran to error use
while read requirement; do pip install $requirement || break; done < requirements.txt
// endif
python manage.py migrate
python manage.py runserver
```
