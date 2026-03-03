# ⚙️ RAGE Data API

![Version](https://img.shields.io/badge/version-0.1.2-blue.svg)
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

## 🎯 Roadmap

| Feature                                           | Status          |
|---------------------------------------------------|-----------------|
| Add important GTA5 data                           | ✅ Done        |
| Add all GTA5 data                                 | 🔄 In progress |
| Replace JSON files with PostgreSQL                | ⏳ Planned     |
| JWT Authentication                                | ⏳ Planned     |
| User roles                                        | ⏳ Planned     |
| JSON file import for administrators               | ⏳ Planned     |
| CRUD operations for all models (administrators)   | ⏳ Planned     |
| User modification/creation requests               | ⏳ Planned     |
| Markdown page creation                            | ⏳ Planned     |

## 🔄 Updates

### 🔄 v0.1.2 — March 4, 2026
- ✨ Implemented read operations for filtered game controls
- 📝 Added the Health tag documentation.

### 🔄 v0.1.1 — March 3, 2026
- 📝 Added the roadmap to the README files.

### 🔄 v0.1.0 — February 17, 2026
- ✅ Added unit tests and verified its coverage.

### 🔄 v0.1.0-beta-2 — February 13, 2026
- 👷 Added `docker-compose-prod.yml`, `docker-compose.dev.yml` and `Makefile`.
- 👷 Added a CI using Pylint.
- ✨ Added filters on each endpoint.

### 🔄 v0.1.0-beta-1 — February 12, 2026
- ✨ Implemented the API with FastAPI.

### 🌱 v0.1.0-alpha.1 — January 22, 2026
- 🎉 Project initialization.
