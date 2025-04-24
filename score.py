
import json
import joblib
import pandas as pd
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path("model")
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)['data']
        df = pd.DataFrame(data)
        preds = model.predict(df).tolist()
        return json.dumps(preds)
    except Exception as e:
        return json.dumps({"error": str(e)})
