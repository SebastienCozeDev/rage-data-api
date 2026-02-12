# ⚙️ RAGE Data API

![Version](https://img.shields.io/badge/version-0.1.0--beta.2-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0-green.svg)

[🇫🇷 Français](README-fr.md) | [🇺🇸 English](README.md)

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more details.

## 📝 Description

RAGE Data API allows you to retrieve useful information from video games using the RAGE game engine. This information helps, in particular, mod developers to simplify their research.

## 🐳 Run with Docker

### 🛠️ In development mode

```sh
make init-pre-commit
make build-up
```

### 🚀 In production mode

```sh
make build-up-d-prod
```

## 🔄 Updates

### 🔄 v0.1.0-beta-2
- 👷 Added `docker-compose-prod.yml`, `docker-compose.dev.yml` and `Makefile`.
- 👷 Added a CI using Pylint.
- ✨ Added filters on each endpoint.

### 🔄 v0.1.0-beta-1 — February 12, 2026
- ✨ Implemented the API with FastAPI.

### 🌱 v0.1.0-alpha.1 — January 22, 2026
- 🎉 Project initialization.
