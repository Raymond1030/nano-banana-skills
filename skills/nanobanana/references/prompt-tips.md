# Prompt Engineering Tips for Nano Banana

## General Guidelines

- **Be specific and descriptive**: Include details about style, lighting, composition, colors, mood
- **Specify art style** if the user hasn't: "digital art", "watercolor", "photorealistic", "3D render", "pixel art", etc.
- **Include technical details**: camera angle, lighting direction, background description
- **For text in images**: Nano Banana Pro excels at rendering legible text — wrap the desired text in quotes within the prompt
- **Enhance vague prompts**: If the user says "draw me a cat", enhance it to something like "A cute orange tabby cat sitting on a windowsill, soft natural lighting, digital illustration style, warm colors" — but stay true to the user's intent

## Prompt Structure

A good prompt follows this pattern:

```
[Subject] + [Action/Pose] + [Style] + [Lighting] + [Background] + [Mood/Atmosphere]
```

Example: "A golden retriever puppy playing in autumn leaves, watercolor style, warm afternoon sunlight, forest background, cheerful and playful mood"

## Model-Specific Tips

### Nano Banana 2 (gemini-3.1-flash-image-preview)
- Best all-around model for most use cases
- Good balance of speed and quality
- Works well with both simple and detailed prompts

### Nano Banana Pro (gemini-3-pro-image-preview)
- Use for complex compositions with multiple subjects
- Best for text rendering in images
- Supports up to 4K resolution
- Handles nuanced art style descriptions better

### Nano Banana (gemini-2.5-flash-image)
- Fastest generation speed
- Best for high-volume batch generation
- Keep prompts concise for best results
