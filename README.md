# Nano Banana Skills

Generate and edit images using Google's Nano Banana (Gemini) API as AI agent skills.

## Getting Started

```bash
# 1. Create skills directory (if it doesn't exist)
mkdir -p ~/.claude/skills

# 2. Clone this repository
cd ~/.claude/skills
git clone https://github.com/Raymond1030/nano-banana-skills nanobanana

# 3. That's it! Open Claude Code and say:
"generate an image of a banana on a beach"
```

### Other AI Tools

| Tool | Command |
|------|---------|
| Cursor | `git clone https://github.com/Raymond1030/nano-banana-skills ~/.cursor/skills/nanobanana` |
| Codex | `git clone https://github.com/Raymond1030/nano-banana-skills ~/.codex/skills/nanobanana` |
| Gemini CLI | `git clone https://github.com/Raymond1030/nano-banana-skills ~/.gemini/skills/nanobanana` |

### Prerequisites

```bash
pip install google-genai Pillow
export GOOGLE_API_KEY="your-api-key-here"   # or GEMINI_API_KEY
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
python scripts/generate.py --prompt "a banana on a beach" --output banana.png

# Edit an image
python scripts/edit.py --input banana.png --prompt "add sunglasses" --output cool_banana.png

# Multi-turn refinement
python scripts/chat.py --prompt "a banana character" --refinement "make it more cartoon-like" --refinement "add a cape"
```

## License

MIT
