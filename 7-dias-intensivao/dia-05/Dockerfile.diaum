# Aqui eu estou definindo a imagem base
FROM python:3.13
# Apenas alguns metadados para identificação
LABEL autor="Jhonathan Lobato" versao="1.0"

# Aqui eu estou definindo onde vai ser o local de trabalho
WORKDIR /app

# Como definimos o /app como raiz do projeto, temos que colocar
# a venv nesse diretório
RUN python -m venv /app/venv

# O mais importante, devo copiar o arquivo requirements.txt
# e devo instalar a biblioteca do flask
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Deixando claro qual porta deve ser aberta para a comunicação
EXPOSE 5000

CMD ["python", "main.py"]