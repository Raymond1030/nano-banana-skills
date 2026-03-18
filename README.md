# Nano Banana Skills

Generate and edit images using Google's Nano Banana (Gemini) API as AI agent skills.

Nano Banana Skills follows the open [Agent Skills](https://github.com/anthropics/claude-code/blob/main/docs/skills.md) standard. Simply copy the skill folders into your skills directory and your AI agent will automatically discover and use them.

## Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/Raymond1030/nano-banana-skills.git
```

### Step 2: Copy Skills to Your Skills Directory

Copy the individual skill folders from `skills/` to one of the supported skill directories below. You can install skills globally (available across all projects) or per-project.

**Global installation** (recommended — skills available everywhere):

| Tool | Directory |
|------|-----------|
| Claude Code | `~/.claude/skills/` |
| Cursor | `~/.cursor/skills/` |
| Codex | `~/.codex/skills/` |
| Gemini CLI | `~/.gemini/skills/` |

```bash
# Example: install for Claude Code (global)
cp -r nano-banana-skills/skills/nanobanana ~/.claude/skills/
```

**Per-project installation** (available only in that project):

```bash
# From your project root
cp -r nano-banana-skills/skills/nanobanana .claude/skills/
```

### Step 3: Install Python Dependencies

```bash
pip install google-genai Pillow
```

### Step 4: Set Your API Key

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
python scripts/generate.py --prompt "a banana on a beach" --output banana.png

# Edit an image
python scripts/edit.py --input banana.png --prompt "add sunglasses" --output cool_banana.png

# Multi-turn refinement
python scripts/chat.py --prompt "a banana character" --refinement "make it more cartoon-like" --refinement "add a cape"
```

## License

MIT
