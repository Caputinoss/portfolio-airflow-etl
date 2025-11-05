from airflow.sdk import dag, task
from datetime import datetime
from pipelines.extract.extrai_versalic import get_versalic_data
from pipelines.transform.rouanet_transformer import limpa_dados_rouanet
from pipelines.load.postgres_loader import load_to_postgres, create_gold_table

@dag(schedule="@daily", start_date=datetime(2025, 11, 1), catchup=False, tags=["VERSALIC"])
def etl_versalic_rouanet():

    @task()
    def extract():
        return get_versalic_data().to_dict(orient="records")

    @task()
    def transform(raw):
        import pandas as pd
        df = pd.DataFrame(raw)
        return limpa_dados_rouanet(df).to_dict(orient="records")

    @task()
    def load(dados_rouanet_limpos):
        import pandas as pd
        df = pd.DataFrame(dados_rouanet_limpos)
        load_to_postgres(df)
        create_gold_table()

    raw = extract()
    clean = transform(raw)
    load(clean)

etl_versalic_rouanet_dag = etl_versalic_rouanet()
