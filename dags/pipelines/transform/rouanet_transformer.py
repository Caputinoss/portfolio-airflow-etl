import pandas as pd

def limpa_dados_rouanet(df: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "nome", "municipio", "UF", "responsavel", "total_doado",
        "tipo_pessoa", "cgccpf", "_links",
    ]
    df = df[cols]
    df["total_doado"] = pd.to_numeric(df["total_doado"], errors="coerce")

    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df = df.replace("", pd.NA)
    
    return df.dropna(subset=["nome", "cgccpf"])