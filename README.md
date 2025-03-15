# Ram-TroubleshootAI
python3 -m venv venv

source venv/bin/activate

pip freeze > requirements.txt

pip install --upgrade pip

uvicorn main:app --reload

gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker

pip install -e .


# Install NumPy
python -m pip install -U numpy

# Install SciPy
python -m pip install -U scipy

# Install pandas
python -m pip install -U pandas
clear