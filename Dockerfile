# Container base: python 3.7
FROM python:3.7

ENV PYTHONUNBUFFERED 1

# Cria diretório onde vão ficar os fontes
RUN mkdir /src

# Define o diretório de trabalho
WORKDIR /src

# "Copia" arquivo requirements.txt para o diretorio src
ADD requirements.txt /src/

# Executa o pip
RUN pip install -r requirements.txt

# Copia os arquivos locais para o diretorio src no container 
ADD . /src/        