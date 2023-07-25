import paralleldots
class API:
    def __init__(self):
        paralleldots.set_api_key("zD4kwtbEC99JzQhipSIu16MqqPggujYUyb7fl8SZZtc")

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response
    def ner(self,text):
        pass