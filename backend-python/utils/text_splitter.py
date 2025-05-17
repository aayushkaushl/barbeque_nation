
def chunk_text(data, max_words=700):
    chunks = []
    for section in data.get("sections", []):
        words = section["text"].split()
        while words:
            chunk = words[:max_words]
            words = words[max_words:]
            chunks.append(" ".join(chunk))
    return chunks
