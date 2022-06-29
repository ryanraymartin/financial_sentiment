# File name: local_model.py
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# use transformers==4.19.0 for better output

def classify(text):
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    finbert = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
    nlp = pipeline("sentiment-analysis", model=finbert, tokenizer=tokenizer, return_all_scores=True)
    results = nlp(text)
    return results


sentences = "Stocks rallied and the British pound gained."
results = classify(sentences)
print(results[0])  # LABEL_0: neutral; LABEL_1: positive; LABEL_2: negative
