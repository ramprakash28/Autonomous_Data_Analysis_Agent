import eda
from llm import call_llm
from tools import inspect_csv
from eda import run_eda
from memory import save_to_memory
import json
import pandas as pd
import numpy as np

data_path = "Exam_Score_Prediction.csv"

#Json serialization helper
def to_json_serializable(obj):
        if isinstance(obj, pd.DataFrame):
            return obj.to_dict(orient="records")
        elif isinstance(obj, pd.Series):
            return obj.to_dict()
        elif isinstance(obj, dict):
            return {k: to_json_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [to_json_serializable(i) for i in obj]
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, (np.integer, np.floating)):
            return obj.item()
        elif isinstance(obj, np.bool_):
            return bool(obj)
        elif isinstance(obj, (np.datetime64, np.timedelta64)):
            return str(obj)
        else:
            return obj

def explain_findings(observations: dict):
    safe_observations = to_json_serializable(observations)
    prompt = f"""
    You are a senior data analyst.

    Explain the key insights, risks, and recommended next steps
    based on the following EDA observations:

    {json.dumps(observations, indent=2)}

    Respond in clear, concise paragraphs.
    """
    return call_llm(prompt)

def agent_loop():
    observations = inspect_csv(data_path)
    print("DATASET OBSERVATIONS:")
    safe_observations = to_json_serializable(observations)
    print(json.dumps(to_json_serializable(observations), indent=2))

    #Run EDA
    eda_results = run_eda(observations)
    safe_eda_results = to_json_serializable(eda_results)

    # Save to memory
    save_to_memory(safe_eda_results)

    # Generate explanation
    explanation = explain_findings(safe_eda_results)
    print("\nAGENT EXPLANATION:")
    print(explanation)

    prompt = f"""
    You are an expert data analyst.

    Based on the EDA results below, decide the NEXT action.
    Choose ONLY ONE:
    - clean_data
    - perform_eda
    - modeling
    - stop

    EDA Results:
    {json.dumps(safe_eda_results, indent=2)}
    Return only the action name.
    """

    decision = call_llm(prompt).strip().lower()
    print(f"AGENT DECISION: {decision}")

if __name__ == "__main__":
    agent_loop()

