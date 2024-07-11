class BaseLogger:
    def log(self, level: str, message: str):
        raise NotImplementedError("Subclasses should implement this method.")
