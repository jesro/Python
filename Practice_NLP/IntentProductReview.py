import spacy
nlp = spacy.load('en_core_web_sm')
inp = input()         # Camera picture quality is good worth for money
doc = nlp(inp)
for dc in doc.sents:
    #for i in dc:
    # if i.pos_ in ['ADV','ADJ']:
    #      for child in i.head.children:
    #          if child.dep_ == 'nsubj':
    #              for t in child.children:
    #                 print(t)
    #              print(child)
    for i in dc.noun_chunks:
        if i.root.dep_ == 'nsubj':
            if len(i.text) > 5:
                if i:
                    print(i)
            else:
                print(i.root)
        print(i)
