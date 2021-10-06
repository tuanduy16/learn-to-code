#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Answer:
    def __init__(self, text, flag):
        self.text = text
        self.flag = flag
        
    def clone(self):
        return Answer(self.text, False)

class Question:
    def __init__(self, text, aws):
            self.text = text
            self.aws = aws
        
    def display(self):
        for i in self.aws:
            print(i.text)
            
    def clone(self):
        q = Question(self.text, [])
        answer = []
        for i in self.aws:
            answers.append(i.clone())
        q.aws = answers.copy()
        return q
        
               
class ListQuestion:
    def __init__(self, path):
        self.path = path
        self.qs = self.load()
    
    def load(self):
        list_question = []
        f = open(self.path, 'r')
        for line in f:
            q = line.split('|')
            question = Question(q[0],[Answer(q[1],eval(q[5])),Answer(q[2],eval(q[6])),Answer(q[3],eval(q[7])),Answer(q[4],eval(q[8]))])
            list_question.append(question)
        f.close()
        return list_question
    
    def clone(self):
        questions = []
        for i in self.qs:
            questions.append(i.clone())
        return questions

test = ListQuestion('data.txt')
print(len(test.qs))

            

