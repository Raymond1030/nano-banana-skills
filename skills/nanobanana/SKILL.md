---
name: nanobanana
version: 1.0.0
license: MIT
description: Generate and edit images using Google's Nano Banana API (Gemini image generation). Use this skill whenever the user asks to create, generate, produce, or edit images/pictures/illustrations/graphics, or mentions "nano banana", "nanobanana", image generation, AI art, or wants to visualize any concept as an image. Also trigger when the user provides an image and asks to modify, edit, or transform it.
---

# Nano Banana Image Generator

Generate and edit images using Google's Nano Banana models via the Gemini API.

## Available Models

| Model | ID | Best For | Resolution |
|-------|-----|----------|------------|
| Nano Banana 2 | `gemini-3.1-flash-image-preview` | Fast, high-quality (default) | Up to 1K |
| Nano Banana Pro | `gemini-3-pro-image-preview` | Pro-grade, complex prompts, 4K | Up to 4K |
| Nano Banana | `gemini-2.5-flash-image` | Speed, high-volume | Up to 1K |

Default to **Nano Banana 2** (`gemini-3.1-flash-image-preview`) unless the user specifically requests Pro quality or 4K resolution.

## Model Selection

Before generating, present the user with a model choice if they haven't already specified one:

> **Choose a model (or press Enter for default):**
> 1. **Nano Banana 2** (default) — Fast, high-quality, up to 1K
> 2. **Nano Banana Pro** — Pro-grade, complex prompts, up to 4K
> 3. **Nano Banana** — Fastest, high-volume, up to 1K

Use AskUserQuestion to let the user pick. If the user:
- Replies with `1`, empty, or doesn't choose → use `gemini-3.1-flash-image-preview`
- Replies with `2` or mentions "pro"/"4K"/"high quality" → use `gemini-3-pro-image-preview`
- Replies with `3` or mentions "fast"/"speed"/"quick" → use `gemini-2.5-flash-image`
- Already specified a model in their original request → skip the prompt and use that model directly

## Prerequisites

The user needs:
1. `google-genai` Python package (`pip install google-genai`)
2. `Pillow` for image handling (`pip install Pillow`)
3. A Google AI API key set as `GOOGLE_API_KEY` environment variable (or `GEMINI_API_KEY`)

If packages are missing, install them automatically. If the API key is missing, ask the user to set it up.

## CLI Scripts

All scripts are located in `scripts/` relative to this skill. Use them directly via `python`:

### Text-to-Image Generation

```bash
python scripts/generate.py --prompt "PROMPT" [--model MODEL] [--output FILE] [--count N] [--aspect-ratio RATIO] [--resolution RES]
```

Options:
- `--prompt` (required): Text prompt for image generation
- `--model`: Model ID (default: `gemini-3.1-flash-image-preview`)
- `--output`: Output file path (default: `output.png`)
- `--count`: Number of images 1-4 (default: 1)
- `--aspect-ratio`: `1:1`, `3:4`, `4:3`, `9:16`, `16:9`
- `--resolution`: `512`, `1k`, `2k`, `4k` (4k requires Pro model)

### Image Editing

```bash
python scripts/edit.py --input IMAGE --prompt "EDIT INSTRUCTION" [--model MODEL] [--output FILE]
```

Options:
- `--input` (required): Input image path
- `--prompt` (required): Edit instruction
- `--model`: Model ID (default: `gemini-3.1-flash-image-preview`)
- `--output`: Output file path (default: `edited.png`)

### Multi-turn Chat (Iterative Refinement)

```bash
python scripts/chat.py --prompt "INITIAL PROMPT" [--refinement "REFINE 1"] [--refinement "REFINE 2"] [--model MODEL] [--output-prefix PREFIX]
```

Options:
- `--prompt` (required): Initial prompt
- `--refinement`: Refinement prompt (can be specified multiple times)
- `--model`: Model ID (default: `gemini-3.1-flash-image-preview`)
- `--output-prefix`: Output file prefix (default: `chat_output`)

## Core Workflow

### Step 1: Run the appropriate script

Use the CLI scripts above based on the user's request. Run them from the skill's directory.

### Step 2: Display the result

After generation, use the Read tool to show the image to the user. Tell them the file path.

## Prompt Engineering

When constructing the image generation prompt, enhance vague prompts with style, lighting, composition, and mood details while staying true to the user's intent. See `references/prompt-tips.md` for detailed guidance.

## Output Conventions

- Save images to the current working directory by default
- Use descriptive filenames: `banana_logo.png`, `sunset_landscape.png`
- Always use `.png` format for best quality
- After saving, use the Read tool to display the image to the user
- Report the full file path so the user can find it

## Error Handling

- If `google-genai` is not installed: run `pip install google-genai Pillow`
- If API key is missing: tell the user to set `GOOGLE_API_KEY` or `GEMINI_API_KEY`
- If the model returns only text (no image): the prompt may have been filtered or too ambiguous — suggest the user rephrase
- If rate limited: suggest waiting a moment or switching to a faster model
