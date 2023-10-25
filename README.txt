Le but du projet est de créer une API accédant à une base de données SQLite, ainsi qu’un script permettant de récupérer les données de l’API.

La base de données utilisée sera Chinook : https://www.sqlitetutorial.net/sqlite-sample-database/.


Le script devra demander à l’utilisateur :

un nom d’artiste, et afficher les artistes comprenant le nom donné,
un identifiant d’artiste, et afficher les noms d’albums correspondants,
un identifiant d’album, et afficher les noms de pistes correspondants.
Ce script peut récupérer les données de l’utilisateur avec la fonction input ou le module argparse. Il doit être utilisable simplement.

L’API doit proposer des routes qui correspondent aux fonctionnalités du script.

l'on peut acceder au projet via le terminal de commande en : 
1. En entrant dans l'environnement env via la commande : env\Scripts\activate.bat 
2. Une fois dans l'environnement , saisir : uvicorn server:app --reload pour recharger le serveur
4. Pour interroger le fichier client saisir python client.python
5. Une fois dans le fichier client , l'utilisateur devra repondre à la question posée pour afficher les reponses correspondantes.

