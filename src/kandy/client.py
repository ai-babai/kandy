from .api import Text2ImageAPI
from .image_generator import ImageGenerator

class Kandy:
    def __init__(self, api_key: str, secret_key: str, base_url: str = 'https://api-key.fusionbrain.ai/'):
        api = Text2ImageAPI(base_url, api_key, secret_key)
        self.images = ImageGenerator(api)
