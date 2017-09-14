node_collection = [('attr2', 'sp2', 1.6373326057329134, 0),
                   ('attr2', 'sp1', 0.545663100388463, 1),
                   ('attr3', 'sp5', 2.245804529802605, 2),
                   ('terminal', 'terminal', -7777, 3),
                   ('terminal', 'terminal', -7777, 4),
                   ('attr3', 'sp1', 2.065308108672463, 5),
                   ('terminal', 'terminal', -7777, 6)('terminal', 'terminal', -7777, 7)('attr2', 'sp2', 2.5888773127155993, 8)('attr3', 'sp5', 3.7949417141146546, 9)('terminal', 'terminal', -7777, 10)('terminal', 'terminal', -7777, 11)('attr3', 'sp5', 4.5311631058202053, 12)('terminal', 'terminal', -7777, 13)('terminal', 'terminal', -7777, 14)]


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
MOM = Master_of_Master = 0
Master, Slave = int(), int()
nat = Node_and_Terminal = []
already_used = 0
for attr, sp, sp_v, n_o in node_collection:
        if sp=="terminal":   nat.append([n_o, "terminal", already_used])
        else : nat.append([n_o, "node", already_used])

def fill_nodes(MOM=0): # fill_nodes(node_collection)
    #global nat
    Master = MOM
    Slave  = Master+1
    nat[Master][2] += 1#already used +1
    if nat[Master][1] == True : return("go to next")
    if nat[Slave][1] == "node" :
        Master = Slave
    else : 
        Master = Master
    
    Slave  = Slave+1
    print(Master, '->', Slave)
    fill_nodes(MOM=Master)

fill_nodes()


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
