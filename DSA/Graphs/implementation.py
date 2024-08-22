class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.dic={}
        for start,end in edges:
            if start in self.dic:
                self.dic[start].append(end)
            else:
                self.dic[start]=[end]

    def getPath(self,start,end,history=[]):
        history=history+[start]
        if start==end:
            return [history]
        if start not in self.dic:
            return []
        else:
            pathChoices=[]
            for stops in self.dic[start]:
                if stops not in history:
                    choices=self.getPath(stops,end,history)
                    for item in choices:
                        pathChoices.append(item)
            return pathChoices


if __name__=="__main__":
    routes=[
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Dubai","New York"),
        ("Paris","New York"),
        ("New York","Toronto"),
    ]

    g=Graph(routes)

    print(g.getPath("Mumbai","Toronto"))