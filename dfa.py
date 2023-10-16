from state import State


class DFA:
    def __init__(self,in_file):
        self.states=[]
        self.labels=""
        f = open(in_file, "r")
        self.alphabet = f.readline()[2:-1]
        for line in f:
            new_states={}
            i=0
            for symbol in self.alphabet:
                new_states.update({symbol:line[2+i]})
                i+=1
            self.labels+=line[0]
            self.states.append(State(line[0],
                                 True if line[1]=="*" else False,
                                 new_states
                                 ))
            print(new_states)
        

    def check(self,word):
        for c in word:
            if not c in self.alphabet: 
                return False
        
        curr_s = self.states[0]
        for c in word:
            curr_s = self.states[self.labels.find(curr_s.compute(c))]
        return curr_s.is_final()