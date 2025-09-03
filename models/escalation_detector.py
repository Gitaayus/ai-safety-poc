from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def check_escalation(history: list):
    if len(history) < 2:
        return {"escalating": False}

    last_two = history[-2:]
    scores = [sentiment_model(m)[0] for m in last_two]

    if (scores[0]['label'] == "NEGATIVE" and scores[1]['label'] == "NEGATIVE" 
        and scores[1]['score'] > scores[0]['score']):
        return {"escalating": True}
    else:
        return {"escalating": False}
