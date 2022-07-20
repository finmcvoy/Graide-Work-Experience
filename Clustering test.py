from cluster import HierarchicalClustering
data = [12,34,23,32,46,96,13]
cl = HierarchicalClustering(data, lambda x,y: abs(x-y))
cl.getlevel(10)     # get clusters of items closer than 10
cl.getlevel(5)      # get clu

print(cl.getlevel(5))
