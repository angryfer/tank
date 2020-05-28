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
            except Exception as e :
                print(i)


def add_ammo_fields(AMMO_PATH):
    with open(AMMO_PATH,'w+') as file:
        for i in SYMBOLS:
            url = "/hub0/upstream/symlistfeed/fields/reuters?symbol={}".format(i)
            ammo2 = "GET {} HTTP/1.0\nHost: {}\nUser-Agent: xxx (shell 1)\r\n\r\n\r\n".format(url,host)
            ammo = "{}\n{}".format(len(ammo2),ammo2)
            file.write(ammo)
            
            url_p = "/hub0/upstream/symlistfeed/batchfields/reuters?fields=*"
            symb = '["{}"]'.format(i)
            ammo2 = "POST {} HTTP/1.0\nHost: {}\nUser-Agent: xxx (shell 1)\nContent-Type: application/json\nContent-Length: {}\r\n\r\n{}\r\n\r\n\r\n".format(url_p, host,len(symb),symb )
            ammo = "{}\n{}".format(len(ammo2),ammo2)
            file.write(ammo)





if __name__ == '__main__':
    parse_file(PATH)
    print(len(SYMBOLS))
    add_ammo_fields(AMMO_PATH)
