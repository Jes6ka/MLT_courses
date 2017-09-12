# imagine, I have best IG node.
# which is (attr2, sp3)
# then I need (attr2, sp3) tuple first.

# split raw_data -> raw_data1, raw_data2.

NODE_COLLECTION = []

raw_data = {'data' : [[1,2,3],[5,6,7],[8,9,10]]}
for each_line in raw_data['data']:
    print(each_line)
    
from collections import defaultdict
def split_raw_data_by_node(raw_data, node):
	#node = ((attr=2) , (sp3=293))
	#attr, sp = tuple([int(w[-1])-1 for w in node ])
	
	NODE_COLLECTION.append(node)

	attr, sp = node 	#attr-1 is necessary. because that's what I defined
	attr-=1

	raw_data1 = defaultdict(list)
	raw_data2 = defaultdict(list)
    
	for each_line in raw_data['data']:
		print(raw_data['data'][attr], attr, sp)
		if each_line[attr]<=sp:
			raw_data1['data'].append(each_line)
		else : raw_data2['data'].append(each_line)
		
	return raw_data1, raw_data2


"""
r1, r2 = split_raw_data_by_node(raw_data, (2,5))
print(r1, '/n', r2)
[5, 6, 7] 1 5
[5, 6, 7] 1 5
[5, 6, 7] 1 5
defaultdict(<class 'list'>,
	{'data': [[1, 2, 3]]})
defaultdict(<class 'list'>,
 {'data': [[5, 6, 7], [8, 9, 10]]})
 """

#so, now have to put raw_data1, raw_data2 as if raw_data
