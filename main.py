
class DFA :

    def __init__(self ,states,alphabet,initial,trans_func ,state_num, finals):
        self.state_num=state_num
        self.states=states
        self.alphabet=alphabet
        self.initial=initial
        self.finals=finals
        self.trans_func = trans_func
        self.to_dic()

    def to_dic(self):
        my_dfa={}
        my_dfa["states"] = self.states
        my_dfa["state_num"] = self.state_num
        my_dfa["alphabet"] = self.alphabet
        my_dfa["func"]=self.trans_func
        my_dfa["initial"]=self.initial
        my_dfa["finals"]=self.finals
        print("DFA Done.")

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
        self.To_DFA()

    def To_DFA(self):
        landa=[]
        for i in self.states:
            a=[]
            a.append(i)
            landa.append(a)
        for i in range(len(landa)):
            for k in landa[i]:
                for j in self.trans_func:
                    if k == j[0]:
                        if j[1]== '_':
                            landa[i].append(j[2])

        # landa is our new self.states
        closure=[[landa[0] ,]]
        for i in closure:
            for a in range(len(self.alphabet)):
                i.append([])
                p=i[0]
                for j in p:
                    for k in self.trans_func:
                        if k[0] == j:
                            if k[1] == self.alphabet[a]:
                                k2=self.new_state_finder(k[2],landa)
                                for item in k2:
                                    i[a + 1].append(item)
                    i[a+1]=list(set(i[a+1]))
                    i[a+1]=sorted(i[a+1])
                # print(i)
                flag = True
                for t in closure:
                    if i[a+1] == t[0]:
                        flag=False
                        break
                if flag==True:
                    if i[a+1]!=[]:
                        closure.append([i[a+1]])
        self.finishing_checker(landa,closure)

    def new_state_finder(self,k2,landa):
        out=[]
        tmp=[]
        for ele in landa:
            if k2 in ele:
                tmp.append(ele)
        for li in tmp:
            for item in li:
                out.append(item)
        return out

    def finishing_checker(self,landa,closure):
        new_closure=closure
        flag=False
        inn = False
        for li in landa:
            for lis in closure:
                if flag ==True:
                    inn = True
                    break
                for state in li:
                    if state in lis[0]:
                        flag=True
            if inn == False:
                new_closure.append([li,])


        if new_closure != closure:
            for i in range(len(closure),len(new_closure)):
                for a in range(len(self.alphabet)):
                    new_closure[i].append([])
                    p = new_closure[i][0]
                    for j in p:
                        for k in self.trans_func:
                            if k[0] == j:
                                if k[1] == self.alphabet[a]:
                                    k2 = self.new_state_finder(k[2], landa)
                                    for item in k2:
                                        new_closure[i][a + 1].append(item)
                        new_closure[i][a + 1] = list(set(new_closure[i][a + 1]))
                        new_closure[i][a + 1] = sorted(new_closure[i][a + 1])
                    # print(i)
                    flag = True
                    for t in new_closure:
                        if new_closure[i][a + 1] == t[0]:
                            flag = False
                            break
                    if flag == True:
                        if new_closure[i][a + 1] != []:
                            new_closure.append([new_closure[i][a + 1]])

        # print(landa)
        # print(new_closure)
        self.dfa_constructor(new_closure)

    def dfa_constructor(self,closure):
        d_states= []
        d_stat = []
        state_dic={}
        for i in closure:
            d_stat.append(i[0])
        # print(d_stat)
        for i in range(len(d_stat)):
            d_states.append("q%d" %i)
            state_dic[str(d_stat[i])]=d_states[i]
        d_init =d_states[0]
        d_final=[]
        d_finals= []
        for li in d_stat:
            for item in self.finals:
                if item in li:
                    d_final.append(li)
        for i in d_final:
            a=d_stat.index(i)
            d_finals.append("q%d" %a)
        d_statesNO=len(d_states)
        d_alphabet=self.alphabet
        for i in closure:
            for j in range(len(i)):
                if i[j]!=[]:
                    i[j]=state_dic[str(i[j])]
        d_trans=[]
        for statee in closure:
            for alph in range(len(self.alphabet)):
                d_trans.append([statee[0],self.alphabet[alph],statee[alph+1]])

        print(d_init,d_states,d_finals,d_statesNO,d_alphabet,d_trans)
        DFA(d_states,d_alphabet,d_init,d_trans,d_statesNO,d_finals)
        # print(self.trans_func)
        # print(closure)


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