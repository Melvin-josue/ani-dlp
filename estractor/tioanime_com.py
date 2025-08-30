import requests
from bs4 import BeautifulSoup

def geting_link(a):
    
    head = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0"}
    
    res = requests.get(a, headers=head)
    
    if res.status_code == 200:
        html = BeautifulSoup(res.text, "html.parser")
        
        btn = html.find(class_="btn btn-success btn-download btn-sm rounded-pill")
        
        print(btn["href"])
    else:
        return None

if __name__ == "__main__":
    url = "https://tioanime.com/ver/mizu-zokusei-no-mahoutsukai-8"
    geting_link(url)