# API-FLASK
Exemplo simples de uma api que insere em um banco postgresql grande quantidade de dados.

## Exemplo de utilização:

crie um script python para gerar um json.

```python
import json

data = [
    {"field1": f"value1_{i}", "field2": f"value2_{i}"}
    for i in range(15000)
]

with open('data.json', 'w') as f:
    json.dump(data, f) 
```

Vá até a pasta onde está o json gerado e utilize o comando:

```bash
curl -X POST http://localhost:5000/upload -H "Content-Type: application/json" -H "Authorization: q5a7x87s6gfdvs929x" -d @data.json
```
O Console deverá ter a seguinte saida:

```bash
{
  "message": "Data inserted successfully"
}
```
