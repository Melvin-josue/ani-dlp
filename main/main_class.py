# importar modulos para trabajar
from http.client import responses

import httpx # para peticiones http
import cloudscraper # para paginas con cloudflare
from typing import Optional # para manejo de opciones de datos

HEADERS = {'ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     'ACCEPT-ENCODING': 'gzip, deflate, br, zstd',
    'ACCEPT-LANGUAGE': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'SEC-FETCH-DEST': 'document',
    'SEC-FETCH-MODE': 'navigate',
    'SEC-FETCH-SITE': 'cross-site',
    'SEC-FETCH-USER': '?1',
    'SEC-GPC': '1',
    'UPGRADE-INSECURE-REQUESTS': '1',
    'USER-AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0'} # headers para saltar algo de antibots

class GetHtml:
    """ Obtiene html de paginas que no tienen fuerte los antibots"""
    def Obten(self, url: str) -> Optional[httpx.Response]:
        try:
            response = httpx.get(url, headers=HEADERS, timeout=10)
            print(response.status_code)
            return response.text if response.status_code == 200 else None
        except (httpx.RequestError, httpx.TimeoutException):
            return None


class GetHtmlBot:
    """Obtiene el html de paginas que tiene cloudflare"""
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()

    def Obten(self, url: str):
        try:
            response = self.scraper.get(url, headers=HEADERS, timeout=30)
            print(response.status_code)
            return response.text if response.status_code == 200 else None
        except Exception:
            return None
