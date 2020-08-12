# API Medicar

- python3.7.5
- django3.0.3
- djangorestframework3.11.0

## Como rodar a API localmente

### Clonando o projeto 
```sh
git clone https://github.com/LucasGabrielSI/desafio-medicar-intmed.git
````
### Criando e ativando uma env
```sh
python -m venv <nome_da_env>
source <nome_da_env>/bin/activate
````
### Instalando as dependencias
```sh
pip install -r requirements.txt
````
### Configuração do banco
```sh
Após configurar um novo banco no seu cliente de postgressql, adicione as seguintes informações em database no arquivo settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<nome do banco>',
        'USER': '<usuario>',
        'PASSWORD': '<senha>',
        'HOST': '<endereco_onde_o_projeto_esta_rodando>',
        'PORT': '<porta>',
    }
}
```` 
### Rodando Migrates
```sh
python manage.py migrate
````
### Criando um superusuário
```sh
python manage.py createsuperuser
````
### Rodando a aplicação 
```sh
python manage.py runserver
````
