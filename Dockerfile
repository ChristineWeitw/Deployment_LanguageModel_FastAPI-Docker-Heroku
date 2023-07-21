FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

# Install other project dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app