# Teste Prático - Avaliação de Programador Python/Django

## 📌 Sobre o Projeto
Este projeto é um sistema de gerenciamento de leiloeiros e seus respectivos anexos, desenvolvido como parte de um teste prático para avaliar as habilidades de programação em Python com Django.

## 🎯 Objetivos
O sistema permite:
- Cadastro de leiloeiros.
- Autenticação de leiloeiros.
- Upload e gerenciamento de anexos.
- Exibição de anexos apenas para o leiloeiro correspondente.
- Painel administrativo para gestão dos dados (Admin padrão do Django).

## 🚀 Como Executar o Projeto

### 1. Clone o repositório:
```sh
git clone https://github.com/RodrigoMartinsMoraes-Z/TesteLeilao.git
cd TesteLeilao
```

### 2. Crie e ative um ambiente virtual:
```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências:
```sh
pip install -r requirements.txt
```

### 4. Configure o banco de dados:
Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
```sh
SECRET_KEY='sua_chave_secreta'
DEBUG=True
DB_NAME='nome_do_banco'
DB_USER='usuario'
DB_PASSWORD='senha'
DB_HOST='localhost'
DB_PORT='5432'
```

### 5. Execute as migrações:
```sh
python manage.py makemigrations
python manage.py migrate
```

### 6. Crie um superusuário::
```sh
python manage.py createsuperuser
```

### 7. Execute o servidor de desenvolvimento:
```sh
python manage.py runserver
```

8. Acesse a aplicação:
Admin: http://localhost:8000/admin

Sistema: http://localhost:8000


