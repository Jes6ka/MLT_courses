#what i have
#[ [0,1,attr,sp],
#  [1,2,attr,sp] ... ]


def predict(line, node_relation, node_collection, flag=0):
	if node_collection[flag][1] == "terminal": return(most.common)

	parent, child, attr, sp = node_relation[flag]
		if line[int(attr[-1])-1] <= sp:
			predict(line, node_relation, flag=c)
		else :
			for m,c,attr,sp in node_relation[flag:]:
				if m==flag:
					predict(line, node_relation, flag=c)

	return(predict_class)
