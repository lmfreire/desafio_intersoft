# desafio_intersoft

Rotas

## Produto
### Get
```
  baseUrl/api/produtos/
```
### Post
```
baseUrl/api/produtos/
  {
  	"nome": "Produto Teste",
  	"valor": 100,
  	"quantidade": 50	
  }
```
### Update
```
baseUrl/api/produtos/:idProduto/
  {
  	"nome": "Produto Teste",
  	"valor": 100,
  	"quantidade": 50	
  }
```
### Delete
```
baseUrl/api/produtos/:idProduto/
```

## Cliente
### Get
```
  baseUrl/api/clientes/
```
### Post
```
baseUrl/api/clientes/
  {
  	"nome": "",
  	"telefone": "",
  	"cpf": "",
  	"endereco": {
  		"cidade": "",
  		"uf": "",
  		"rua": "",
  		"numero": 
  	}
  	
  }
```
### Update
```
baseUrl/api/clientes/:idCliente/
  {
  	"nome": "",
  	"telefone": "",
  	"cpf": "",
  	"endereco": {
  		"cidade": "",
  		"uf": "",
  		"rua": "",
  		"numero": 
  	}
  	
  }
```
### Delete
```
baseUrl/api/clientes/:idCliente/
```

## Venda
### Get
```
  baseUrl/api/vendas/
```
### Post
```
baseUrl/api/vendas/
{
	"data": "2023-08-02",
	"quantidade": 2,
	"produto": "31c970fd-e586-4ff6-b1e4-812a73ce31f3",
	"cliente": "6f32599e-18b6-4825-b871-126476bba2b7"
}
```
### Update
```
baseUrl/api/vendas/:idVenda/
{
	"data": "2023-08-02",
	"quantidade": 2,
	"produto": "31c970fd-e586-4ff6-b1e4-812a73ce31f3",
	"cliente": "6f32599e-18b6-4825-b871-126476bba2b7"
}
```
### Delete
```
baseUrl/api/vendas/:idVenda/
```
