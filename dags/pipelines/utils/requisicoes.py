import requests
import logging
import time
from requests.exceptions import RequestException

def get_pagina(url, tentativas=3, timeout=10):

    for tentativa in range(1, tentativas + 1):
        try:
            response = requests.get(url=url, timeout=timeout)
            response.raise_for_status()
            return response
        except RequestException as e:
            logging.error(f"Tentativa {tentativa}/{tentativas} falhou: {e}")
            logging.error('. . .')
            time.sleep(3 ** tentativa)
    return None