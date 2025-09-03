from models.abuse_detector import check_abuse
from models.escalation_detector import check_escalation
from models.crisis_detector import check_crisis
from models.content_filter import check_content

def run_chat():
    print(" AI Safety Chat POC (type 'exit' to quit)\n")
    history = []
    while True:
        msg = input("User: ")
        if msg.lower() == "exit":
            break

        history.append(msg)

        results = {
            "abuse": check_abuse(msg),
            "escalation": check_escalation(history),
            "crisis": check_crisis(msg),
            "content": check_content(msg)
        }

        print(f"\nSafety Analysis → {results}\n")

if __name__ == "__main__":
    run_chat()
