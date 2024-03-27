
class ImageGenerator:
    def __init__(self, api):
        self._api = api

    def generate(self, pos_prompt: str, neg_prompt: str, **kwargs):
        models = self._api.get_all_models()
        if not models:
            print("No models available.")
            return None
            
        model_id = models[0]['id']  # Используем первую доступную модель
        uuid = self._api.generate(pos_prompt, neg_prompt, model_id, **kwargs)
        images = self._api.check_generation(uuid)
        return images
