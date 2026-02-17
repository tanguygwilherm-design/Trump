# Trump
import requests

def obtenir_citation_aleatoire():
    # L'URL de l'API pour une citation aléatoire
    url = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"
    
    try:
        # Envoi de la requête GET à l'API
        reponse = requests.get(url)
        
        # Vérification que la requête a réussi (code 200)
        reponse.raise_for_status()
        
        # Extraction des données au format JSON
        donnees = reponse.json()
        
        # Affichage de la citation (clé 'message' dans le JSON)
        print("--- Citation Aléatoire ---")
        print(donnees['message'])
        
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à l'API : {e}")

if __name__ == "__main__":
    obtenir_citation_aleatoire()
    