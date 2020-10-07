#UnionFind(Disjoint Set Union) structure in Python
#Author : yadavnaman
class UnionFind:

    def __init__(self):
        """Create a new empty union-find class."""
        self.size = {}
        self.parents = {}

    def find(self, object):
        #find the disjoint set in which object is present

        # if object is not yet called by union method, the set consists of only the current object
        if object not in self.parents:
            self.size[object] = 1
            self.parents[object] = object
            return object
       
        # compressing the path(improves time complexity)
        parent = self.parents[object]
        if object != parent:
            parent = find(parent)

        return parent
        

    def union(self, object1, object 2):
        #Merge the sets according to size
        par_1 = find(object1)
        par_2 = find(object2)
        if(par_1 != par_2):
            if self.size[par_1] > self.size[par_2]:
                self.parents[par_2] = par_1
                self.size[par_1] += self.size[par_2]

            else:
                self.parents[par_1] = par_2
                self.size[par_2] += self.size[par_1]
        
