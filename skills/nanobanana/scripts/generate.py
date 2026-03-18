#!/usr/bin/env python3
"""Text-to-image generation using Google's Nano Banana (Gemini) API."""

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
    parser = argparse.ArgumentParser(description="Generate images with Nano Banana (Gemini)")
    parser.add_argument("--prompt", required=True, help="Text prompt for image generation")
    parser.add_argument("--model", default="gemini-3.1-flash-image-preview",
                        help="Model ID (default: gemini-3.1-flash-image-preview)")
    parser.add_argument("--output", default="output.png", help="Output file path (default: output.png)")
    parser.add_argument("--count", type=int, default=1, help="Number of images (1-4, default: 1)")
    parser.add_argument("--aspect-ratio", default=None,
                        choices=["1:1", "3:4", "4:3", "9:16", "16:9"],
                        help="Aspect ratio (default: model default)")
    parser.add_argument("--resolution", default=None,
                        choices=["512", "1k", "2k", "4k"],
                        help="Output resolution (4k requires Pro model)")
    args = parser.parse_args()

    from google.genai import types

    image_config_kwargs = {}
    if args.count > 1:
        image_config_kwargs["number_of_images"] = args.count
    if args.aspect_ratio:
        image_config_kwargs["aspect_ratio"] = args.aspect_ratio
    if args.resolution:
        image_config_kwargs["output_resolution"] = args.resolution

    config_kwargs = {"response_modalities": ["TEXT", "IMAGE"]}
    if image_config_kwargs:
        config_kwargs["image_config"] = types.ImageConfig(**image_config_kwargs)

    client = get_client()
    response = client.models.generate_content(
        model=args.model,
        contents=args.prompt,
        config=types.GenerateContentConfig(**config_kwargs),
    )

    saved = 0
    for i, part in enumerate(response.parts):
        if part.inline_data is not None:
            image = part.as_image()
            if args.count > 1:
                base, ext = os.path.splitext(args.output)
                path = f"{base}_{i}{ext}"
            else:
                path = args.output
            image.save(path)
            print(f"Image saved to {path}")
            saved += 1
        elif part.text:
            print(part.text)

    if saved == 0:
        print("Warning: No image was generated. The prompt may have been filtered or too ambiguous.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
