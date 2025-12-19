from app.services.split_strategies.base import SplitStrategy

class EqualSplitStrategy(SplitStrategy):
    def calculate(self, total_amount, splits):
        per_head = round(total_amount / len(splits), 2)
        return {s["user_id"]: per_head for s in splits}