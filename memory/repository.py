from memory.database import Database
from memory.models import Conversation


class ConversationRepository:

    def save(

        self,

        conversation: Conversation,

    ):

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute(

            """

            INSERT INTO conversations(

                session_id,

                question,

                answer,

                confidence

            )

            VALUES (?, ?, ?, ?)

            """,

            (

                conversation.session_id,

                conversation.question,

                conversation.answer,

                conversation.confidence,

            ),

        )

        conn.commit()

        conn.close()

    def history(

        self,

        session_id: str,

    ):

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute(

            """

            SELECT *

            FROM conversations

            WHERE session_id=?

            ORDER BY created_at

            """,

            (session_id,),

        )

        rows = cursor.fetchall()

        conn.close()

        return rows
