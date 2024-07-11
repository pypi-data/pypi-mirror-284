from .embedder import Embedder


class HFEmbedder(Embedder):
    def __init__(self, model, text, *args, **kwargs) -> None:
        super().__init__(model, text)
        self.text = self._tokenize(text, kwargs["tokenizer"])

    def _tokenize(text):
        raise NotImplementedError

    def embed(self, batch):
        raise NotImplementedError
