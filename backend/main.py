from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# On charge un modèle d'IA gratuit (Zero-Shot Classification)
# Ce modèle est capable de classer du texte dans des catégories qu'on choisit
print("Chargement de l'IA en cours...")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
print("IA prête !")

@app.get("/")
def home():
    return {"message": "Serveur IA Gaz et Électricité opérationnel"}

@app.get("/analyser")
def analyser_demande(texte: str):
    # On définit les catégories que l'IA doit reconnaître
    labels_possibles = ["souscription électricité", "souscription gaz", "résiliation", "facture"]
    
    # L'IA analyse le texte envoyé
    resultat = classifier(texte, candidate_labels=labels_possibles)
    
    # On renvoie le résultat propre
    return {
        "demande_client": texte,
        "categorie": resultat['labels'][0],
        "confiance": f"{round(resultat['scores'][0] * 100, 2)}%"
    }