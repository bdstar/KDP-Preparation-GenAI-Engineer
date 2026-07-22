# competency_map.py
from dataclasses import dataclass
import json
from pathlib import Path
 
@dataclass
class Competency:
    name: str
    target: int          # desired proficiency 0-5
    current: int = 0     # your self-assessment 0-5
 
    @property
    def gap(self) -> int:
        return max(self.target - self.current, 0)
 
STACK = [
    Competency("Python foundations & toolkit", target=5),
    Competency("ML / DL / NLP core", target=4),
    Competency("Transformers & LLMs", target=4),
    Competency("Prompting & fine-tuning (PEFT)", target=4),
    Competency("RAG & vector databases", target=5),
    Competency("Agents & orchestration", target=4),
    Competency("APIs, backends & data engineering", target=4),
    Competency("MLOps / LLMOps & inference optimization", target=3),
    Competency("Safety, guardrails & observability", target=3),
]
