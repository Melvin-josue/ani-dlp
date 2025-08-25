
# Modulos a usar para extraer los datos necesarios
# import requests
from curl_cffi import requests
import base64
from bs4 import BeautifulSoup

# Funcion para sacar la url escondida en base64 de mediafire


def get_link(url):
    # cabeceras para evitar bloqueos anti-bots basicos
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}

    # variable que guarda el codigo html y el codigo de respuesta
    code = requests.get(url, headers=head, impersonate="chrome")

    if code.status_code == 200:  # verificacion para saber si la peticion fue aceptada

        # obtener el html decodificado
        html = BeautifulSoup(code.text, 'html.parser')

        # obtener la url en base64
        scrambled_url = html.find("a", {"data-scrambled-url": True})

        # la url en base64 lista para decodificar
        base64_scrambled = scrambled_url["data-scrambled-url"]

        # decodificacion de la url a bytes
        base64_decode_url = base64.b64decode(base64_scrambled)

        # decodificacion de la url a codificacion utf-8 legible para humanos
        base64_url_utf = base64_decode_url.decode("utf-8")

        return base64_url_utf  # devolvemos la url decodificada


# main para la ejecucuion
if __name__ == "__main__":
    url = "https://www.mediafire.com/file/vrqt9dg7as92s4i/Gachiakuta-06.720p.AnimeYT.es.mp4/file"  # url de entrada
    get_link(url)  # funcion para recibir la url
