# Simple Kandinsky Python SDK

For working with the Kandinsky SDK, you need to obtain API keys. You can register and receive your keys on the official Fusion Brain website, where the Kandinsky service is available. Follow the link below to get your keys:

[Kandinsky on FusionBrain](https://fusionbrain.ai/)

## Components

- **Text2ImageAPI**: Manages authentication, requests to generate images, and retrieves results.
- **ImageGenerator**: Uses `Text2ImageAPI` for image generation based on textual prompts.
- **Kandy**: Provides an interface for interacting with `ImageGenerator` and `Text2ImageAPI`.
- **GeneratedImage**: Stores generated image information and converts base64 to PIL image objects.

## Requirements

- Python 3.6+
- requests
- Pillow

## Installation

```bash
pip install requests Pillow
```

Or install directly from the GitHub repository:

```bash
pip install git+https://github.com/maxim-popkov/kandy.git
```

## Usage

```python
from kandy import Kandy

kandy = Kandy(api_key="your_api_key", secret_key="your_secret_key")

images = kandy.images.generate(
    pos_prompt="positive prompt",
    neg_prompt="negative prompt"
)

if images:
    image = images[0].to_image()
    image.save("generated_image.png")
```

# How to obtain Kandinsky API keys on FusionBrain
1. Go to [fusionbrain.ai](https://fusionbrain.ai/)
2. Register or log into your account.
3. Find the API section on the left to obtain keys for Kandinsky.
4. Follow the instructions on the site to generate your personal API key and secret key.
