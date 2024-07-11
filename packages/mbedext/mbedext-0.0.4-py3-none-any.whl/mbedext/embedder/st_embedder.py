from typing import Union, Optional

from .embedder import Embedder

class STEmbedder(Embedder):
    def __init__(self, model, text) -> None:
        super().__init__(model, text)

    def embed(self, batch: Union[list[str], str], batch_size: Optional[int] = 256):
        return self.model.encode(batch, batch_size=batch_size, convert_to_tensor=True)