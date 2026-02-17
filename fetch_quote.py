#!/usr/bin/env python3
"""
Script pour extraire une citation aléatoire de l'API whatdoestrumpthink.com
"""

import requests
import json


def get_trump_quote():
    """
    Récupère une citation aléatoire de l'API whatdoestrumpthink.com
    
    Returns:
        dict: Les données de la citation contenant 'quote' et 'tags'
        None: Si la requête échoue
    """
    url = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Lève une exception pour les codes d'erreur
        
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête API: {e}")
        return None


def display_quote(data):
    """
    Affiche la citation de manière lisible
    
    Args:
        data (dict): Les données de la citation
    """
    if data is None:
        print("Impossible de récupérer la citation.")
        return
    
    quote = data.get("message", "Citation non disponible")
    print("\n" + "="*60)
    print("CITATION ALÉATOIRE")
    print("="*60)
    print(f"\n{quote}\n")
    print("="*60 + "\n")


if __name__ == "__main__":
    quote_data = get_trump_quote()
    display_quote(quote_data)
    
    # Afficher les données complètes en JSON si souhaité
    if quote_data:
        print("Données complètes (JSON):")
        print(json.dumps(quote_data, indent=2))
