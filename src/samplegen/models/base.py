from dataclasses import dataclass


@dataclass
class ModelSpec:
    name: str
    supports_key_conditioning: bool = False
    notes: str = ""
