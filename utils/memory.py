class ChatMemory:

    def __init__(self):

        self.history = []

    def add_message(
        self,
        question,
        answer
    ):

        self.history.append(
            {
                "question": question,
                "answer": answer
            }
        )

    def get_history(self):

        text = ""

        for item in self.history:

            text += (
                f"User: {item['question']}\n"
                f"Assistant: {item['answer']}\n"
            )

        return text
