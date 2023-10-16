from dfa import DFA

d = DFA("./test/input_0.txt")
s="a010001"
if d.check(s):
    print("Your DFA accept the string "+s)
else: 
    print("Try another DFA!")
