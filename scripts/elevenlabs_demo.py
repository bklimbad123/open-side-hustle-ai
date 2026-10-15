import os
from pathlib import Path

import requests


def main() -> None:
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise SystemExit("Set ELEVENLABS_API_KEY to run this demo.")

    voice_id = os.getenv("ELEVENLABS_VOICE_ID", "JBFqnCBsd6RMkjVDRZzb")
    response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        headers={"xi-api-key": api_key, "Content-Type": "application/json"},
        json={
            "text": "Your latest receipt was processed by ReceiptLens.",
            "model_id": "eleven_multilingual_v2",
        },
        timeout=60,
    )
    response.raise_for_status()
    Path("sample_summary.mp3").write_bytes(response.content)
    print("Wrote sample_summary.mp3")


if __name__ == "__main__":
    main()