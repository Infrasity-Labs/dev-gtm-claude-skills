#!/usr/bin/env python3
"""
Blog Audio Generator - Gemini TTS
Converts prepared text to speech using Google's Gemini TTS models.

Usage:
    python scripts/run.py generate_audio.py --text "Hello world" --voice Charon --json
    python scripts/run.py generate_audio.py --text-file article.txt --voice Puck --voice2 Kore --json
    python scripts/run.py generate_audio.py --text "Test" --dry-run --json
"""

import argparse
import base64
import json
import os
import shutil
import subprocess
import sys
import struct
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

# All 30 Gemini TTS prebuilt voices
VOICES = {
    "Zephyr": "Bright", "Puck": "Upbeat", "Charon": "Informative",
    "Kore": "Firm", "Fenrir": "Excitable", "Leda": "Youthful",
    "Orus": "Firm", "Aoede": "Breezy", "Callirrhoe": "Easy-going",
    "Autonoe": "Bright", "Enceladus": "Breathy", "Iapetus": "Clear",
    "Umbriel": "Easy-going", "Algieba": "Smooth", "Despina": "Smooth",
    "Erinome": "Clear", "Algenib": "Gravelly", "Rasalgethi": "Informative",
    "Laomedeia": "Upbeat", "Achernar": "Soft", "Alnilam": "Firm",
    "Schedar": "Even", "Gacrux": "Mature", "Pulcherrima": "Forward",
    "Achird": "Friendly", "Zubenelgenubi": "Casual", "Vindemiatrix": "Gentle",
    "Sadachbia": "Lively", "Sadaltager": "Knowledgeable", "Sulafat": "Warm",
}

MODELS = {
    "flash": "gemini-2.5-flash-preview-tts",
    "pro": "gemini-2.5-pro-preview-tts",
}

# Audio constants (Gemini TTS output format)
SAMPLE_RATE = 24000  # 24kHz
SAMPLE_WIDTH = 2     # 16-bit (2 bytes per sample)
CHANNELS = 1         # Mono

# Cost per 1M tokens (output)
COST_PER_1M_OUTPUT = {"flash": 10.0, "pro": 20.0}
COST_PER_1M_INPUT = {"flash": 0.50, "pro": 1.0}


def estimate_cost(text: str, model: str) -> dict:
    """Estimate generation cost from text length."""
    char_count = len(text)
    input_tokens = char_count / 4  # rough: 1 token ~ 4 chars
    # Output tokens scale with audio duration; ~150 words/min speech
    word_count = len(text.split())
    duration_minutes = word_count / 150
    duration_seconds = duration_minutes * 60
    # Rough output token estimate based on audio duration
    output_tokens = duration_seconds * 200  # ~200 tokens per second of audio

    input_cost = (input_tokens / 1_000_000) * COST_PER_1M_INPUT[model]
    output_cost = (output_tokens / 1_000_000) * COST_PER_1M_OUTPUT[model]
    total_cost = input_cost + output_cost

    return {
        "input_tokens_est": int(input_tokens),
        "output_tokens_est": int(output_tokens),
        "duration_seconds_est": int(duration_seconds),
        "duration_human_est": f"{int(duration_minutes)}:{int(duration_seconds % 60):02d}",
        "cost_estimate": f"${total_cost:.3f}",
    }


def pcm_to_wav(pcm_data: bytes, output_path: str):
    """Write raw PCM data as a WAV file."""
    num_samples = len(pcm_data) // SAMPLE_WIDTH
    data_size = num_samples * SAMPLE_WIDTH * CHANNELS
    byte_rate = SAMPLE_RATE * CHANNELS * SAMPLE_WIDTH
    block_align = CHANNELS * SAMPLE_WIDTH

    with open(output_path, "wb") as f:
        # RIFF header
        f.write(b"RIFF")
        f.write(struct.pack("<I", 36 + data_size))
        f.write(b"WAVE")
        # fmt chunk
        f.write(b"fmt ")
        f.write(struct.pack("<I", 16))            # chunk size
        f.write(struct.pack("<H", 1))             # PCM format
        f.write(struct.pack("<H", CHANNELS))
        f.write(struct.pack("<I", SAMPLE_RATE))
        f.write(struct.pack("<I", byte_rate))
        f.write(struct.pack("<H", block_align))
        f.write(struct.pack("<H", SAMPLE_WIDTH * 8))
        # data chunk
        f.write(b"data")
        f.write(struct.pack("<I", data_size))
        f.write(pcm_data)


