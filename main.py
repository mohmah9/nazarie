
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

        file = open("output.txt" , "w")
        file.write(str(self.state_num))
        file.write("\n")
        for i in self.alphabet:
            file.write(i)
            file.write(",")
        file.write("\n")
        file.write("->")
        for i in self.trans_func:
            if i[0] in self.finals:
                file.write("*")
            file.write(i[0])
            file.write(",")
            file.write(i[1])
            file.write(",")
            if i[2] in self.finals:
                file.write("*")
            file.write(i[2])
            file.write("\n")
        file.write("\n")
        file.write("\n")
        file.close()
        self.minimization(my_dfa["states"])

    def minimization(self,nodes):
        nodes2 =nodes.copy()
        matrix=[]
        for i in nodes2:
            matrix.append([])
        for i in range(len(nodes2)):
            for j in range(len(self.alphabet)):
                matrix[i].append([])
        for i in range(len(nodes2)):
            nodes2[i]=[nodes2[i]]
        # for i in range(len(self.alphabet)):
        #     for j in range(len(nodes2)):
        #         matrix[j][i]=self.node_finder(self.alphabet[i],nodes2[j])
        non_omiting=[self.initial]
        for i in range(1,len(self.states)):
            for j in matrix:
                if self.states[i] in j:
                    non_omiting.append(self.states[i])
                    break
        for i in nodes:
            if i not in non_omiting:
                nodes2.remove([i])  #removing unreachable
        first=[[]]
        for i in self.states:
            if i not in self.finals:
                first[0].append(i)
        first.append(self.finals)
        # print(first)
        for i in range(len(self.alphabet)):
            for j in range(len(nodes)):
                matrix[j][i]=self.node_finder(self.alphabet[i],nodes[j],first)
        # print(matrix)
        # print(nodes)
        self.minimization2(nodes,first,matrix)
    def minimization2(self,nodes,first,matrix):
        nodes2=nodes.copy()
        second=[]
        temp=[]
        for i in matrix:
            j=self.duplicates(matrix,i)
            for k in range(len(j)):
                j[k]="q%d" %j[k]
            if j not in temp:
                temp.append(j)
        second=temp
        # print(matrix)
        # print(second)
        if second!= first:
            for i in range(len(self.alphabet)):
                for j in range(len(nodes)):
                    matrix[j][i] = self.node_finder(self.alphabet[i], nodes[j], second)
            self.minimization2(nodes,second,matrix)
        else:
            for i in range(len(self.alphabet)):
                for j in range(len(nodes)):
                    matrix[j][i] = self.node_finder(self.alphabet[i], nodes[j], second)
            self.minimize_final(nodes,second,matrix)
    def minimize_final(self,nodes,first,matrix):
        second=[]
        temp=[]
        for i in matrix:
            j=self.duplicates(matrix,i)
            for k in range(len(j)):
                j[k]="q%d" %j[k]
            if j not in temp:
                temp.append(j)
        second=temp
        # print(matrix)
        # print(second)

        d_states=[]
        state_dic={}
        matrix2=[]
        for i in second:
            matrix2.append(matrix[int(i[0][1:])])
        matrix=matrix2
        for i in range(len(second)):
            d_states.append("g%d" %i)
            state_dic[str(second[i])]=d_states[i]
        for i in second :
            if self.initial in i:
                d_init=state_dic[str(i)]
        d_finals=[]
        for i in self.finals:
            for j in second:
                if i in j:
                    d_finals.append(state_dic[str(j)])
        d_stateNO=len(d_states)
        d_alph=self.alphabet
        for i in matrix:
            for j in range(len(i)):
                i[j]=state_dic[str(i[j])]
        # print(matrix)
        d_trans=[]
        for i in range(len(d_states)):
            for j in range(len(d_alph)):
                d_trans.append([d_states[i],d_alph[j],matrix[i][j]])
        print(d_states,d_init,d_finals,d_stateNO,d_alph,d_trans)
        print("Minimization Done")
        self.print_min(d_states,d_init,d_finals,d_stateNO,d_alph,d_trans)
    def print_min(self,d_states,d_init,d_finals,d_stateNO,d_alph,d_trans):
        file = open("output.txt" , "a+")
        file.write(str(d_stateNO))
        file.write("\n")
        for i in d_alph:
            file.write(i)
            file.write(",")
        file.write("\n")
        file.write("->")
        for i in d_trans:
            if i[0] in d_finals:
                file.write("*")
            file.write(i[0])
            file.write(",")
            file.write(i[1])
            file.write(",")
            if i[2] in d_finals:
                file.write("*")
            file.write(i[2])
            file.write("\n")
        file.close()
    def node_finder(self,alph,node,first):
        for i in self.trans_func:
            if i[0] == node:
                if i[1] == alph:
                    for j in first:
                        if i[2] in j:
                            return j

    def duplicates(self,lst, item):
        return [i for i, x in enumerate(lst) if x == item]

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