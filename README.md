# base10
"A ideia é fornecer uma base ampla de questões do ENEM como uma api REST"

### TODO

* Documentar a api com [apifairy](https://apifairy.readthedocs.io/en/latest/)
* Criar testes
* Criar crawler para sites com questões do enem
* Implementar métodos POST, PUT e DELETE de questions
* Criar bucket pára armazenamento de imagens
* Dockerizar a parada e subir uma imagem no docker hub

### 🐑 Clonar e rodar ⚙️

```
git clone https://github.com/wadsongarbes/base10 api-base10
```
Pronto, agora que clonou, acesse o diretório 
```
cd api-base10
```
Crie e ative um ambiente virtual com o seguinte comando (Mac ou Linux):
```
python3 -m venv env && source env/bin/activate
```
Instale as dependências do projeto
```
pip install -r requirements.txt
```
Crie o banco de dados local (SQLite) e popule-o com as questões existentes
```
flask db init && flask db migrate && flask db upgrade && flask integrate
```
Rode o server
```
flask run
```

## API Endpoints

|  URL | Métodos | Descrição |
| -------- | ------------- | --------- |
| `/api/v1/questions/<int:id>` | GET | Visualizar questão por ID|
| `/api/v1/questions` | GET | Ver todas as questões |


## Construído com

* [Flask](https://flask.palletsprojects.com/en/2.1.x/) - Framework utilizado

## Dúvidas ?

Tire suas dúvidas na seção "Issues".

* [Dúvidas](https://github.com/WadsonGarbes/base10/issues)
