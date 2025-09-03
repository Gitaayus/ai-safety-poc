from transformers import pipeline

zero_shot = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def check_crisis(message: str):
    labels = ["self-harm", "distress", "safe"]
    result = zero_shot(message, candidate_labels=labels)
    top = result['labels'][0]
    score = float(result['scores'][0])
    return {
        "crisis": True if top in ["self-harm", "distress"] and score > 0.7 else False,
        "label": top,
        "score": score
    }
