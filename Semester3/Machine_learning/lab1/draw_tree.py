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
#MOM = Master_of_Master = 0
#Master, Slave = int(), int()
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
        fill_nodes(Master=Master-1,Slave= Slave+1, Last_Slave = "ghost")
        
    if nat[Master][1]=="terminal":
            
        print(Master, '->ee ', Slave,nat[Master], nat[Slave])
        fill_nodes(Master=Master-1,Slave= Slave, Last_Slave = nat[Slave][1])

        print(Master, '->dd ', Slave,nat[Master], nat[Slave])
        fill_nodes(Master=Master-1, Slave=Slave+1, Last_Slave = nat[Slave][1])
    
    if nat[Slave][1] == "node" :
        
        if nat[Master][2] == 3: 

            print(Master, '->aa ', Slave,nat[Master], nat[Slave])
            fill_nodes(Master=Master-1, Slave = Slave, Last_Slave = nat[Slave][1])

        print(Master, '->bb ', Slave,nat[Master], nat[Slave])
        fill_nodes(Master = Slave, Slave = Slave+1, Last_Slave = nat[Slave][1])

    else : 
        if nat[Master][2] == 3 :
            fill_nodes(Master=Master-1, Slave=Slave, Last_Slave = nat[Slave][1])
            
        print(Master, '->cc ', Slave,nat[Master], nat[Slave])
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


#http://graphviz.readthedocs.io/en/stable/examples.html#btree-py
#best example,

from graphviz import Digraph

g = Digraph('g', filename='btree.gv', node_attr={'shape': 'record', 'height': '.1'})

g.node('node0', '<f0> |<f1> G|<f2> ')
g.node('node1', '<f0> |<f1> E|<f2> ')
g.node('node2', '<f0> |<f1> B|<f2> ')
g.node('node3', '<f0> |<f1> F|<f2> ')
g.node('node4', '<f0> |<f1> R|<f2> ')
g.node('node5', '<f0> |<f1> H|<f2> ')
g.node('node6', '<f0> |<f1> Y|<f2> ')
g.node('node7', '<f0> |<f1> A|<f2> ')
g.node('node8', '<f0> |<f1> C|<f2> ')

g.edge('node0:f2', 'node4:f1')
g.edge('node0:f0', 'node1:f1')
g.edge('node1:f0', 'node2:f1')
g.edge('node1:f2', 'node3:f1')
g.edge('node2:f2', 'node8:f1')
g.edge('node2:f0', 'node7:f1')
g.edge('node4:f2', 'node6:f1')
g.edge('node4:f0', 'node5:f1')

g.view()



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



#backup

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
#MOM = Master_of_Master = 0
#Master, Slave = int(), int()
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
        fill_nodes(Master=Master-1,Slave= Slave+1, Last_Slave = "ghost")
        
    if nat[Master][1]=="terminal":
    
        #print(Master, '->ee ', Slave,nat[Master], nat[Slave])
        fill_nodes(Master=Master-1,Slave= Slave, Last_Slave = nat[Slave][1])

    if nat[Slave][1] == "node" :
        
        if nat[Master][2] == 3: 

            #print(Master, '->aa ', Slave,nat[Master], nat[Slave])
            fill_nodes(Master=Master-1, Slave = Slave, Last_Slave = nat[Slave][1])

        print(Master, '->bb ', Slave,nat[Master], nat[Slave])
        fill_nodes(Master = Slave, Slave = Slave+1, Last_Slave = nat[Slave][1])

    else : 
        if nat[Master][2] == 3 :
            fill_nodes(Master=Master-1, Slave=Slave, Last_Slave = nat[Slave][1])
            
        print(Master, '->cc ', Slave,nat[Master], nat[Slave])
        fill_nodes(Master = Master, Slave = Slave+1, Last_Slave = nat[Slave][1])

print(nat)
try : fill_nodes()
except : pass
