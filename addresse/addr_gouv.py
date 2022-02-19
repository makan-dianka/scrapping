import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import json 


url = "https://api-adresse.data.gouv.fr/search/"


def get_info_addr(porte, street, name): 
    """_
    cette fonction recupere les info l'addresse saisi, dans l'api des adresses: api-adresse.data.gouv.fr 
    et affiche les informations suivante : nom, ville, code postale et la région de l'addresse saisi
    _

    Args:
        porte (_number_): _numero de la porte_
        street (_string_): _type de rue_
        name (_string_): _nom de rue_
    """
    
    param = {'q' : f'{porte}+{street}+{name}'}
    res = requests.get(url, params=param)
    if res.ok:
        print("\nUrl....... : " + res.url)
        print("StatusCode : " + str(res.status_code))

        cjson = res.json()
        infos_addr = cjson['features'][0]['properties']

        # affichage en forme de table: colonnes et lignes avec la module prettytable
        table = PrettyTable()
        table.field_names = ['NAME', 'CITY', 'CODE POSTAL', 'REGION']
        table.add_rows(
            [
                [
                    infos_addr['name'],  
                    infos_addr['city'], 
                    infos_addr['postcode'], 
                    infos_addr['context'],
                    ],

            ]
            )

        print(table)
    else:
        print("\nStatusCode : " + str(res.status_code))
        
        
print("\n Renseigner les infos de l'addresse pour lancer un requete\n")
PORT = input("PORTE ex (num porte) $ ")
STREET = input("STREET ex (avenue/rue) $ ")
NAME = input("NOM ex (louisville) $ ") 

get_info_addr(PORT, STREET, NAME)