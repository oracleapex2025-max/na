import random

class AIChat:
    def __init__(self, db):
        self.db = db

    def get_response(self, user_message: str) -> str:
        # Save user message to history
        self.db.save_message("User", user_message)

        # Simple AI logic (random responses for now)
        responses = [
            "Interesting! Tell me more.",
            "Why do you think that?",
            "Hmm, I see.",
            "That's cool!",
            "Can you explain further?"
        ]
        ai_message = random.choice(responses)

        # Save AI response to history
        self.db.save_message("AI", ai_message)
        return ai_message
