# Lab 1 — Build and Secure a CI/CD Pipeline

This repository is the participant starter project for the Cloud Threat Modeling training.

## Learning objectives
By completing this lab you will:
1. Create a Git repository for an application.
2. Run automated tests in GitHub Actions.
3. Store a configuration value as a GitHub Actions secret.
4. Run SAST with Bandit.
5. Scan Python dependencies with pip-audit.
6. Scan the Git repository for hardcoded secrets with Gitleaks.
7. Build a release artifact.
8. Experience a failing security gate, fix the issue, and obtain a clean pipeline.

## Important
This is a training application. Do not place real passwords, API keys, cloud credentials, or other secrets in this repository.

## Project layout

```text
cloud-threat-modeling-lab1/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   └── app.py
├── tests/
│   └── test_app.py
├── requirements.txt
└── README.md
```

## Run locally

Python 3.10+ is recommended.

```bash
python -m venv .venv
```

Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
python -m pip install -r requirements.txt
```

Run tests:
```bash
python -m pytest -q
```

Run the application:
```bash
python -m app.app
```

Open:
```text
http://127.0.0.1:5000/
```

Health endpoint:
```text
http://127.0.0.1:5000/health
```

## Security tools locally

SAST:
```bash
python -m pip install bandit
bandit -r app
```

Dependency audit:
```bash
python -m pip install pip-audit
pip-audit -r requirements.txt
```

The CI workflow is intentionally more complete than the local setup because it also includes secret scanning and artifact creation.
