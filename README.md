# PP4AI
The official repository of the "Programing Principles for AI" course

## Set up Python

Use Python 3.10 or newer. In PowerShell, run these commands from the repository root to create an isolated environment and install the notebook and example dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

In VS Code, select the `.venv` interpreter with **Python: Select Interpreter**. If PowerShell blocks environment activation, select the `.venv` interpreter in VS Code and run the `python -m pip` commands using that interpreter.

The Gemini examples also need a `GEMINI_API_KEY`. The YOLO example downloads its model weights the first time it runs, so that first run needs an internet connection. See [L4/README.md](L4/README.md) for commands to run the local examples.
