from app.services.split_strategies import SplitStrategy

class PercentSplitStrategy(SplitStrategy):
    def calculate(self, total_amount, splits):
        total_percent = sum(s["percent"] for s in splits)
        if total_percent != 100:
            raise ValueError("Percent split must sum to 100")
        return {
            s["user_id"]: round((s["percent"]/100)*total_amount, 2)
            for s in splits
        }