# Simple Kandinsky Python SDK

Kandinsky:
https://fusionbrain.ai/

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

## Usage

```python
from client import Kandy

kandy = Kandy(api_key="your_api_key", secret_key="your_secret_key")

images = kandy.images.generate(
    pos_prompt="positive prompt",
    neg_prompt="negative prompt"
)

if images:
    image = images[0].to_image()
    image.save("generated_image.png")
```


Для работы с SDK Kandinsky необходимо получить API ключи. Вы можете зарегистрироваться и получить свои ключи на официальном сайте Fusion Brain, где доступен сервис Kandinsky. Перейдите по ссылке ниже для получения ключей:


# Как получить ключи для Api Kandinsky на FusionBrain
1. Перейдите на сайт [fusionbrain.ai](https://fusionbrain.ai/)
2. Зарегистрируйтесь или войдите в свой аккаунт.
3. Найдите слева раздел API для получения ключей для Kandinsky.
4. Следуйте инструкциям на сайте для генерации вашего персонального API ключа и секретного ключа.
