import spacy

nlp = spacy.load('en_core_web_sm')
inp = input()                          # Apple and Google are 400 billion and 500 billion dollars respectively
doc = nlp(inp)

for i in doc:
    if i.pos_ == "NOUN" and i.dep_ == "nsubj":
        for j in i.head.subtree:
            if j.dep_ == 'attr' or j.dep_ == 'prep' or j.dep_ == 'pobj':
                    print(i)

for i in doc.ents:
    print(i)
