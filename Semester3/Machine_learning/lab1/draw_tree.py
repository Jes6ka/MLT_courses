node_collection = [('attr2', 'sp2', 1.6373326057329134, 0),
                   ('attr2', 'sp1', 0.545663100388463, 1),
                   ('attr3', 'sp5', 2.245804529802605, 2),
                   ('terminal', 'terminal', -7777, 3),
                   ('terminal', 'terminal', -7777, 4),
                   ('attr3', 'sp1', 2.065308108672463, 5),
                   ('terminal', 'terminal', -7777, 6),
                   ('terminal', 'terminal', -7777, 7),
                   ('attr2', 'sp2', 2.5888773127155993, 8),
                   ('attr3', 'sp5', 3.7949417141146546, 9),
                   ('terminal', 'terminal', -7777, 10),
                   ('terminal', 'terminal', -7777, 11),
                   ('attr3', 'sp5', 4.5311631058202053, 12),
                   ('terminal', 'terminal', -7777, 13),
                   ('terminal', 'terminal', -7777, 14)]

linking_tree_leaf_list = []


nat = Node_and_Terminal = []
already_used = 0
for attr, sp, sp_v, n_o in node_collection:
        if sp=="terminal":   nat.append([n_o, "terminal", already_used])
        else : nat.append([n_o, "node", already_used])

def fill_nodes(Master=0, Slave=1, Last_Slave = "ghost"): # fill_nodes(node_collection)
    global nat
    
    nat[Master][2] += 1
    
    if Last_Slave == "terminal" and nat[Slave][1] == "terminal":
        if nat[Master][2]==3: 
            print("QuQUQU")
            fill_nodes(Master=Master-1,Slave= Slave, Last_Slave = "ghost")
        print(Master, '->kk ', Slave,nat[Master], nat[Slave])
        linking_tree_leaf_list.append(Master, Slave])
        fill_nodes(Master=Master-1,Slave= Slave+1, Last_Slave = "ghost")
        
    if nat[Master][1]=="terminal":
            
        print(Master, '->ee ', Slave,nat[Master], nat[Slave])
        linking_tree_leaf_list.append(Master, Slave])
        fill_nodes(Master=Master-1,Slave= Slave, Last_Slave = nat[Slave][1])

        print(Master, '->dd ', Slave,nat[Master], nat[Slave])
        linking_tree_leaf_list.append(Master, Slave])
        fill_nodes(Master=Master-1, Slave=Slave+1, Last_Slave = nat[Slave][1])
    
    if nat[Slave][1] == "node" :
        
        if nat[Master][2] == 3: 

            print(Master, '->aa ', Slave,nat[Master], nat[Slave])
            linking_tree_leaf_list.append(Master, Slave])
            fill_nodes(Master=Master-1, Slave = Slave, Last_Slave = nat[Slave][1])

        print(Master, '->bb ', Slave,nat[Master], nat[Slave])
        linking_tree_leaf_list.append(Master, Slave])
        fill_nodes(Master = Slave, Slave = Slave+1, Last_Slave = nat[Slave][1])

    else : 
        if nat[Master][2] == 3 :
            fill_nodes(Master=Master-1, Slave=Slave, Last_Slave = nat[Slave][1])
            
        print(Master, '->cc ', Slave,nat[Master], nat[Slave])
        linking_tree_leaf_list.append(Master, Slave])
        fill_nodes(Master = Master, Slave = Slave+1, Last_Slave = nat[Slave][1])

print(nat)
try : fill_nodes()
except : pass
"""
0 ->bb  1 [0, 'node', 1] [1, 'node', 0]
1 ->bb  2 [1, 'node', 1] [2, 'node', 0]
2 ->cc  3 [2, 'node', 1] [3, 'terminal', 0]
2 ->kk  4 [2, 'node', 2] [4, 'terminal', 0]
1 ->bb  5 [1, 'node', 2] [5, 'node', 0]
5 ->cc  6 [5, 'node', 1] [6, 'terminal', 0]
5 ->kk  7 [5, 'node', 2] [7, 'terminal', 0]
4 ->ee  8 [4, 'terminal', 1] [8, 'node', 0]
3 ->ee  8 [3, 'terminal', 1] [8, 'node', 0]
2 ->aa  8 [2, 'node', 3] [8, 'node', 0]
1 ->aa  8 [1, 'node', 3] [8, 'node', 0]
0 ->bb  8 [0, 'node', 2] [8, 'node', 0]
8 ->bb  9 [8, 'node', 1] [9, 'node', 0]
9 ->cc  10 [9, 'node', 1] [10, 'terminal', 0]
9 ->kk  11 [9, 'node', 2] [11, 'terminal', 0]
8 ->bb  12 [8, 'node', 2] [12, 'node', 0]
12 ->cc  13 [12, 'node', 1] [13, 'terminal', 0]
12 ->kk  14 [12, 'node', 2] [14, 'terminal', 0]
"""

from graphviz import Graph
g = Graph(format='png')



from graphviz import Digraph
dot = Digraph(comment='The Round Table')

dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')

# render()-method to save the source code and render it 
dot.render('test-output/round-table.gv', view=True)  


#http://graphviz.readthedocs.io/en/stable/examples.html
#best example,

from graphviz import Digraph
from graphviz import Digraph

f = Digraph('finite_state_machine', filename='fsm.gv')
f.attr(rankdir='LR', size='8,5')

