import os
import asyncio
import asyncpg
from dotenv import load_dotenv

load_dotenv()

async def list_tables_and_data():
    # Conectar ao banco de dados
    conn = await asyncpg.connect(os.environ.get("DATABASE_URL"))
    
    # Listar tabelas
    tables = await conn.fetch("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    
    for table in tables:
        table_name = table['table_name']
        print(f"Tabela: {table_name}")
        
        # Listar dados da tabela
        data = await conn.fetch(f"SELECT * FROM {table_name};")
        for row in data:
            print(dict(row))
        print("\n")  # Adiciona uma linha em branco entre as tabelas

    # Fechar a conexão
    await conn.close()

if __name__ == "__main__":
    asyncio.run(list_tables_and_data())