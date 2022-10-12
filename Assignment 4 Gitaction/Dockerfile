# Eny
FROM python:3.9

# Workdirectory
WORKDIR /code

# Dependencies
COPY ./requirements.txt /code/requirements.txt

# install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# App file
COPY ./app /code/app

# Running command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
