#Dictionary Project
import json
import difflib
class dictionary:
    def __init__(self,word):
        self.dict={}
        self.word=word
        self.py=json.load(open("data.json"))
        if self.word.lower() in self.py:
            print('\n'.join(self.py[self.word.lower()]))
        elif self.word.title() in self.py:
            print('\n'.join(self.py[self.word.title()]))
        elif self.word.capitalize() in self.py:
            print('\n'.join(self.py[self.word.capitalize()]))
        elif self.word.upper() in self.py:
            print('\n'.join(self.py[self.word.upper()]))
        else:
            self.g = difflib.get_close_matches(self.word.lower(), self.py, cutoff=0.1)[0]
            self.gu = difflib.get_close_matches(self.word.upper(), self.py, cutoff=0.1)[0]
            self.gue = difflib.get_close_matches(self.word.title(), self.py, cutoff=0.1)[0]
            self.gues = difflib.get_close_matches(self.word.capitalize(), self.py, cutoff=0.1)[0]
            self.a=difflib.SequenceMatcher(a=self.word.lower(),b=self.g).ratio()
            self.b=difflib.SequenceMatcher(a=self.word.upper(),b=self.gu).ratio()
            self.c=difflib.SequenceMatcher(a=self.word.title(),b=self.gue).ratio()
            self.d=difflib.SequenceMatcher(a=self.word.capitalize(),b=self.gues).ratio()
            self.dict[self.g]=self.a
            self.dict[self.gu]=self.b
            self.dict[self.gue]=self.c
            self.dict[self.gues]=self.d
            self.result=sorted(self.dict.items(),key=lambda x:x[1])
            print('You mean:{}'.format(self.result[len(self.result)-1][0]))
            self.h=input('Press Y if yes or Press N if no:')
            if(self.h=='Y'):
                print('\n'.join(self.py[self.result[len(self.result)-1][0]]))
            else:
                print('You entered the wrong word!!!')

word=input("Enter the word you want to search:")
dict=dictionary(word)
