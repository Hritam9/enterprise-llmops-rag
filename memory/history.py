import uuid

from memory.models import Conversation
from memory.repository import ConversationRepository


class ConversationMemory:

    def __init__(self):

        self.repo = ConversationRepository()

    def new_session(self):

        return str(uuid.uuid4())

    def save(

        self,

        session_id,

        question,

        answer,

        confidence,

    ):

        self.repo.save(

            Conversation(

                session_id=session_id,

                question=question,

                answer=answer,

                confidence=confidence,

            )

        )

    def history(

        self,

        session_id,

    ):

        return self.repo.history(session_id)
