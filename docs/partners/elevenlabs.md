# ElevenLabs

ElevenLabs can turn a short extraction result into an optional spoken summary.
The demo in `scripts/elevenlabs_demo.py` calls the text-to-speech API only when
`ELEVENLABS_API_KEY` is set and writes `sample_summary.mp3` locally.

The demo uses a generic sentence, not receipt contents. A production feature
should request consent before transmitting financial details and keep the key
in environment-based secret storage.