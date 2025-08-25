# importacion de modulos necesarios
import requests
import html
import json
from bs4 import BeautifulSoup

# funcion para obtener los links


def get_link(a):

    # headers para saltar mini anti-bots
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}

    code = requests.get(a, headers=head)  # peticion

    if code.status_code == 200:

        html = BeautifulSoup(code.text, "html.parser")  # codigo html

        server = html.find("a", {"data-dwn": True})  # obtencion de los servers

        jo = server["data-dwn"]  # carga de la data en formato json

        servers = json.loads(jo)  # transformacion de la data en formato python

        url = [item[2] for item in servers]  # obtencion de las urls
        
        return url


# =========== Main ===========
if __name__ == "__main__":
    urls = get_link("https://wwv.veranimes.net/ver/dandadan-2nd-season-8")
    
    print(urls)
