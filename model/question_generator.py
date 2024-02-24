import spacy
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from constants import MODEL_PATH


class QuestionGenerator: 
    def __init__(self):
        ckpt_path = MODEL_PATH
        self.model = AutoModelForSeq2SeqLM.from_pretrained(ckpt_path)
        self.tokenizer = AutoTokenizer.from_pretrained('t5-base')

    def _load_spacy(self):
        try:
            return spacy.load('en_core_web_sm')
        except IOError:
            from spacy.cli.download import download as spacy_download
            spacy_download('en_core_web_sm')
            return spacy.load('en_core_web_sm')

    def _run_model(self, input_string, model, tokenizer, device, **generator_args):
        input_ids = tokenizer.encode(input_string, return_tensors="pt").to(torch.device(device))
        res = model.generate(input_ids, **generator_args)
        output = tokenizer.batch_decode(res, skip_special_tokens=True)
        return output[0] if output else None

    def get_entities(self, text):
        seen = set()
        entities = []

        spacy_nlp = self._load_spacy()

        for entity in spacy_nlp(text).ents:
            if entity.text not in seen:
                seen.add(entity.text)
                entities.append(entity)
        return sorted(entities, key=lambda e: e.text)

    def generate_question(self, context, answer):
        return self._run_model(f"generate question: {answer} context: {context}", self.model, self.tokenizer, 'cpu', max_length=50)
