# File name: model_on_ray_serve.py
import ray
from ray import serve
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification


def classify(text):
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    finbert = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
    classifier = pipeline("sentiment-analysis", model=finbert, tokenizer=tokenizer, return_all_scores=True)
    scores = classifier(text)
    return scores


ray.init(address="auto")
#serve.start(detached=True)


@serve.deployment
def router(request):
    txt = request.query_params["txt"]
    return classify(txt)


#router.deploy()
