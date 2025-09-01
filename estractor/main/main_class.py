# importar modulos para trabajar
import httpx # para peticiones http
import cloudscraper # para paginas con cloudflare
from typing import Optional # para manejo de opciones de datos

HEADERS = {'USER-AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0'} # headers para saltar algo de antibots

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

if __name__ == '__main__':
    # Crear un objeto de la clase
    url = "https://jkanime.net/gachiakuta/8/"
    get_html_bot = GetHtmlBot()
    lk = get_html_bot.Obten(url)
    print(lk)