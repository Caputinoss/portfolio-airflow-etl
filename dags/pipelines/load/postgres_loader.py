import sqlalchemy

def load_to_postgres(df, table_name="projetos_clean"):
    engine = sqlalchemy.create_engine(f"postgresql+psycopg2://caputo:teste123@postgres_dados:5432/postgres")

    df.to_sql(
        table_name, 
        engine, 
        schema="silver", 
        if_exists="replace", 
        index=False,
        dtype={"_links": sqlalchemy.types.JSON},
    )
    print(f"✅ {len(df)} registros carregados em silver.{table_name}")

def create_gold_table():
    query = """
    CREATE SCHEMA IF NOT EXISTS gold;
    DROP TABLE IF EXISTS gold.investimento_por_uf;
    CREATE TABLE gold.investimento_por_uf AS
        SELECT 
            "UF",
            COUNT(*) AS total_investidores,
            SUM(total_doado) AS total_doado
        FROM silver.projetos_clean
        GROUP BY "UF";
    """
    engine = sqlalchemy.create_engine(f"postgresql+psycopg2://caputo:teste123@postgres_dados:5432/postgres")
    with engine.begin() as conn:
        conn.execute(query)
