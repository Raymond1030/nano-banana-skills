# Nano Banana Skills

Generate and edit images using Google's Nano Banana (Gemini) API as a Claude Code skill.

## Installation

### Via Claude Code Marketplace

Add this repository URL to your `extraKnownMarketplaces` in Claude Code settings:

```json
{
  "extraKnownMarketplaces": [
    "https://github.com/Raymond1030/nano-banana-skills"
  ]
}
```

### Manual Installation

Clone this repo and add it as a skill source in your Claude Code configuration.

## Setup

1. Install Python dependencies:

```bash
pip install google-genai Pillow
```

2. Set your API key as an environment variable:

```bash
export GOOGLE_API_KEY="your-api-key-here"
# or
export GEMINI_API_KEY="your-api-key-here"
```

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

## Available Models

| Model | ID | Best For | Max Resolution |
|-------|-----|----------|---------------|
| Nano Banana 2 | `gemini-3.1-flash-image-preview` | Fast, high-quality (default) | 1K |
| Nano Banana Pro | `gemini-3-pro-image-preview` | Pro-grade, complex prompts | 4K |
| Nano Banana | `gemini-2.5-flash-image` | Speed, high-volume | 1K |

## CLI Usage

The scripts can also be used standalone:

```bash
# Generate an image
python skills/nanobanana/scripts/generate.py --prompt "a banana on a beach" --output banana.png

# Edit an image
python skills/nanobanana/scripts/edit.py --input banana.png --prompt "add sunglasses" --output cool_banana.png

# Multi-turn refinement
python skills/nanobanana/scripts/chat.py --prompt "a banana character" --refinement "make it more cartoon-like" --refinement "add a cape"
```

## License

MIT
