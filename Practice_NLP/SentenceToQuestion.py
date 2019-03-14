from textacy.spacier import utils
import spacy
nlp = spacy.load("en_core_web_sm")
inp = input()                       # The ingredients for an omelette are eggs, bacon, cheese, and onions, I do zip your code
doc = nlp(inp)
string,label = [],""

for sentence in doc.sents:
    root = sentence.root
    for i in sentence.ents:
        if len(utils.get_subjects_of_verb(root)) or len(utils.get_objects_of_verb(root)) > 0:
            if i.root.text == str(utils.get_subjects_of_verb(root)[0]):
                label = i.label_
            elif i.root.text == str(utils.get_objects_of_verb(root)[0]):
                label = i.label_

    if len(utils.get_subjects_of_verb(root)) > 0:
        if root.lemma_ == 'be':
            if label == "PERSON":
                ques = 'Who ' + str(root)+" "+ str(utils.get_subjects_of_verb(root)[0]) +' ?'
            elif label == "QUANTITY":
                ques = 'How ' + str(root)+" "+ str(utils.get_subjects_of_verb(root)[0]) +' ?'
            elif label == "MONEY":
                ques = 'How much ' + str(root) + " " + str(utils.get_subjects_of_verb(root)[0]) + ' ?'
            elif label == "TIME":
                ques = 'When ' + str(root)+" "+ str(utils.get_subjects_of_verb(root)[0]) +' ?'
            elif label == "GPE":
                ques = 'Where ' + str(root)+" "+ str(utils.get_subjects_of_verb(root)[0]) +' ?'
            elif label == 'PRODUCT':
                ques = 'What ' + str(root)+" "+ str(utils.get_subjects_of_verb(root)[0]) +' ?'
            else:
                for to in doc:
                    if to.pos_ == "VERB":
                        q = to.i
                question = doc
                for r in doc[q].rights:
                    for x,y in enumerate(r.subtree):
                        question = str(question).replace(str(y),"")
                print(str(question)+" what?")
                break
        else:
            if label == "PERSON":
                ques = 'Who does '+str(utils.get_objects_of_verb(root)[0])+" "+ root.lemma_+'?'
            elif label == "QUANTITY":
                ques = 'how does '+str(utils.get_objects_of_verb(root)[0])+" "+ root.lemma_+'?'
            elif label == "MONEY":
                ques = 'how much does '+str(utils.get_objects_of_verb(root)[0])+" "+ root.lemma_+'?'
            elif label == "TIME":
                ques = 'When does '+str(utils.get_objects_of_verb(root)[0])+" "+ root.lemma_+'?'
            elif label == "GPE":
                ques = 'Where does '+str(utils.get_objects_of_verb(root)[0])+" "+ root.lemma_+'?'
            elif label == 'PRODUCT':
                ques = 'What does '+str(utils.get_objects_of_verb(root)[0])+" "+ root.lemma_+'?'
            else:
                break

        string.append(ques)

print(string)














# other method
# for to in doc:
#         if to.pos_ == "VERB":
#             q = to.i
#     question = doc
#
#     for r in doc[q].rights:
#         for x,y in enumerate(r.subtree):
#             question = str(question).replace(str(y),"")
#     print(str(question)+" what?")


# if i.root.text == str(utils.get_subjects_of_verb(root)[0]):
#     label = i.label_
#     break
# elif str(utils.get_subjects_of_verb(root)[0]):
#     label = i.label_
# print(label)



# def print_structure():
#     for tokens in doc:
#         print(tokens.text, tokens.tag_, tokens.pos_, tokens.is_stop, tokens.lemma_)
# def print_question():
#     question = []
#     for token in doc:
#         if((token.tag_ in ['VBP','MD']) and token.is_stop == True):
#             question.insert(0, token.text)
#         else:
#             question.append(token.text)
#     question = ' '.join(question)
#     question = question.replace('.', '')
#     question += '?'
#     print('Statement:', format(stmt))
#     print('Question:', format(question))
# print_structure()
# # print_question()


# who, where, which, how
# for j in doc.ents:
#     if j.label_ == 'GPE' and j.text in a:
#         v = s.replace(j.text,"")
#         v = v.replace(t.text,"")
#         v = v.replace(w,"")
#         v = v.lower().replace("my","your")
#         first ="Where "
#     elif j.label_ == 'TIME' and j.text in a:
#         v = s.replace(j.text,"")
#         v = v.replace(t.text,"")
#         v = v.replace(w.text,"")
#         w = w.lemma_
#         first ="Which "
#     elif j.label_ == 'PERSON' and j.text in a:
#         v = s.replace(j.text,"")
#         v = v.replace(t.text,"")
#         v = v.replace(w.text,"")
#         w = w.lemma_
#         first ="Who "
#     elif j.label_ == 'QUANTITY' and j.text in a:
#         v = s.replace(j.text,"")
#         v = v.replace(t.text,"")
#         v = v.replace(w.text,"")
#         w = w.lemma_
#         first ="HOW "
#
# print(first+" "+str(w)+" "+v)












# other method
# for to in doc:
#         if to.pos_ == "VERB":
#             q = to.i
#     question = doc
#
#     for r in doc[q].rights:
#         for x,y in enumerate(r.subtree):
#             question = str(question).replace(str(y),"")
#     print(str(question)+" what?")



# def print_structure():
#     for tokens in doc:
#         print(tokens.text, tokens.tag_, tokens.pos_, tokens.is_stop, tokens.lemma_)
# def print_question():
#     question = []
#     for token in doc:
#         if((token.tag_ in ['VBP','MD']) and token.is_stop == True):
#             question.insert(0, token.text)
#         else:
#             question.append(token.text)
#     question = ' '.join(question)
#     question = question.replace('.', '')
#     question += '?'
#     print('Statement:', format(stmt))
#     print('Question:', format(question))
# print_structure()
# # print_question()


# who, where, which, how
# for j in doc.ents:
#     if j.label_ == 'GPE' and j.text in a:
#         v = s.replace(j.text,"")
#         v = v.replace(t.text,"")
#         v = v.replace(w,"")
#         v = v.lower().replace("my","your")
#         first ="Where "
#     elif j.label_ == 'TIME' and j.text in a:
#         v = s.replace(j.text,"")
#         v = v.replace(t.text,"")
#         v = v.replace(w.text,"")
#         w = w.lemma_
#         first ="Which "
#     elif j.label_ == 'PERSON' and j.text in a:
#         v = s.replace(j.text,"")
#         v = v.replace(t.text,"")
#         v = v.replace(w.text,"")
#         w = w.lemma_
#         first ="Who "
#     elif j.label_ == 'QUANTITY' and j.text in a:
#         v = s.replace(j.text,"")
#         v = v.replace(t.text,"")
#         v = v.replace(w.text,"")
#         w = w.lemma_
#         first ="HOW "
#
# print(first+" "+str(w)+" "+v)
