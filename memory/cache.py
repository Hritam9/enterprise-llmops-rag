import hashlib
import time


class ResponseCache:

    def __init__(self):

        self.cache = {}

        self.ttl = 600

    def _key(

        self,

        question,

    ):

        return hashlib.md5(

            question.encode()

        ).hexdigest()

    def get(

        self,

        question,

    ):

        key = self._key(question)

        value = self.cache.get(key)

        if not value:

            return None

        if time.time() - value["time"] > self.ttl:

            del self.cache[key]

            return None

        return value["response"]

    def set(

        self,

        question,

        response,

    ):

        self.cache[

            self._key(question)

        ] = {

            "response": response,

            "time": time.time(),

        }
