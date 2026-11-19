import os
import time

from google import genai
from google.genai import errors, types

MODEL_NAME = "gemini-3.8-flash"


def generate_text(prompt: str) -> str:
    """Generate text with retries for temporary Gemini server errors."""

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable is missing.")

    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(
            timeout=20000,
            retry_options=types.HttpRetryOptions(attempts=1),
        ),
    )

    try:
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt,
                )

                if not response.text:
                    raise RuntimeError("Gemini returned an empty response.")

                return response.text.strip()

            except errors.ServerError as exc:
                if exc.code != 503 or attempt == 2:
                    raise

                delay = 2 ** (attempt + 1)
                print(
                    f"Gemini temporarily unavailable. "
                    f"Retrying in {delay} seconds "
                    f"(attempt {attempt + 2}/3)."
                )
                time.sleep(delay)

        raise RuntimeError("Gemini failed after three attempts.")

    finally:
        client.close()
