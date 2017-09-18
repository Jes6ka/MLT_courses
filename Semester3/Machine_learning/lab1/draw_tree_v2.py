node_relation_list = []
nat = Node_and_Terminal = []
already_used = 0


def fill_nodes(Master=0, Slave=1, Last_Slave = "ghost", already_used=False): # fill_nodes(node_collection)
    global nat
    
    if not already_used : nat[Master][2] += 1
    
    if Last_Slave == "terminal" and nat[Slave][1] == "terminal":
        if nat[Master][2] >= 3 :
            print(Master, '->@@@ ', Slave,nat[Master], nat[Slave])
            fill_nodes(Master=Master-1, Slave=Slave, Last_Slave = nat[Slave][1])
        print(Master, '->kk ', Slave,nat[Master], nat[Slave])
        node_relation_list.append((Master, Slave, nat[Master][3], nat[Master][4]))
        fill_nodes(Master=Master-1,Slave= Slave+1, Last_Slave = "ghost")
        
    if nat[Master][1]=="terminal":
    
        #print(Master, '->ee ', Slave,nat[Master], nat[Slave])
        print(Master, '->&&& ', Slave,nat[Master], nat[Slave])
        fill_nodes(Master=Master-1,Slave= Slave, Last_Slave = nat[Slave][1], already_used=False)

    if nat[Slave][1] == "node" :
        
        if nat[Master][2] >= 3: 
            print(Master, '->*** ', Slave,nat[Master], nat[Slave])
            #print(Master, '->aa ', Slave,nat[Master], nat[Slave])
            fill_nodes(Master=Master-1, Slave = Slave, Last_Slave = nat[Slave][1], already_used=False)

        print(Master, '->bb ', Slave, nat[Master], nat[Slave])
        node_relation_list.append((Master, Slave, nat[Master][3], nat[Master][4]))
        fill_nodes(Master = Slave, Slave = Slave+1, Last_Slave = nat[Slave][1])

    else : 
        if nat[Master][2] >= 3 :
            print(Master, '->*** ', Slave,nat[Master], nat[Slave])
            fill_nodes(Master=Master-1, Slave=Slave, Last_Slave = nat[Slave][1])
            
        print(Master, '->cc ', Slave,nat[Master], nat[Slave])
        node_relation_list.append((Master, Slave, nat[Master][3], nat[Master][4]))
        fill_nodes(Master = Master, Slave = Slave+1, Last_Slave = nat[Slave][1])


#print(nat)
#(attr, sp, IG, stamp+1, status)
def make_tree(node_collection):
  for attr, sp, IG, node_order, status in node_collection:
        if sp=="terminal":   nat.append([node_order, "terminal", already_used, attr, sp, status])
        else : nat.append([node_order, "node", already_used, attr, sp, status])
  try : fill_nodes()
  except : pass
  print('\n',node_relation_list,'\n')


def draw_tree_graphviz(node_relation_list, node_collection):
    from graphviz import Digraph
    f = Digraph('decision_tree', filename='ID3.gv')
    f.attr('node', shape='square')
    node_list = []
    for attr, sp, IG, node_order, status in node_collection:
      if isinstance(attr, tuple):
        most_common, freq = attr
        node_list.append('node'+str(node_order)+'\n'+str(most_common)+'\n'+ str(sp))#cannot add str(status), graphviz doesn't support long name

      else:
        node_list.append('node'+str(node_order)+'\n'+str(attr)+ '\n'+ str(sp))#cannot add str(status), graphviz doesn't support long name

    f.attr('node', shape='square')
    for mom, child, attr, sp in node_relation_list:
        if mom == child-1 :
          f.edge(node_list[mom], node_list[child], label='small')
        else : 
          f.edge(node_list[mom], node_list[child], label='big')

        #, label = str(attr)+'\n'+str(sp)

    f.view()
    return("Successful to draw the tree")

