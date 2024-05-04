import joblib


class MachineLearningService:
    def run(self, data):
        try:
            model = joblib.load(data.get("path"))
            result = model.predict([data.get("inputs")])

            return {"anomaly": True if result == [-1] else False}, None

        except Exception as e:
            return None, {"MachineLearningError": str(e)}
