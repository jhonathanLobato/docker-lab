FROM python:3.13-slim

WORKDIR app/

RUN python -m venv venv

COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["python", "main.py"]