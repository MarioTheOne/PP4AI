# Lecture 4 local examples

These scripts are the local Python versions of the examples in `notebooks/PP4AI_L4.ipynb`. Run commands from the repository root with the Python interpreter selected in VS Code.

## Search and data structures

```powershell
python L4/search_demo.py
```

The reusable function definitions are in `L4/search_functions.py`; `search_demo.py` imports them and runs the request recap, stack and queue examples, and BFS/DFS checks, including the notebook exercises for starting at `B` and adding a deeper branch.

## LLM example

Install the client in the selected environment:

```powershell
python -m pip install --upgrade google-genai
```

Paste your key on the first line of `secrets/gemini_api_key.txt`. That file is ignored by Git. The script checks `GEMINI_API_KEY` first, then reads the file, and uses a hidden prompt if neither contains a key.

Run the script:

```powershell
python L4/llm_demo.py
```

The script asks for a question and tries the notebook's model list. Keep API keys out of source files and version control.

## Iris classifier

```powershell
python -m pip install scikit-learn pandas matplotlib
python L4/ml_demo.py
```

The script uses scikit-learn's built-in Iris dataset, prints the evaluation and predictions, and opens a window showing the trained decision tree.

## Image detection

```powershell
python -m pip install ultralytics opencv-python matplotlib
python L4/count_people.py
```

The first run downloads the YOLO11 nano weights and needs an internet connection. The script uses `L4/people.jpg` if present; otherwise it uses the example street image from Ultralytics. It displays the detected people and saves the annotated image as `L4/counted_people.jpg`.

## Live webcam

```powershell
python L4/count_people_live.py
```

This uses webcam 0 and shows the current detected person count on each frame. Press `q` while the video window is focused to quit. Camera access requires a local desktop session and may be blocked by operating-system privacy settings.