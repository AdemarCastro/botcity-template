# BotCity Automation Template

![alt text](resources/botcity-template.gif)

A professional boilerplate for creating robust automations with [BotCity](https://www.botcity.dev), supporting both **Web** and **Desktop** scenarios. This template leverages:

* **Singleton** `BotManager` for centralized bot web and desktop configuration
* **Environment variables** for flexible browser and headless settings
* **Helpers** for clean `find`, `click`, and `type` operations
* **BotMaestro** integration for task orchestration and reporting

---

## 📦 Project Structure

```
project-root/
├─ config/                  # Project configuration directory
│  └─ constants/
│     └─ enviroment_variables.py   # Loads and validates environment variables from .env
├─ downloads/               # Default download folder (auto-created by the BotManager)
├─ modules/                 # Core automation modules
│  └─ BotManager.py         # Singleton manager for WebBot and DesktopBot instances
├─ resources/               # Desktop vision assets (e.g., button templates .png files)
├─ utils/                   # Utility helper functions
│  └─ helper.py             # Web and desktop helpers (find_and_click, find_and_type, etc.)
├─ .env.example             # Example environment variables file
├─ .gitignore               # Git ignore rules
├─ bot.py                   # Main automation script entry point
├─ build.bat                # Windows batch build script
├─ build.ps1                # Windows PowerShell build script
├─ build.sh                 # Unix shell build script
├─ README.md                # Project documentation (this file)
└─ requirements.txt         # Python dependencies
```

---

## 🔧 Prerequisites

* Python 3.10+ installed
* pip (package manager)
* `.env` file configured (see below)

Install dependencies:

```bash
pip install python-dotenv webdriver-manager botcity-core botcity-web botcity-maestro
```

---

## ⚙️ Configuration

Create a `.env` file in the project root:

```dotenv
# Browser settings: CHROME, FIREFOX, or EDGE
BROWSER=CHROME
# Headless mode: true or false
HEADLESS=False
# Default downloads folder
DOWNLOAD_FOLDER=downloads
# Base URL for web automation (required)
BASE_URL=https://www.botcity.dev
```

All environment variables are loaded and validated by `config/constants/variables.py`.

---

## 🚀 Usage

### 1. Clone the Repository & Navigate
```bash
git clone <REPO_URL>
cd botcity-template
```

### 2. Create & Activate Virtual Environment (Recommended)

Windows
```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Upgrade pip & Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Update Resources

Place any desktop vision assets (e.g., `2_button.png`, `x_button.png`) under `resources/`.

### 5. Configure Environment

Copy the example environment file and customize it:

```bash
cp .env.example .env
```

Edit the .env file as needed (e.g., browser, headless, base URL).

### 6. Run the Automation

```bash
python main.py
```

### 4. Monitor Output

* **Console logs** display task ID, parameters, and step-by-step info.
* **Downloads folder** captures any files saved by the WebBot.

---

## 📝 Code Highlights

### BotManager (`BotManager.py`)

```python
from botcity.web import WebBot, Browser
from botcity.core import DesktopBot
# Singleton pattern for WebBot & DesktopBot
class BotManager:
    @staticmethod
    def get_web_instance(): ...
    @staticmethod
    def get_desktop_instance(): ...
```

### Helpers (`utils/helpers.py`)

```python
def click(bot, selector, label=""): ...
def find_and_click(webbot, selector, text, label=""): ...
```

### Main Script (`bot.py`)

```python
from modules.BotManager import BotManager
from helpers.web_helpers import click, find_and_click

def main():
    desktop = BotManager.get_desktop_instance()
    webbot = BotManager.get_web_instance()
    # Desktop example
    desktop.execute("calc.exe")
    click(desktop, "2_button.png", "Button 2")
    # Web example
    webbot.browse(BASE_URL)
    find_and_click(webbot, "//a[text()='Platform']", "Platform link")
```

---

## 📜 Convenções de Commits

| Tipo       | Descrição                                                                 | Exemplo do Projeto                          |
|------------|---------------------------------------------------------------------------|---------------------------------------------|
| **FEAT**   | Introduz uma nova funcionalidade                                         | `[FEAT] - Adiciona login social com Google` |
| **FIX**    | Corrige um bug ou comportamento indesejado                               | `[FIX] - Corrige loop infinito na paginação`|
| **DOCS**   | Alterações na documentação                                               | `[DOCS] - Atualiza guia de instalação`      |
| **CHORE**  | Mudanças em configurações, scripts ou dependências                       | `[CHORE] - Atualiza versão do Docker Compose` |
| **REFACTOR**| Refatoração de código sem mudar funcionalidades                         | `[REFACTOR] - Simplifica lógica de validação` |
| **BUILD**  | Modificações no sistema de build ou dependências externas                | `[BUILD] - Adiciona pacote de internacionalização` |
| **TEST**   | Adiciona/atualiza testes                                                 | `[TEST] - Cobre cenários de autenticação`   |
| **STYLE**  | Formatação de código, linting ou melhorias de legibilidade               | `[STYLE] - Aplica Prettier nos componentes` |
| **PERF**   | Melhorias de performance                                                 | `[PERF] - Otimiza queries do Prisma`        |
| **CI**     | Mudanças na configuração de CI/CD                                        | `[CI] - Adiciona workflow de deploy na Vercel` |
| **CD**     | Configurações de entrega contínua e deploys automatizados                | `[CD] - Automatiza deploy no Render após merge` |
| **CLEANUP**| Remoção de código morto ou comentários                                   | `[CLEANUP] - Remove componentes obsoletos`  |
| **REMOVE** | Exclusão de arquivos ou funcionalidades                                  | `[REMOVE] - Exclui endpoint não utilizado`  |
| **RAW**    | Mudanças em dados brutos ou configurações específicas                    | `[RAW] - Atualiza dataset de cidades`       |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/xyz`)
3. Commit your changes (`git commit -m "Add new helper"`)
4. Push to branch (`git push origin feature/xyz`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.