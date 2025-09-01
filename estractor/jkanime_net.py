# modulos para parsear el html
from bs4 import BeautifulSoup
import json
import re
import base64
from pprint import pprint 

# modulos que hice y usare
from main.main_class import GetHtmlBot

def geting_links(url):

    clase = GetHtmlBot() # instacia de la clase

    link = clase.Obten(url) # metodo de la clase

    soup = BeautifulSoup(link, "html.parser")

    scripts = soup.find_all("script")
    servers_data = None

    for script in scripts:
        if script.string and 'var servers' in script.string:
            match = re.search(r'var servers\s*=\s*(\[.*?\]);', script.string, re.DOTALL)
            if match:
                json_data = match.group(1)
                servers_data = json.loads(json_data)
                break

    for server in servers_data:
        remote_encode = server["remote"]
        try:
            remote_decode = base64.b64decode(remote_encode).decode("utf-8")
            server["remote_decode"] = remote_decode
        except:
            server["remote_decode"] = "error decodificando"
    pprint(servers_data)


