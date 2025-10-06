# README principal
@'
# 🚀 NexusCRM - Modern CRM SaaS Platform

[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://djangoproject.com)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.3-blue.svg)](https://vuejs.org)

**NexusCRM** is a modern, multi-tenant CRM platform built with Django and Vue.js.

## ✨ Features
- 🏢 Multi-tenant Architecture
- 📊 Visual Sales Pipeline  
- 🤖 AI-Powered Insights
- 💰 Stripe Billing
- 📈 Real-time Analytics

## 🚀 Quick Start

```bash
# Backend
cd backend
pip install -r requirements/development.txt
python manage.py migrate
python manage.py runserver
'@ | Out-File -FilePath "README.md" -Encoding utf8

Git ignore
@'

Django
*.pyc
*pycache/
*.pyo
*.pyd
.Python
env/
venv/
.venv/
.env
*.sqlite3
media/
staticfiles/

Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
dist/
build/

IDE
.vscode/
.idea/
*.swp
*.swo

OS
.DS_Store
Thumbs.db

Database
*.db

Logs
*.log

Environment variables
.env.local
.env.development.local
.env.test.local
.env.production.local
'@ | Out-File -FilePath ".gitignore" -Encoding utf8

LICENSE
@'
MIT License

Copyright (c) 2024 NexusCRM

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'@ | Out-File -FilePath "LICENSE" -Encoding utf8

# Fronten

### **2. CONFIGURACIÓN GITHUB ACTIONS**
```powershell
# GitHub CI/CD
@'
name: CI Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test-backend:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:13
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    steps:
    - uses: actions/checkout@v3
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: ''3.11''
    - name: Install dependencies
      run: |
        cd backend
        pip install -r requirements/development.txt
    - name: Run tests
      run: |
        cd backend
        python manage.py test
      env:
        DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
        SECRET_KEY: test-key
'@ | Out-File -FilePath ".github/workflows/ci.yml" -Encoding utf8

# Issue Template
@'
---
name: Bug Report
about: Create a report to help us improve
title: ''[BUG] ''
labels: bug
assignees: ''''

**Describe the Bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to ''...''
2. Click on ''....''
3. Scroll down to ''....''
4. See error

**Expected Behavior**
A clear and concise description of what you expected to happen.

**Environment:**
 - OS: [e.g. Windows, macOS]
 - Browser [e.g. chrome, safari]
'@ | Out-File -FilePath ".github/ISSUE_TEMPLATE/bug_report.md" -Encoding utf8
cd frontend
npm install
npm run dev
