# Container base: python 3.7
FROM python:3.7

ENV PYTHONUNBUFFERED 1

# Cria diretório onde vão ficar os fontes
RUN mkdir /code

# Define o diretório de trabalho
WORKDIR /code

# "Copia" arquivo requirements.txt para o diretorio code
ADD requirements.txt /code/

# Atualiza e executa o pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia os arquivos locais para o diretorio code no container 
COPY . /code/

# Executando as migrações do banco de dados
RUN python manage.py makemigrations
RUN python manage.py migrate

# Remove as permissões de administrador da pasta
RUN sudo chown -R $USER:$USER .