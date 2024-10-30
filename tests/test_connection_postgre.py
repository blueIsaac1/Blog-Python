import asyncio
import asyncpg
import os

async def test_connection():
    # Substitua os valores abaixo pelos seus dados de conexão
    username = 'postgres'
    password = 'ctdev'
    database = 'blog-python'
    host = 'localhost'
    port = '5432'
    db_url=os.environ.get("DATABASE_URL")

    try:
        # Estabelecendo a conexão
        conn = await asyncpg.connect(dsn=db_url)
        print("Conexão bem-sucedida ao PostgreSQL!")

        # Executando uma consulta simples
        rows = await conn.fetch('SELECT version();')
        print("Versão do PostgreSQL:", rows[0]['version'])

    except Exception as e:
        print("Erro ao conectar ao PostgreSQL:", e)

    finally:
        # Fechando a conexão
        if 'conn' in locals():
            await conn.close()

# Executando a função de teste
if __name__ == '__main__':
    asyncio.run(test_connection())