def wav_to_mp3(wav_path: str, mp3_path: str) -> bool:
    """Convert WAV to MP3 using FFmpeg. Returns True on success."""
    if not shutil.which("ffmpeg"):
        return False
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", wav_path, "-codec:a", "libmp3lame",
             "-b:a", "192k", "-ar", "24000", "-ac", "1", mp3_path],
            check=True, capture_output=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def extract_audio_data(response) -> bytes:
    """Extract raw PCM audio bytes from Gemini TTS response.
    The SDK returns inline_data.data as bytes (raw PCM), not base64."""
    data = response.candidates[0].content.parts[0].inline_data.data
    if isinstance(data, bytes):
        return data
    # Fallback: if it's a base64 string (older SDK versions)
    return base64.b64decode(data)


def generate_single_speaker(client, text: str, voice: str, model: str) -> bytes:
    """Generate audio with a single voice."""
    from google.genai import types

    response = client.models.generate_content(
        model=MODELS[model],
        contents=text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=voice
                    )
                )
            ),
        ),
    )
    return extract_audio_data(response)


def generate_multi_speaker(client, text: str, voice1: str, voice2: str, model: str) -> bytes:
    """Generate audio with two speakers (dialogue mode)."""
    from google.genai import types

    response = client.models.generate_content(
        model=MODELS[model],
        contents=text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                    speaker_voice_configs=[
                        types.SpeakerVoiceConfig(
                            speaker="Speaker1",
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name=voice1
                                )
                            ),
                        ),
                        types.SpeakerVoiceConfig(
                            speaker="Speaker2",
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name=voice2
                                )
                            ),
                        ),
                    ]
                )
            ),
        ),
    )
    return extract_audio_data(response)


def output_result(data: dict, as_json: bool):
    """Print result in JSON or human-readable format."""
    if as_json:
        print(json.dumps(data, indent=2))
    else:
        if data["status"] == "success":
            print(f"\n{'=' * 50}")
            print(f"  Audio generated successfully!")
            print(f"{'=' * 50}")
            print(f"  File:     {data['path']}")
            print(f"  Format:   {data['format']}")
            print(f"  Duration: {data['duration_human']}")
            print(f"  Voice:    {data['voice']}")
            print(f"  Model:    {data['model']}")
            print(f"  Cost:     ~{data['cost_estimate']}")
            print(f"\n  Embed HTML:")
            print(f"  {data['embed_html']}")
            print(f"{'=' * 50}\n")
        elif data["status"] == "dry_run":
            print(f"\n  Dry run estimate:")
            print(f"  Duration: ~{data['duration_human_est']}")
            print(f"  Cost:     ~{data['cost_estimate']}")
            print(f"  Model:    {data['model']}")
            print(f"  Voice:    {data['voice']}")
        else:
            print(f"\n  Error: {data.get('error', 'Unknown error')}")


