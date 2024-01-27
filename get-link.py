import requests
from os import system as pip
from time import sleep

try:
    from user_agent import generate_user_agent
except:
    pip('pip install user_agent')
    from user_agent import generate_user_agent
try:
    from bs4 import BeautifulSoup
except:
    pip('pip install beautifulsoup4')
    pip('pip install html5lib')
    from bs4 import BeautifulSoup

preboyx = ("""
#---------------------------------------------------------------
#######                                      
#     # ###### ##### #       # #    # #    # 
#       #        #   #       # ##   # #   #  
#  #### #####    #   #       # # #  # ####   
#     # #        #   #       # #  # # #  #   
#     # #        #   #       # #   ## #   #  
 #####  ######   #   ####### # #    # #    #

#---------------------------------------------------------------
BY: @PreBoyx  •  @Juan_hack_v5
#---------------------------------------------------------------
""")
print('\033[1;32;40m' + preboyx)  # Imprime en verde
url = input('\033[1;32;40m[~] Ingresa el enlace del sitio: ')  # Imprime en verde

r = requests.get(url, headers={'user_agent': generate_user_agent()})
if r.status_code == 200:
    print('\033[1;32;40m[•] Extrayendo enlaces ..\n')  # Imprime en verde
    x = BeautifulSoup(r.text, 'html.parser')
    cc = list(x.find_all('a'))
    for i in cc:
        try:
            line = str(i['href']).replace(' ', '').replace('#', '')
            if line == '' or line == ' ' or line == '#' or line == '/':
                pass
            else:
                print('\033[1;32;40m[🜸] ' + line)  # Imprime en verde
                file = open('links.txt', 'a').write(f'{line}\n')
        except:
            pass
else:
    print('\033[1;31;40m[!] Url del sitio web incorrecto, inténtalo de nuevo')  # Imprime en rojo
    sleep(3)
    quit()
