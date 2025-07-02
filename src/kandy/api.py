import json
import time
from typing import List
import requests

from .models import GeneratedImage

class Text2ImageAPI:
    def __init__(self, url: str, api_key: str, secret_key: str):
        self.URL = url
        self.session = requests.Session()
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }
        self.session.headers.update(self.AUTH_HEADERS)

    def get_all_pipelines(self) -> list:
        response = self.session.get(self.URL + 'key/api/v1/pipelines')
        response.raise_for_status()
        return response.json()

    def generate(self, pos_prompt: str, pipeline_id: str = "pipeline_id", images: int = 1, width: int = 1024, height: int = 1024) -> str:
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {"query": pos_prompt},
            
        }
        data = {
            'pipeline_id':(None, pipeline_id),
            'params': (None, json.dumps(params), 'application/json')
        }
        # print(data)
        response = self.session.post(self.URL + 'key/api/v1/pipeline/run', files=data)
        response.raise_for_status()
        return response.json()['uuid']

    # В методе check_generation API
    def check_generation(self, request_id: str, attempts: int = 10, delay: int = 10) -> List[GeneratedImage]:
        for _ in range(attempts):
            response = self.session.get(self.URL + 'key/api/v1/pipeline/status/' + request_id)
            data = response.json()
            if data['status'] == 'DONE':
                return [
                    GeneratedImage(
                        base64_str=img, 
                        status=data['status'], 
                        prompt=data.get('result')) 
                        for img in data['result']['files']
                ]
            time.sleep(delay)
        return []
