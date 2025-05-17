def get_response(message, kb_data):
    message = message.lower()
    for item in kb_data.get("faqs", []):
        if message in item["question"].lower():
            return item["answer"]
    return "Sorry, I don't have information on that. Please try again."
