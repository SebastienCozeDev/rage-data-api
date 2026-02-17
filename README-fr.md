# ⚙️ RAGE Data API

![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0-green.svg)

[🇫🇷 Français](README-fr.md) | [🇺🇸 English](README.md)

Ce projet est sous licence Apache 2.0. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📝 Description

RAGE Data API permet d'obtenir certains informations utiles des jeux vidéos utilisant le moteur de jeu RAGE. Ces informations permette, nottament, aux développeurs de mods de simplifier leurs recherches.

## 🐳 Démarrer le projet avec Docker

### 🛠️ En développement

```sh
make init-pre-commit
make build-up
```

### 🚀 En production

```sh
make build-up-d-prod
```

## 🔄 Mises à jour

### 🔄 v0.1.0 — 17 février 2026
- ✅ Ajout de tests unitaires et vérification de leur couverture.

### 🔄 v0.1.0-beta-2 — 13 février 2026
- 👷 Ajout du `docker-compose-prod.yml`, du `docker-compose.dev.yml` et du `Makefile`.
- 👷 Ajout d'une CI utilisant Pylint.
- ✨ Ajout des filtres sur chaque point de terminaison.

### 🔄 v0.1.0-beta-1 — 12 février 2026
- ✨ Mise en place de l'API avec FastAPI.

### 🌱 v0.1.0-alpha.1 — 22 janvier 2026
- 🎉 Initialisation du projet.
