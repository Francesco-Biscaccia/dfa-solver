class State:

    def __init__(self,name,final_state=False,*links):
        self.name=name
        self.final_state=final_state
        self.links=links[0]

    def compute(self,c):
        return self.links[c]
    
    def is_final(self):
        return self.final_state
