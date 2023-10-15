from state import State

class DFA:
    def __init__(self,in_file):
        self.states=[]
        self.labels=""
        f = open(in_file, "r")
        for line in f:
            self.labels+=line[0]
            self.states.append(State(line[0],
                                 True if line[1]=="*" else False,
                                 {"0":line[2],"1":line[3]}
                                 ))

    def check(self,word):
        curr_s = self.states[0]
        for c in word:
            curr_s = self.states[self.labels.find(curr_s.compute(c))]
        return curr_s.is_final()