from transformers import pipeline

abuse_model = pipeline("text-classification", model="unitary/toxic-bert")

def check_abuse(message: str):
    result = abuse_model(message)[0]
    return {
        "toxic": True if result['label'].lower() == "toxic" else False,
        "score": float(result['score'])
    }
