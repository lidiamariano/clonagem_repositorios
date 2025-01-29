# 🚀 Guia de Uso do Script de Clonagem de Repositórios GitHub | Escritório de Projetos - Inteli

Este script tem como objetivo clonar repositórios existentes e recriá-los dentro de uma organização no GitHub. Ele realiza as seguintes etapas:

1. Clona um repositório existente.
2. Cria um novo repositório dentro de uma organização no GitHub.
3. Copia os arquivos do repositório clonado para o novo repositório.
4. Faz commit e push dos arquivos para o novo repositório.

---

## ✅ Requisitos

Antes de utilizar o script, é necessário:
- Ter o **Git** instalado na máquina.
- Uma conta no **GitHub** com permissões para criar repositórios na organização desejada.
- Criar um [Personal Access Token (PAT)](https://github.com/settings/tokens) no GitHub com permissões de repositório.

---

## ⚙️ Configuração

Edite as seguintes variáveis no código antes de executá-lo:

```python
repo_urls = ''  # Lista de URLs dos repositórios a serem clonados e duplicados.
```
🔹 **Substitua** `''` por uma **lista de URLs** dos repositórios a serem clonados. Exemplo:

```python
repo_urls = ['https://github.com/usuario/repositorio1', 'https://github.com/usuario/repositorio2']
```

```python
github_username = ''  # Nome de usuário do GitHub.
```
🔹 **Substitua** `''` pelo **seu nome de usuário do GitHub**. Exemplo:

```python
github_username = 'seu_usuario'
```

```python
github_token = " "  # Token de acesso do GitHub.
```
🔹 **Substitua** `" "` pelo **seu Personal Access Token**. Exemplo:

```python
github_token = "ghp_xxxSeuTokenAqui"
```

```python
org_name = 'InteliProjects'  # Nome da organização no GitHub.
```
🔹 **Substitua** `'InteliProjects'` pelo **nome da organização** onde os repositórios serão criados.

---

## ▶️ Execução do Script

Após configurar as variáveis corretamente, execute o script com o Python:

```sh
python nome_do_script.py
```

### Durante a execução, o script:
✅ Clona os repositórios listados em `repo_urls`.
✅ Cria um novo repositório na organização `org_name`.
✅ Copia os arquivos do repositório clonado para o novo repositório.
✅ Faz commit e push dos arquivos para o novo repositório no GitHub.

---

## ⚠️ Possíveis Erros e Soluções

### 🔴 Erro de autenticação no GitHub
- Verifique se o `github_token` está correto e possui permissões adequadas.

### 🔴 Erro ao criar repositório na organização
- Confirme se você tem permissões para criar repositórios na organização `org_name`.
- Verifique se o nome do repositório já existe.

### 🔴 Erro ao excluir diretório
- O script altera permissões automaticamente para evitar esse problema. Se persistir, tente deletar manualmente o diretório clonado.

---


