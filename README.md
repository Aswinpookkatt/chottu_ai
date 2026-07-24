# Chottu_AI
Chottu AI is a lightweight, CLI-based assistant designed to help you write scripts, debug commands, and automate daily terminal tasks without breaking your flow.

Prerequisites

Before running the project, make sure you have the following installed:

* Python 3.12 or later
* Git
* Ollama

Verify your installations:

python3 --version
git --version
ollama --version

⸻

1. Clone the Repository

git clone https://github.com/<your-username>/ai-terminal-agent.git
cd ai-terminal-agent

⸻

2. Create a Virtual Environment

macOS/Linux

python3 -m venv .venv
source .venv/bin/activate

Windows (PowerShell)

python -m venv .venv
.venv\Scripts\Activate.ps1

⸻

3. Install Dependencies

pip install -r requirements.txt

If requirements.txt is not available yet:

pip install openai pydantic rich typer python-dotenv

⸻

4. Install Ollama

Follow the official installation instructions for your operating system:

https://ollama.com/download

⸻

5. Download a Model

Example:

ollama pull qwen3:8b

Or use another supported model:

ollama pull qwen2.5:7b

Check installed models:

ollama list

⸻

6. Start Ollama

Normally Ollama starts automatically after installation.

To verify it’s running:

ollama ps

If no models are running, that’s okay—the model will start automatically on first use.

⸻

7. Configure the Model

Open config.py and ensure the model name matches the one you downloaded.

Example:

model = "qwen3:8b"

or

model = "qwen2.5:7b"

⸻

8. Run the Application

python main.py

You should see an interactive prompt:

You >

Example:

You > list all python files

The agent will propose a terminal command, ask for confirmation, execute it (if approved), and display the results.

⸻

Project Structure

ai-terminal-agent/
│
├── agent/
│   └── controller.py
│
├── llm/
│   └── client.py
│
├── models/
│   └── schemas.py
│
├── tools/
│   └── terminal.py
│
├── main.py
├── config.py
├── prompts.py
└── README.md

⸻

Troubleshooting

ModuleNotFoundError

Ensure your virtual environment is activated:

source .venv/bin/activate

Then reinstall dependencies:

pip install -r requirements.txt

⸻

Cannot connect to Ollama

Verify Ollama is installed and accessible:

ollama list

If the command is not found, install Ollama from:

https://ollama.com/download

⸻

Model not found

Download the required model:

ollama pull qwen3:8b

Then update config.py with the correct model name.

⸻


