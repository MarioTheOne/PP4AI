import os
import time
from getpass import getpass
from pathlib import Path

from google import genai
from google.genai import errors, types


MODEL_NAMES = [
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-3.7-flash",
    "gemini-3.8-flash",
]
API_KEY_FILE = Path(__file__).resolve().parents[1] / "secrets" / "gemini_api_key.txt"


def create_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key and API_KEY_FILE.is_file():
        file_key = API_KEY_FILE.read_text(encoding="utf-8").strip()
        if file_key != "PASTE_YOUR_GEMINI_API_KEY_HERE":
            api_key = file_key
    if not api_key:
        api_key = getpass("Gemini API key: ")
    if not api_key:
        raise ValueError("A Gemini API key is required for the live example.")

    os.environ["GEMINI_API_KEY"] = api_key
    return genai.Client(
        http_options=types.HttpOptions(
            timeout=15000,
            retry_options=types.HttpRetryOptions(attempts=1),
        )
    )


def ask_with_fallback(client, prompt, model_names, wait_seconds=2):
    for index, model_name in enumerate(model_names):
        print(f"Trying {model_name}...")
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
            )
            if not response.text:
                print("No text was returned. Inspect the response before retrying.")
                return None
            print(f"Model used: {model_name}")
            return response.text
        except errors.APIError as error:
            print(f"API status {error.code} from {model_name}.")
            if error.code not in (429, 503):
                print("Check the request, model ID, API key, or permissions.")
                return None
            if index < len(model_names) - 1:
                print(f"Waiting {wait_seconds} seconds before trying the next model.")
                time.sleep(wait_seconds)

    print("No model succeeded. Check availability and quota before trying again.")
    return None


def main():
    client = create_client()
    question = input("Your question: ")
    response_format = (
        "The response should be formulated in scientific language "
        "as we are writing a scientific paper."
    )
    prompt = f"{question}\n\n{response_format}"
    response_text = ask_with_fallback(client, prompt, MODEL_NAMES)
    if response_text is not None:
        print(response_text)


if __name__ == "__main__":
    main()