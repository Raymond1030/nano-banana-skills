#!/usr/bin/env python3
"""Image editing using Google's Nano Banana (Gemini) API."""

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


def main():
    parser = argparse.ArgumentParser(description="Edit images with Nano Banana (Gemini)")
    parser.add_argument("--input", required=True, help="Input image path")
    parser.add_argument("--prompt", required=True, help="Edit instruction")
    parser.add_argument("--model", default="gemini-3.1-flash-image-preview",
                        help="Model ID (default: gemini-3.1-flash-image-preview)")
    parser.add_argument("--output", default="edited.png", help="Output file path (default: edited.png)")
    args = parser.parse_args()

    from PIL import Image
    from google.genai import types

    if not os.path.exists(args.input):
        print(f"Error: Input image not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    image = Image.open(args.input)
    client = get_client()

    response = client.models.generate_content(
        model=args.model,
        contents=[args.prompt, image],
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
        ),
    )

    saved = False
    for part in response.parts:
        if part.inline_data is not None:
            result = part.as_image()
            result.save(args.output)
            print(f"Edited image saved to {args.output}")
            saved = True
        elif part.text:
            print(part.text)

    if not saved:
        print("Warning: No image was generated. Try rephrasing the edit instruction.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
