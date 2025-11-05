from pipelines.utils.requisicoes import get_pagina
import pandas as pd
import logging

def get_versalic_data(limit=100, max_pages=5):
    base_url = "https://api.salic.cultura.gov.br/api/v1/incentivadores"

    total_investidores = get_pagina(f"{base_url}?limit=1&offset=1")
    logging.info(f"=========== Total de investidores: {total_investidores.json().get("total", {})} ===========")

    all_data = []
    for page in range(max_pages):
        offset = page * limit
        resp = get_pagina(f"{base_url}?limit={limit}&offset={offset}")
        logging.info(f"============================ Acessando página {base_url}?limit={limit}&offset={offset} ============================")
        resp.raise_for_status()
        investidores = resp.json().get("_embedded", {}).get("incentivadores", [])
        all_data.extend(investidores)
    return pd.DataFrame(all_data)
