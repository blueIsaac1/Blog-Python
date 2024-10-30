import pytest
from tortoise import Tortoise, fields
from tortoise.models import Model
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Definindo um modelo de exemplo
class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50)

# Configuração do Tortoise ORM
@pytest.fixture(scope="module", autouse=True)
async def setup_database():
    print("Inicializando o Tortoise ORM...")
    # Verificando se a variável de ambiente DATABASE_URL está definida
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        raise ValueError("A variável de ambiente DATABASE_URL não está definida.")
    
    # Inicializando o Tortoise ORM
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["__main__"]}  # Substitua "__main__" pelo seu módulo de modelos
    )
    await Tortoise.generate_schemas()
    print("Banco de dados inicializado.")

    yield  # Permite que os testes sejam executados

    # Fechando a conexão após os testes
    await Tortoise.close_connections()
    print("Conexões fechadas.")

@pytest.mark.asyncio
async def test_create_user():
    print("Testando a criação de um usuário...")
    # Criando um novo usuário
    user = await User.create(username="testuser")
    
    # Verificando se o usuário foi criado
    assert user.id is not None
    assert user.username == "testuser"
    print("Usuário criado com sucesso:", user.username)

@pytest.mark.asyncio
async def test_read_user():
    print("Testando a leitura de um usuário...")
    # Lendo o usuário que foi criado
    user = await User.get(username="testuser")
    
    # Verificando se o usuário foi lido corretamente
    assert user.id is not None
    assert user.username == "testuser"
    print("Usuário lido com sucesso:", user.username)