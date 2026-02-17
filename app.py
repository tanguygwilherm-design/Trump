#!/usr/bin/env python3
"""
Application web pour afficher les citations de Trump
"""

from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_trump_quote():
    """Récupère une citation aléatoire"""
    url = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("message", "Citation non disponible")
    except requests.exceptions.RequestException as e:
        return f"Erreur: {e}"


@app.route('/')
def index():
    """Page d'accueil avec une citation"""
    quote = get_trump_quote()
    return render_template('index.html', quote=quote)


@app.route('/random')
def random_quote():
    """Récupère une nouvelle citation"""
    quote = get_trump_quote()
    return render_template('index.html', quote=quote)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
