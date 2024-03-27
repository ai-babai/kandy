from dataclasses import dataclass
from typing import Optional
from PIL import Image
import base64
from io import BytesIO


@dataclass
class GeneratedImage:
    base64_str: str
    status: str
    seed: Optional[int] = None
    prompt: Optional[str] = None

    def to_image(self) -> Image:
        """Converts base64 string to a PIL.Image object."""
        return Image.open(BytesIO(base64.b64decode(self.base64_str)))

    @property
    def base64(self) -> str:
        """Returns the base64 string of the image."""
        return self.base64_str
