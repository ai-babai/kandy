import json
import time
from typing import List
import requests

from .models import GeneratedImage

class Text2ImageAPI:
    def __init__(self, url: str, api_key: str, secret_key: str):
        self.URL = url
        self.session = requests.Session()
        self.session.headers.update({
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        })

    def get_all_models(self) -> list:
        response = self.session.get(self.URL + 'key/api/v1/models')
        response.raise_for_status()
        return response.json()

    def generate(self, pos_prompt: str, neg_prompt: str, model: str = 4, images: int = 1, width: int = 1024, height: int = 1024) -> str:
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {"query": pos_prompt},
            "negativePromptUnclip": neg_prompt
            
        }
        data = {
            'model_id':(None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        print(data)
        response = self.session.post(self.URL + 'key/api/v1/text2image/run', files=data)
        response.raise_for_status()
        return response.json()['uuid']

    # В методе check_generation API
    def check_generation(self, request_id: str, attempts: int = 10, delay: int = 10) -> List[GeneratedImage]:
        for _ in range(attempts):
            response = self.session.get(self.URL + 'key/api/v1/text2image/status/' + request_id)
            data = response.json()
            if data['status'] == 'DONE':
                return [
                    GeneratedImage(
                        base64_str=img, 
                        status=data['status'], 
                        prompt=data.get('prompt')) 
                        for img in data['images']
                ]
            time.sleep(delay)
        return []
