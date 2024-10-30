# API de Gerenciamento de Postagens

Este projeto é uma API para gerenciar postagens, desenvolvida com FastAPI e Tortoise ORM. A API permite criar, listar e obter postagens, com suporte a diferentes estados de postagens (publicado e rascunho).

## Tecnologias Utilizadas

- **FastAPI**: Um framework moderno e rápido para construir APIs com Python 3.6+ baseado em padrões como OpenAPI.
- **Tortoise ORM**: Um ORM asyncio inspirado no Django, que facilita a interação com bancos de dados.
- **Pydantic**: Para validação de dados e criação de modelos de dados.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional utilizado para armazenar os dados.

## Estrutura do Projeto

```
.
├── adapter
│   ├── post.py
│   └── schemas
│       └── post.py
├── domain
│   ├── entities
│   │   └── post.py
│   └── service
│       └── post.py
├── port
│   ├── factory
│   │   └── post.py
│   └── fastapi
│       ├── application.py
│       ├── configurations.py
│       └── router
│           └── post.py
├── tests
│   ├── test_connection_postgre.py
│   └── test_connection_tortoise.py
└── .env
```

## Instalação

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente no arquivo `.env`:
   ```env
   DATABASE_URL=postgres://<USUARIO>:<SENHA>@localhost:5432/<NOME_DO_BANCO>
   ```

## Uso

Para iniciar a aplicação, execute o seguinte comando:

```bash
uvicorn port.fastapi.application:core_module --reload
```

A API estará disponível em `http://127.0.0.0:3000`.

## Endpoints

- `GET /posts`: Lista todas as postagens.
- `POST /posts`: Cria uma nova postagem.
- `GET /posts/{post_id}`: Obtém uma postagem específica pelo ID.

## Testes

O projeto inclui testes para verificar a conexão com o banco de dados e a funcionalidade da API. Para executar os testes, você pode usar o seguinte comando:

```bash
pytest
```

### Testes de Conexão

- **test_connection_postgre.py**: Testa a conexão com o banco de dados PostgreSQL.
- **test_connection_tortoise.py**: Testa a configuração do Tortoise ORM e a criação de um modelo de exemplo.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.