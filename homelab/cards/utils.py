# cards/utils.py

import requests
import docker

def get_public_ip_info():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        return {"public_ip": ip_data['ip']}
    except Exception as e:
        return {"error": f"Erro ao acessar IP público: {str(e)}"}

def get_docker_info():
    try:
        client = docker.from_env()  # Cria um cliente Docker conectado ao Docker local
        containers = client.containers.list()  # Lista os containers em execução
        container_info = [{"name": container.name, "status": container.status} for container in containers]
        return {"docker_containers": container_info}
    except Exception as e:
        return {"error": f"Erro ao acessar Docker: {str(e)}"}
