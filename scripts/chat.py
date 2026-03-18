#!/usr/bin/env python3
"""Multi-turn chat image generation using Google's Nano Banana (Gemini) API."""

import argparse
import os
import sys


def get_client():
    api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: Set GOOGLE_API_KEY or GEMINI_API_KEY environment variable.", file=sys.stderr)
        sys.exit(1)
    from google import genai
    return genai.Client(api_key=api_key)


def save_images(response, prefix, iteration):
    saved = 0
    for i, part in enumerate(response.parts):
        if part.inline_data is not None:
            image = part.as_image()
            path = f"{prefix}_iter{iteration}_{i}.png" if i > 0 else f"{prefix}_iter{iteration}.png"
            image.save(path)
            print(f"Image saved to {path}")
            saved += 1
        elif part.text:
            print(part.text)
    return saved


def main():
    parser = argparse.ArgumentParser(description="Multi-turn chat image generation with Nano Banana (Gemini)")
    parser.add_argument("--prompt", required=True, help="Initial prompt")
    parser.add_argument("--model", default="gemini-3.1-flash-image-preview",
                        help="Model ID (default: gemini-3.1-flash-image-preview)")
    parser.add_argument("--output-prefix", default="chat_output",
                        help="Output file prefix (default: chat_output)")
    parser.add_argument("--refinement", action="append", default=[],
                        help="Refinement prompt(s), can be specified multiple times")
    args = parser.parse_args()

    from google.genai import types

    client = get_client()
    chat = client.chats.create(
        model=args.model,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
        ),
    )

    # Initial generation
    print(f"--- Iteration 1: {args.prompt}")
    response = chat.send_message(args.prompt)
    total = save_images(response, args.output_prefix, 1)

    # Refinements
    for idx, refinement in enumerate(args.refinement, start=2):
        print(f"\n--- Iteration {idx}: {refinement}")
        response = chat.send_message(refinement)
        total += save_images(response, args.output_prefix, idx)

    if total == 0:
        print("Warning: No images were generated.", file=sys.stderr)
        sys.exit(1)

    print(f"\nTotal images generated: {total}")


if __name__ == "__main__":
    main()
