import requests
import json



PATH = 'symbols.txt'
AMMO_PATH = 'ammo.txt'
SYMBOLS = []
FIELDS=['ebitda','industry']
host='hub01.xtools.tv'


def parse_file(path):
    with open(path,'r') as file:
        file = file.read()
        obj = file.split('\n')
        for i in obj:
            try:
                i=json.loads(i)
                SYMBOLS.append(i['exchange-listed']+':'+i['symbol'])
            except json.decoder.JSONDecodeError as e :
                print(i)


def add_ammo_fields(AMMO_PATH):
    with open(AMMO_PATH,'w+') as file:
        for i in SYMBOLS:
            url = f"/hub0/upstream/symlistfeed/fields/reuters?symbol={i}"
            ammo2 = f"GET {url} HTTP/1.0\nHost: {host}\nUser-Agent: xxx (shell 1)\r\n\r\n\r\n"
            ammo = f"{len(ammo2)}\n{ammo2}"
            file.write(ammo)
            
            url_p = f"/hub0/upstream/symlistfeed/batchfields/reuters?fields=*"
            symb = f'["{i}"]'
            ammo2 = f"POST {url_p} HTTP/1.0\nHost: {host}\nUser-Agent: xxx (shell 1)\nContent-Type: application/json\nContent-Length: {len(symb)}\r\n\r\n{symb}\r\n\r\n\r\n"
            ammo = f"{len(ammo2)}\n{ammo2}"
            file.write(ammo)





if __name__ == '__main__':
    parse_file(PATH)
    print(len(SYMBOLS))
    add_ammo_fields(AMMO_PATH)
