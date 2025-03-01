# Ram-TroubleshootAI
python3 -m venv venv

source venv/bin/activate

pip freeze > requirements.txt

pip install --upgrade pip

uvicorn main:app --reload

gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
