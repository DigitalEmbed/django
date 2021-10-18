# Container base: python 3.7
FROM python:3.7

ENV PYTHONUNBUFFERED 1

# Cria diretório onde vão ficar os fontes
RUN mkdir /code
RUN mkdir /databank

# Define o diretório de trabalho
WORKDIR /code

# Copia arquivo requirements.txt para o diretorio code
ADD requirements.txt /code/

# Executa o pip
RUN pip install -r requirements.txt

# Copia os arquivos locais para o diretorio code no container 
ADD . /code/

# Inicializa os comandos iniciais do Docker
CMD ./entrypoint.sh