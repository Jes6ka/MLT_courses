



#get depth of list
#https://stackoverflow.com/questions/30427268/on-finding-the-maximum-depth-of-an-arbitrarily-nested-list
def depthCount(x, depth=0):
    if not x or not isinstance(x, list):
        return depth
    return max(depthCount(x[0], depth+1),
               depthCount(x[1:], depth))
