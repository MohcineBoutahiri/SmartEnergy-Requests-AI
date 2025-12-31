# Smart HIRE — Recrutement automatisé par IA générative 👥🤖

Smart HIRE est une solution de recrutement **augmentée par l’IA générative** qui automatise les tâches les plus chronophages du cycle RH : **création d’offres**, **analyse de CV**, **matching candidat ↔ poste**, **préparation d’entretiens**, et **pilotage via tableaux de bord**.

L’objectif : **réduire le time-to-hire**, améliorer la **qualité des shortlists**, renforcer l’**objectivité** de la sélection et offrir une meilleure **expérience candidat** — tout en gardant le recruteur au centre des décisions (*human-in-the-loop*).

---

## ✨ Fonctionnalités clés

- **Génération d’offres d’emploi** (JD) à partir de quelques critères (poste, seniorité, compétences, contexte)
- **Parsing & compréhension sémantique des CV** (PDF/DOC/LinkedIn) : extraction automatique des infos clés
- **Matching intelligent** et **classement** des candidats (scoring multi-critères)
- **Explicabilité** du score (compétences présentes/manquantes, adéquation expérience/poste)
- **Génération de questions d’entretien** personnalisées (techniques & comportementales)
- **Orchestration du workflow RH** : suivi, statuts, feedback, historique des décisions
- *(Optionnel)* **Chatbot RH** pour assister recruteurs et managers (FAQ, recommandations, recherche)

---

## 🧠 Approche IA

Smart HIRE combine :
- **NLP & embeddings** pour comprendre le sens des CV et des fiches de poste (au-delà des mots-clés)
- **Modèles de ranking / scoring** pour prioriser les candidatures
- **IA générative** pour produire des contenus RH (offres, emails, questions d’entretien) avec garde-fous

---

## 🔒 Conformité & éthique

Le projet intègre des mécanismes de contrôle pour un usage responsable :
- **Human-in-the-loop** : validation finale par les recruteurs
- **Anonymisation** possible de champs sensibles
- **Traçabilité** des décisions et des scores
- Respect des exigences **RGPD** (gestion des données personnelles, conservation, accès)

---

## 📈 KPI suivis

- Time-to-hire / Time-to-shortlist
- Taux de candidatures qualifiées
- Taux de conversion (candidature → entretien → offre)
- Satisfaction candidats & recruteurs
- Qualité des recrutements (suivi à 3/6/12 mois)

---

## 🚀 Démarrage rapide (exemple)

1. Créer une fiche de poste (titre, compétences, niveau, localisation)
2. Importer un lot de CV
3. Générer la shortlist et analyser les raisons du classement
4. Préparer les entretiens via questions personnalisées
5. Suivre le pipeline et consolider les feedbacks

---

## 🗂️ Structure du projet (suggestion)

- `docs/` : documentation fonctionnelle & technique
- `data/` : jeux de données (anonymisés) & exemples
- `src/` : logique métier, pipeline IA, API
- `ui/` : interface recruteur (dashboard)
- `tests/` : tests unitaires & d’intégration

---

## 🤝 Contribution

Les contributions sont les bienvenues : amélioration du pipeline, ajout de connecteurs (ATS/CRM), enrichissement des métriques, audits d’équité, etc.
Merci de proposer une issue ou une PR avec une description claire et des tests associés.

---

## 📄 Licence

À définir (MIT / Apache-2.0 / Propriétaire).
