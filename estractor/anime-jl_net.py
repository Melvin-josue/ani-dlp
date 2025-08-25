# Importar modulos necesarios
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, unquote

# funcion para obtener todos lo links de la pagina


def get_links(a):

    # definimos cabeceras
    head = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}

    links = []  # lista donde se guardaran los links

    code = requests.get(a, headers=head)  # peticion

    if code.status_code == 200:  # verificacion si es un codigo esperado

        html = BeautifulSoup(code.text, "html.parser")  # obtencion de el html

        # links hacia los animes
        exe = html.find_all("a", {"class": "Button Sm fa-download"})

        for lk in exe:  # iterador de las urls

            # parsea para sacar solo lo que esta despues de &url=
            parsed = urlparse(lk["href"])

            # obtencion de urls como diccionario
            params = parse_qs(parsed.query)

            # obtener los links de los host
            final_host = params.get("url", lk["href"])[0]

            if final_host:
                limpios = final_host.replace(" ", "")  # limpiar espacios
                links.append(limpios)  # guardar los links
        print(links)


# ====================== main =========================================
if __name__ == "__main__":
    get_links(
        "https://anime-jl.net/anime/1981/call-of-the-night-season-2/episodio-8")