def main():
    parser = argparse.ArgumentParser(description="Generate audio from text using Gemini TTS")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="Text to convert to speech")
    group.add_argument("--text-file", help="Path to text file")

    parser.add_argument("--voice", default="Charon", help="Primary voice (default: Charon)")
    parser.add_argument("--voice2", help="Second voice for dialogue mode")
    parser.add_argument("--model", choices=["flash", "pro"], default="flash", help="TTS model")
    parser.add_argument("--output", help="Output file path (default: auto-generated)")
    parser.add_argument("--json", action="store_true", help="Output structured JSON")
    parser.add_argument("--dry-run", action="store_true", help="Estimate cost without generating")

    args = parser.parse_args()

    # Validate voice names
    for voice_arg in [args.voice, args.voice2]:
        if voice_arg and voice_arg not in VOICES:
            result = {"status": "error", "error": f"Unknown voice: {voice_arg}. Valid voices: {', '.join(sorted(VOICES.keys()))}"}
            output_result(result, args.json)
            return 1

    # Read text
    if args.text_file:
        text_path = Path(args.text_file)
        if not text_path.exists():
            result = {"status": "error", "error": f"Text file not found: {args.text_file}"}
            output_result(result, args.json)
            return 1
        text = text_path.read_text(encoding="utf-8").strip()
    else:
        text = args.text.strip()

    if not text:
        result = {"status": "error", "error": "Empty text provided"}
        output_result(result, args.json)
        return 1

    # Dry run - estimate only
    if args.dry_run:
        est = estimate_cost(text, args.model)
        result = {
            "status": "dry_run",
            "model": args.model,
            "voice": args.voice,
            "voice2": args.voice2,
            "text_length": len(text),
            "word_count": len(text.split()),
            **est,
        }
        output_result(result, args.json)
        return 0

    # Check API key
    api_key = os.environ.get("GOOGLE_AI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        result = {"status": "error", "error": "GOOGLE_AI_API_KEY not set. Get one at https://aistudio.google.com/apikey"}
        output_result(result, args.json)
        return 1

    # Generate audio
    try:
        from google import genai
        client = genai.Client(api_key=api_key)

        if not args.json:
            print(f"Generating audio ({args.model} model, voice: {args.voice})...")

        if args.voice2:
            pcm_data = generate_multi_speaker(client, text, args.voice, args.voice2, args.model)
        else:
            pcm_data = generate_single_speaker(client, text, args.voice, args.model)

    except Exception as e:
        result = {"status": "error", "error": f"Gemini TTS API error: {str(e)}"}
        output_result(result, args.json)
        return 1

    # Calculate duration
    num_samples = len(pcm_data) // SAMPLE_WIDTH
    duration_seconds = num_samples / SAMPLE_RATE
    duration_min = int(duration_seconds // 60)
    duration_sec = int(duration_seconds % 60)
    duration_human = f"{duration_min}:{duration_sec:02d}"

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = Path.cwd() / f"audio_{ts}.mp3"

    # Write WAV, then convert to MP3
    wav_path = str(output_path.with_suffix(".wav"))
    pcm_to_wav(pcm_data, wav_path)

    final_format = "wav"
    final_path = wav_path

    if output_path.suffix.lower() in (".mp3", ""):
        mp3_path = str(output_path.with_suffix(".mp3"))
        if wav_to_mp3(wav_path, mp3_path):
            os.unlink(wav_path)  # Remove temp WAV
            final_path = mp3_path
            final_format = "mp3"
        else:
            if not args.json:
                print("  Warning: FFmpeg not found. Output is WAV (install ffmpeg for MP3).")
            final_path = wav_path
            final_format = "wav"
    elif output_path.suffix.lower() == ".wav":
        final_path = wav_path
        final_format = "wav"

    # Build embed HTML
    rel_path = Path(final_path).name
    mime = "audio/mpeg" if final_format == "mp3" else "audio/wav"
    embed_html = (
        f'<audio controls preload="metadata">'
        f'<source src="{rel_path}" type="{mime}">'
        f'Your browser does not support the audio element.</audio>'
    )

    # Cost estimate
    est = estimate_cost(text, args.model)

    result = {
        "status": "success",
        "path": str(Path(final_path).resolve()),
        "format": final_format,
        "duration_seconds": int(duration_seconds),
        "duration_human": duration_human,
        "voice": args.voice,
        "voice2": args.voice2,
        "model": args.model,
        "embed_html": embed_html,
        "cost_estimate": est["cost_estimate"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    output_result(result, args.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
