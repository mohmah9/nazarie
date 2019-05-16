

class DFA :

    def __init__(self ,states,alphabet,initial , finals):
        self.states=states
        self.alphabet=alphabet
        self.trans_func="δ"
        self.initial=initial
        self.finals=finals
        self.to_dic()

    def to_dic(self):
        my_dfa={}
        my_dfa["nodes"] = self.nodes
        my_dfa["alphabet"] = self.alphabet
        my_dfa["func"]=self.trans_func
        my_dfa["initial"]=self.initial
        my_dfa["finals"]=self.finals


class NFA :

    def __init__(self ,states,alphabet,initial,trans_func ,state_num, finals):
        self.state_num=state_num
        self.states=states
        self.alphabet=alphabet
        self.initial=initial
        self.finals=finals
        self.trans_func = trans_func
        self.to_dic()

    def to_dic(self):
        my_nfa={}
        my_nfa["states"] = self.states
        my_nfa["state_num"] = self.state_num
        my_nfa["alphabet"] = self.alphabet
        my_nfa["func"]=self.trans_func
        my_nfa["initial"]=self.initial
        my_nfa["finals"]=self.finals
        print("NFA Done.")
        # print(my_nfa)


if __name__ =='__main__':
    file = open("input.txt" , "r")
    contents = file.readlines()
    file.close()
    for i in range(len(contents)):
        contents[i]=contents[i].strip()
    my_statesNO = int(contents[0])
    my_alph = contents[1].split(",")
    for i in contents:
        if i[0:2] == "->":
            my_init = i.split(',')[0][2:]
    my_finals=[]
    for i in contents:
        j = i.split(",")
        for k in j:
            if k[0] == "*":
                my_finals.append(k[1:])
    my_finals = list(set(my_finals))
    contents2=contents[2:]
    for i in range(len(contents2)):
        contents2[i] = contents2[i].replace("->", "")
        contents2[i] = contents2[i].replace("*", "")
    my_trans=[]
    for i in contents2:
        my_trans.append(i.split(','))
    my_states=[]
    for i in my_trans:
        my_states.append(i[0])
        my_states.append(i[2])
    my_states = list(set(my_states))
    q = my_states.index(my_init)
    my_states[0], my_states[q] = my_states[q], my_states[0]
    NFA(my_states,my_alph,my_init,my_trans,my_statesNO,my_finals)
    # print(my_alph,my_finals,my_init,my_statesNO,my_states,my_trans)