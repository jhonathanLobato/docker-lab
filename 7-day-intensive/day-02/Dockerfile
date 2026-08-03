# sempre pense em camadas
# layer 1 - sistema operaciona
# layer 2 - linguagem do projeto (no caso, o python)
# layer 3 - dependencias
# layer 4 - código
# layer 5 - comando para inicializar

# layer - sistema operacional
FROM python:3.13-slim

# definindo o ambiente de trabalho
WORKDIR app/

RUN python -m venv app/venv

COPY requirements.txt .

# layer - dependencias
RUN pip install --no-cache -r requirements.txt

# layer - codigo
COPY . .

# layer - comando para iniciar
CMD ["python", "main.py"]

