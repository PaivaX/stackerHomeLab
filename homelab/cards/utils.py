# cards/utils.py

import psutil
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

def get_server_resources():
    try:
        # Informações sobre CPU
        cpu_count = psutil.cpu_count(logical=True)  # Número de CPUs lógicas
        cpu_usage = psutil.cpu_percent(interval=1)  # Uso da CPU em porcentagem (com intervalo de 1 segundo)
        
        # Informações sobre memória
        memory = psutil.virtual_memory()
        total_memory = memory.total  # Memória total
        used_memory = memory.used   # Memória usada
        memory_percentage = memory.percent  # Uso de memória em porcentagem
        
        # Informações sobre armazenamento
        disk = psutil.disk_usage('/')
        total_disk = disk.total  # Espaço total do disco
        used_disk = disk.used    # Espaço usado do disco
        disk_percentage = disk.percent  # Uso do disco em porcentagem

        # Retornar todas as informações
        return {
            "cpu": {
                "logical_cores": cpu_count,
                "usage_percent": cpu_usage,
            },
            "memory": {
                "total": total_memory,
                "used": used_memory,
                "usage_percent": memory_percentage,
            },
            "disk": {
                "total": total_disk,
                "used": used_disk,
                "usage_percent": disk_percentage,
            }
        }
    except Exception as e:
        return {"error": f"Erro ao acessar recursos do servidor: {str(e)}"}