f.attr('node', shape='doublecircle')
f.node('LR_0')
f.node('LR_3')
f.node('LR_4')
f.node('LR_8')

f.attr('node', shape='circle')
f.edge('LR_0', 'LR_2', label='SS(B)')
f.edge('LR_0', 'LR_1', label='SS(S)')
f.edge('LR_1', 'LR_3', label='S($end)')
f.edge('LR_2', 'LR_6', label='SS(b)')
f.edge('LR_2', 'LR_5', label='SS(a)')
f.edge('LR_2', 'LR_4', label='S(A)')
f.edge('LR_5', 'LR_7', label='S(b)')
f.edge('LR_5', 'LR_5', label='S(a)')
f.edge('LR_6', 'LR_6', label='S(b)')
f.edge('LR_6', 'LR_5', label='S(a)')
f.edge('LR_7', 'LR_8', label='S(b)')
f.edge('LR_7', 'LR_5', label='S(a)')
f.edge('LR_8', 'LR_6', label='S(b)')
f.edge('LR_8', 'LR_5', label='S(a)')

f.view()



"""
http://graphviz.readthedocs.io/en/stable/manual.html
http://www.webgraphviz.com/
digraph g{
node[shape=box];
0[label="attr1\nX<=3.4432(sp3)"];
1[label="leaf1"];
2[label="leaf2"];
3[label="leaf3"];
4[label="leaf4"];
0 -> 1[labeldistance=2, labelangle=45, headlabel="Yes"];
0 -> 2[labeldistance=2, labelangle=45, headlabel="No"];
2 -> 3[labeldistance=2, labelangle=45, headlabel="No"];
0 -> 4[labeldistance=2, labelangle=45, headlabel="No"];
}
"""



##### ============ Final Version, Working perfect ====================

node_collection = [('attr2', 'sp2', 1.6373326057329134, 0),
                   ('attr2', 'sp1', 0.545663100388463, 1),
                   ('attr3', 'sp5', 2.245804529802605, 2),
                   ('terminal', 'terminal', -7777, 3),
                   ('terminal', 'terminal', -7777, 4),
                   ('attr3', 'sp1', 2.065308108672463, 5),
                   ('terminal', 'terminal', -7777, 6),
                   ('terminal', 'terminal', -7777, 7),
                   ('attr2', 'sp2', 2.5888773127155993, 8),
                   ('attr3', 'sp5', 3.7949417141146546, 9),
                   ('terminal', 'terminal', -7777, 10),
                   ('terminal', 'terminal', -7777, 11),
                   ('attr3', 'sp5', 4.5311631058202053, 12),
                   ('terminal', 'terminal', -7777, 13),
                   ('terminal', 'terminal', -7777, 14)]

node_collection2 = [('attr2', 'sp2', 1.6373326057329134, 0),
                   ('attr2', 'sp1', 0.545663100388463, 1),
                   ('attr3', 'terminal', 2.245804529802605, 2),
                   ('terminal', 'sp2', -7777, 3),
                   ('terminal', 'sp2', -7777, 4),
                   ('attr3', 'terminal', 2.065308108672463, 5),
                   ('terminal', 'terminal', -7777, 6),
                   ('terminal', 'terminal', -7777, 7),
                   ('attr2', 'sp2', 2.5888773127155993, 8),
                   ('attr3', 'terminal', 3.7949417141146546, 9),
                   ('terminal', 'terminal', -7777, 10)]

linking_tree_leaf_list = []

nat = Node_and_Terminal = []
already_used = 0
for attr, sp, sp_v, n_o in node_collection:
        if sp=="terminal":   nat.append([n_o, "terminal", already_used])
        else : nat.append([n_o, "node", already_used])

def fill_nodes(Master=0, Slave=1, Last_Slave = "ghost"): # fill_nodes(node_collection)
    global nat
    
    nat[Master][2] += 1
    
    if Last_Slave == "terminal" and nat[Slave][1] == "terminal":
        print(Master, '->kk ', Slave,nat[Master], nat[Slave])
        linking_tree_leaf_list.append(Master, Slave])
        fill_nodes(Master=Master-1,Slave= Slave+1, Last_Slave = "ghost")
        
    if nat[Master][1]=="terminal":
    
        #print(Master, '->ee ', Slave,nat[Master], nat[Slave])
        linking_tree_leaf_list.append(Master, Slave])
        fill_nodes(Master=Master-1,Slave= Slave, Last_Slave = nat[Slave][1])

    if nat[Slave][1] == "node" :
        
        if nat[Master][2] == 3: 

            #print(Master, '->aa ', Slave,nat[Master], nat[Slave])
            fill_nodes(Master=Master-1, Slave = Slave, Last_Slave = nat[Slave][1])

        print(Master, '->bb ', Slave,nat[Master], nat[Slave])
        linking_tree_leaf_list.append(Master, Slave])
        fill_nodes(Master = Slave, Slave = Slave+1, Last_Slave = nat[Slave][1])

    else : 
        if nat[Master][2] == 3 :
            fill_nodes(Master=Master-1, Slave=Slave, Last_Slave = nat[Slave][1])
            
        print(Master, '->cc ', Slave,nat[Master], nat[Slave])
        linking_tree_leaf_list.append(Master, Slave])
        fill_nodes(Master = Master, Slave = Slave+1, Last_Slave = nat[Slave][1])

print(nat)
try : fill_nodes()
except : pass
