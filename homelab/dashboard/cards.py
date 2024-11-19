import requests
import socket
import docker
from django.shortcuts import render
from django.http import JsonResponse
from psutil import cpu_percent, virtual_memory

# Função para obter o IP público
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json().get('ip')
    except requests.exceptions.RequestException:
        return "Não foi possível obter o IP público"

# Função para obter dados do Uptime Kuma API
def get_uptime_kuma_data():
    # Exemplo de URL da API do Uptime Kuma (modifique conforme necessário)
    url = "http://uptimekuma_api_url/api/health"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        return "Não foi possível conectar ao Uptime Kuma"

# Função para monitorizar o Docker
# Função para obter dados do Docker
def get_docker_info():
    try:
        client = docker.from_env()
        containers = client.containers.list()
        containers_info = []
        for container in containers:
            containers_info.append({
                'id': container.id,
                'name': container.name,
                'status': container.status
            })
        return containers_info
    except Exception as e:
        return None

# Função para obter os dados do servidor (CPU e Memória)
def get_server_info():
    cpu_usage = cpu_percent(interval=1)
    memory = virtual_memory()
    return {"cpu_usage": cpu_usage, "memory_total": memory.total, "memory_available": memory.available}

def dashboards(request):
    public_ip = get_public_ip()
    uptime_kuma_data = get_uptime_kuma_data()
    docker_info = get_docker_info()
    server_info = get_server_info()

    context = {
        'public_ip': public_ip,
        'uptime_kuma_data': uptime_kuma_data,
        'docker_info': docker_info,
        'server_info': server_info,
    }

    return render(request, 'dashboard/tools_dashboard.html', context)

