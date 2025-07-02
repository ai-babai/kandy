
class ImageGenerator:
    def __init__(self, api):
        self._api = api

    def generate(self, pos_prompt: str, **kwargs):
        pipelines = self._api.get_all_pipelines()
        if not pipelines:
            print("No pipelines available.")
            return None
            
        pipeline_id = pipelines[0]['id']  # Используем первую доступную модель
        uuid = self._api.generate(pos_prompt, pipeline_id, **kwargs)
        images = self._api.check_generation(uuid)
        return images
