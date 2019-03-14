import spacy
nlp = spacy.load('en_core_web_sm')
inp = input()
doc = nlp(inp)                        # I love India       #Someone has cleaned the windows
extra_strings,object_verb,object,subject,object = "","","","",""
for i in doc:
    if i.pos_ == 'VERB':
        verb = i.text
    elif i.dep_ == 'nsubj':
        if i.text == 'I': object = 'me'
        elif i.text == 'He': object = 'him'
        elif i.text == 'She': object = 'her'
        elif i.text == 'They': object = 'them'
        elif i.text == 'We': object = 'us'
        else: object = i
    elif i.dep_ == 'dobj':
        if i.tag_ == 'NNS':
            object_verb = "are"
        elif i.tag_ == 'NN':
            b = "is"
        subject += i.text.capitalize()
    else:
        extra_strings += i.text+" "

if subject and object_verb and verb and extra_strings and object:
    print(subject+" "+object_verb+" "+verb+" "+"by "+str(object))
else:
    print(subject+" "+verb+" "+" by "+str(object))
