# models/content_filter.py
from transformers import pipeline

moderator = pipeline("text-classification", model="facebook/roberta-hate-speech-dynabench-r4-target")

def check_content(message: str):
    """
    Uses Hugging Face ML model to classify text for unsafe content.
    """
    try:
        result = moderator(message, truncation=True)[0]
        label = result["label"]
        score = result["score"]

        if label.lower() in ["toxic", "offensive", "hate", "inappropriate"] or score > 0.7:
            return {"allowed": False, "reason": label, "score": score}
        else:
            return {"allowed": True, "reason": label, "score": score}

    except Exception as e:
        return {"allowed": True, "reason": f"error: {str(e)}"}
