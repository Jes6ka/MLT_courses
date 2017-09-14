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
