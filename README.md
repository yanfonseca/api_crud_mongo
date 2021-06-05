# API 

CRUD no banco Mongo usando Sanic

## Como desenvolver
1. Clone o repositório
1. Crie um virtualenv com Python 3.5 ou superior.
1. Ative o virtualenv
1. Instale as dependências
1. Baixe mongo no docker hub

```console
git clone https://github.com/yanfonseca/api_crud_mongo.git
cd api_crud_mongo
python -m venv .myenv
source .myenv/bin/activate
pip install -r requirements.txt
docker pull mongo
sudo docker run -p 27018:27017 -d mongo
```

## Abrir o projeto
```console
python run.py
```

