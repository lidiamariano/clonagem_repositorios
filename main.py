import os
import subprocess
import requests
import shutil
import time
import stat

# Configurações
repo_urls = '' # Lista de URLs de repositórios para clonar e duplicar.

# Função para tratamento de erro ao remover diretórios.
def onerror(func, path, exc_info):
    """
    Error handler for shutil.rmtree.
    Se um arquivo for somente leitura, esta função altera a permissão para permitir a escrita e tenta novamente a remoção.
    """
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)  # Altera permissão para escrita.
        func(path)  # Tenta remover novamente.
    else:
        raise  # Levanta a exceção original se não for um problema de permissão.

# Função para deletar um diretório.
def delete_folder(folder_path):
    """
    Remove um diretório e todo o seu conteúdo.
    Verifica primeiro se o diretório existe e se é realmente um diretório.
    """
    if not os.path.exists(folder_path):
        print(f"O diretório {folder_path} não existe.")
        return

    if not os.path.isdir(folder_path):
        print(f"{folder_path} não é um diretório.")
        return

    try:
        shutil.rmtree(folder_path, onerror=onerror)  # Remove o diretório.
        print(f"O diretório {folder_path} foi excluído com sucesso.")
    except OSError as e:
        print(f"Erro ao excluir {folder_path}: {e.strerror}")

org_name = 'InteliProjects'  # Nome da organização no GitHub.
github_username = ''
github_token = " "  # Token de acesso do GitHub.

# Função para criar um novo repositório no GitHub dentro de uma organização.
def create_github_repo_in_org(org_name, repo_name, token):
    """
    Cria um repositório na organização especificada no GitHub.
    Faz uma requisição POST à API do GitHub para criar o repositório.
    """
    url = f'https://api.github.com/orgs/{org_name}/repos'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    payload = {'name': repo_name}
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 201:
        print(f"Repositório '{repo_name}' criado com sucesso na organização '{org_name}' no GitHub.")
    else:
        print(f"Erro ao criar o repositório '{repo_name}' na organização '{org_name}' no GitHub: {response.content}")
        exit(1)

# Processamento de cada repositório da lista.
for url in repo_urls:
    repo_name = url.split('/')[-1]
    modified_url = url[:8] + github_username + ':' + github_token + '@' + url[8:]
    
    # Clonando o repositório original.
    subprocess.run(['git', 'clone', modified_url, repo_name])

    new_repo_name = url.split('/')[-2] + '-' + repo_name

    # Criando um novo repositório no GitHub na organização especificada.
    create_github_repo_in_org(org_name, new_repo_name, github_token)

    # Criando um novo repositório local.
    if not os.path.exists(new_repo_name):
        os.mkdir(new_repo_name)
    subprocess.run(['git', '-C', new_repo_name, 'init'])
    subprocess.run(['git', '-C', new_repo_name, 'checkout', '-b', 'main'])

    # Copiando arquivos do repositório clonado para o novo repositório local.
    for item in os.listdir(repo_name):
        if item == '.git':
            continue  # Ignora a pasta .git
        s = os.path.join(repo_name, item)
        d = os.path.join(new_repo_name, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    # Removendo o repositório clonado original após a cópia dos arquivos.
    delete_folder(repo_name)

    # Adicionando e commitando arquivos no novo repositório local.
    subprocess.run(['git', '-C', new_repo_name, 'add', '.'])
    subprocess.run(['git', '-C', new_repo_name, 'commit', '-m', 'Commit inicial'])

    # Configurando a URL do repositório remoto para a organização no GitHub.
    remote_repo_url = f'https://github.com/{org_name}/{new_repo_name}.git'
    subprocess.run(['git', '-C', new_repo_name, 'remote', 'add', 'origin', remote_repo_url])

    # Fazendo o push dos arquivos para o repositório remoto no GitHub.
    subprocess.run(['git', '-C', new_repo_name, 'push', '-u', 'origin', 'main:main'])