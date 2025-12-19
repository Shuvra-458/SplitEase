from app.services.split_strategies import SplitStrategy

class ExactSplitStrategy(SplitStrategy):
    def calculate(self, total_amount, splits):
        total = sum(s["amount"] for s in splits)
        if round(total, 2) != round(total_amount, 2):
            raise ValueError("Exact splits amount do not sum to total")
        return {s["user_id"]: s["amount"] for s in splits}