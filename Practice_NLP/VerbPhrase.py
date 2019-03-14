# import spacy
# from textacy.spacier import utils
# nlp = spacy.load("en_core_web_sm")
# inp = input()                      #  You have woken up everyone in the neighborhood.
# doc = nlp(inp)
# for i in doc.sents:
#     print(utils.get_objects_of_verb(i.root))
    # if i.pos_ in 'VERB':
    #     for child in i.children:
    #         if child.dep_ in ['aux','nummod', 'nmod', 'advmod', 'advcl', 'acl', 'amod', 'appos', 'ccomp' , 'obj', 'iobj','prt','acomp']:
    #             print(child)
    #     print(i)

#Other method
from __future__ import unicode_literals
import spacy,en_core_web_sm
import textacy
nlp = en_core_web_sm.load()
sent = textacy.extract.pos_regex_matches(textacy.Doc('I bought a Watch yesterday in your site. Its worth the money', lang='en_core_web_sm'), r'<VERB>?<ADV>*<VERB>+')
for verb in sent:
    print(verb.text)
