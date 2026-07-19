from dataclasses import dataclass


@dataclass
class Conversation:

    session_id: str

    question: str

    answer: str

    confidence: float
