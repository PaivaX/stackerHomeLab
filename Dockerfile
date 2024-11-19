# Use uma imagem base do Python
FROM python:3.9-slim

# Setando o diretório de trabalho
WORKDIR /homelab

# Copiar o arquivo de dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar os arquivos do projeto para o container
COPY . .

# Expor a porta que o Django estará rodando
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
