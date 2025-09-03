# AI Safety Models - Proof of Concept

##  Overview
This project demonstrates a **Proof of Concept (POC)** for AI Safety in conversational platforms.  
It simulates a chat system that analyzes user input in **real-time** for potential risks.

### Features
-  **Abuse Language Detection** – Flags harmful or offensive text.  
-  **Escalation Recognition** – Detects increasing aggression in conversations.  
-  **Crisis Intervention** – Identifies distress or self-harm signals.  
-  **Content Filtering** – Ensures age-appropriate and safe content.  

---

##  Setup Instructions

### 1. Clone the Repository
```
git clone git@github.com:Gitaayus/AI-SAFETY-PC.git
cd ai-safety-poc
```

## Create Virtual Environment

```
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

## Install Dependencies

```
pip install -r requirements.txt
```
## Run the Chat POC

```
python app.py
```

## Example

 AI Safety Chat POC (type 'exit' to quit)

User: I want to end my life
Safety Analysis → {
  'abuse': {'toxic': True, 'score': 0.68},
  'escalation': {'escalating': False},
  'crisis': {'crisis': False, 'label': 'self-harm', 'score': 0.64},
  'content': {'allowed': False, 'reason': 'nothate', 'score': 0.99}
}

## Models Used

- Abuse Detector – unitary/toxic-bert

- Escalation Detector – Sentiment Analysis Pipeline

- Crisis Detector – facebook/bart-large-mnli (Zero-Shot Classification)

- Content Filter – facebook/roberta-hate-speech-dynabench-r4-target

## Author

Aayush Pandey – AI Developer