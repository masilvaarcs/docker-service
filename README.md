# Docker_Service

## Descrição

O Docker_Service é um serviço Dockerizado que permite consultar os dados de endereço a partir de um CEP fornecido. Ele utiliza a API da VIACEP para obter informações precisas e atualizadas sobre o CEP consultado.

## Requisitos

Antes de executar o Docker_Service, certifique-se de ter o seguinte instalado em sua máquina:

- Docker

## Como usar

1. Clone este repositório para sua máquina local.

2. Navegue até a pasta do projeto Docker_Service.

3. Construa o container Docker com o seguinte comando:

```bash
docker build -t Docker_Service .
```

4. Execute o container com o seguinte comando:

```bash
docker run -d -p 5000:5000 Docker_Service
```

5. O serviço estará em execução na porta 5000. Agora você pode enviar requisições para a API do serviço para consultar os dados do endereço usando um CEP.

## API

### Endpoint

```
GET /cep/{cep}
```

### Parâmetros

- `{cep}`: O CEP que você deseja consultar.

### Resposta

A resposta será um JSON contendo os dados do endereço associado ao CEP consultado, ou uma mensagem de erro caso o CEP não seja encontrado.

Exemplo de resposta bem-sucedida:

```json
{
    "cep": "01234-567",
    "logradouro": "Rua Exemplo",
    "bairro": "Bairro Teste",
    "localidade": "Cidade",
    "uf": "SP"
}
```

Exemplo de resposta de erro:

```json
{
    "message": "CEP not found"
}
```

## Contribuição

Se você encontrar algum problema ou tiver alguma sugestão de melhoria, sinta-se à vontade para abrir uma "Issue" neste repositório. Contribuições através de "Pull Requests" também são bem-vindas!

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
