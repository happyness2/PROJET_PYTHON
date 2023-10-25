import requests
import json

#Client saisir le nom de l'artiste
name=input("Entrer le nom de l'artiste svp: ")
url="http://127.0.0.1:8000/read_artist/?artist_name="+name

reponse=requests.get(url)
 # Charger le JSON (si ce n'est pas déjà un objet Python)
data = json.loads(reponse.text)

 # Ici json.dumps() est utilisé  pour formater le JSON de manière lisible
formatted_json = json.dumps(data, indent=4, sort_keys=True)

print(formatted_json)

#utilisateur saisir un identifiant d’artiste
saisir_artist=input("Saisir l'identifiant de l'artiste svp: ")
url="http://127.0.0.1:8000/read_albums/{album_name}?artist_id="+saisir_artist

reponse=requests.get(url)

 # Charger le JSON (si ce n'est pas déjà un objet Python)
data = json.loads(reponse.text)

 # Ici json.dumps() est utilisé  pour formater le JSON de manière lisible
formatted_json = json.dumps(data, indent=4, sort_keys=True)
print(formatted_json)

#afficher les noms de pistes correspondants
saisir_albums=input("Saisir l'identifiant de l'artiste svp: ")
url="http://127.0.0.1:8000/read_tracks/{tracks_name}?album_id="+saisir_albums
reponse=requests.get(url)
 # Charger le JSON (si ce n'est pas déjà un objet Python)
data = json.loads(reponse.text)
 # Ici json.dumps() est utilisé  pour formater le JSON de manière lisible
formatted_json = json.dumps(data, indent=4, sort_keys=True)
print(formatted_json)



       
        

        