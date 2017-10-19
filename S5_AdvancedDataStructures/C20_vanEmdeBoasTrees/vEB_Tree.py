class vEB_Tree():
    import math
    def __init__(self, u):
        self.min = None
        self.max = None
        self.u = u
        self.summary = None
        self.ul = math.floor(math.sqrt(self.u))
        self.uh = math.ceil(math.sqrt(self.u))
        #self.cluster = [None] * self.uh
        if not self.is_leaf():
            self.summary = vEB_Tree(self.uh)
            self.cluster = []
            for x in xrange(self.uh):
                self.cluster.append(vEB_Tree(self.ul))

    def is_leaf(self):
        return self.u == 2

    def high(self, x):
        return math.floor(x/self.ul)

    def low(self, x):
        return int(x) % self.ul

    def index(self, x, y):
        return x*self.ul + y

    def minimum(self):
        return self.min

    def maximum(self):
        return self.max

    def member(self, x):
        if x == self.min or x == self.max:
            return True
        elif self.u == 2:
            return False
        else:
            return self.member(self.cluster[self.high(x)], self.low(x))

    def successor(self, x):
        if self.u == 2:
            if x == 0 and self.max == 1:
                return 1
            else:
                return None
        elif self.min != None and x < self.min:
            return self.min
        else:
            max_low = self.maximum(self.cluster[self.high(x)])
            if max_low != None and self.low(x) < max_low:
                offset = self.successor(self.cluster[self.high(x)], self.low(x))
                return self.index(self.high(x), offset)
            else:
                succ_cluster = self.successor(self.summary, self.high(x))
                if succ_cluster == None:
                    return None
                else:
                    offset = self.minimum(self.cluster[succ_cluster])
                    return self.index(succ_cluster, offset)

    def empty_tree_insert(self, x):
        self.min = x
        self.max = x

    def insert(self, x):
        if self.min == None:
            self.empty_tree_insert(x)
        else:
            if x < self.min:
                self.min, x = x, self.min
            if self.u > 2:
                if self.minimum(self.cluster[self.high(x)]) == None:
                    self.insert(self.summary, self.high(x))
                    self.empty_tree_insert(self.cluster[self.high(x)], self.low(x))
                else:
                    self.insert(self.cluster[self.high(x)], self.low(x))
            if x > self.max:
                self.max = x

    def delete(self, x):
        if self.min == self.max:
            self.min = None
            self.max = None
        elif self.u == 2:
            if x == 0:
                self.min = 1
            else:
                self.min = 0
            self.max = self.min
        else:
            if x == self.min:
                first_cluster = self.minimum(self.summary)
                x = self.index(first_cluster, self.minimum(self.cluster[first_cluster]))
                self.min = x
            self.delete(self.cluster[self.high(x)], self.low(x))
            if self.minimum(self.cluster[self.high(x)]) == None:
                self.delete(self.summary, self.high(x))
                if x == self.max:
                    summary_max = self.maximum(self.summary)
                    if summary_max == None:
                        self.max = self.min
                    else:
                        self.max = self.index(summary_max, self.maximum(self.cluster[summary_max]))
            elif x == self.max:
                self.max = self.index(self.high(x), self.maximum(self.cluster[self.high(x)]))
