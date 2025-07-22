import spacy

class SpacyNLP:
    def __init__(self, model_name="en_core_web_sm"):
        self.nlp = spacy.load(model_name)

    def analyze_text(self, text):
        doc = self.nlp(text)
        for token in doc:
            print(f"{token.text:<12} | POS: {token.pos_:<10} | Lemma: {token.lemma_}")

    def process_text(self, text):
        doc = self.nlp(text)
        return [(token.text, token.pos_, token.dep_) for token in doc]

# Example usage
if __name__ == "__main__":
    spacy_nlp = SpacyNLP()
    text = "Alice Johnson worked at Microsoft for 3 years as a Software Engineer in Seattle."
    spacy_nlp.analyze_text(text)
