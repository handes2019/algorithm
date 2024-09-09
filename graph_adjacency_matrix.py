class GraphAdjMat:
    """基於鄰接矩陣實現的無向圖類"""
    def __init__(self, vertices: list[int], edges: list[list[int]]):
        """構造方法"""
        # 頂點列表，元素代表“頂點值”，索引代表“頂點索引”
        self.vertices: list[int] = []
        # 鄰接矩陣， 行列索引對應“頂點索引"
        self.adj_mat: list[list[int]] = []
        # 添加頂點
        for val in vertices:
            self.add_vertex(val)
        # 添加邊
        # 請注意，edges  元素代表頂點索引，即對應 vertices 元素索引
        for e in edges:
            self.add_edge(e[0],e[1])
    def size(self) -> int:
        """獲取頂點數量"""
        return len(self.vertices)
    def add_vertex(self, val: int):
        """添加頂點"""
        n = self.size()
        # 向頂點列表中添加新頂點的值
        self.vertices.append(val)
        # 在鄰接矩陣中添加一行
        for row in self.adj_mat:
            row.append(0)
    def remove_vertex(self, index: int):
        """刪除頂點"""
        if index >= self.size():
            raise IndexError()
        # 在頂點列表中移除索引 index 的頂點
        self.vertices.pop(index)
        # 在鄰接矩陣中刪除索引 index 的行
        self.adj_mat.pop(index)
        # 在鄰接矩陣中刪除索引 index 的列
        for row in self.adj_mat:
            row.pop(index)
    def add_edge(self, i: int,j: int):
        """添加邊"""
        # 參數 i,j 對應 vertices 元素索引
        # 索引越界與相等處理
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        # 在無向圖中，鄰接矩陣關於主對角線對稱，即滿足(i, j) == (j, i)
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1
    def remove_edge(self, i:int, j: int):
        """刪除邊"""
        # 參數 i,j 對應 vertices 元素索引
        # 索引越界與相等處理
        if i <0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0
        
    def print(self):
        """打印鄰接矩陣"""
        print("頂點列表 =", self.vertices)
        print("鄰接矩陣 =")
        # print_matrix(self.adj_mat)
        
"""Driver Code"""
if __name__ == "__main__":
    # 初始化無向圖
    vertices = [1,3,2,5,4]
    edges = [[0,1],[0,3],[1,2],[2,3],[2,4],[3,4]]
    graph = GraphAdjMat(vertices,edges)
    
    
    # 添加邊
    # 頂點 1， 2 的索引分別為 0， 2
    graph.add_edge(0,2)
    
    # 刪除邊
    # 頂點 1，3 的索引分別為0，1
    graph.remove_edge(0,1)
    
    # 添加頂點
    graph.add_vertex(6)
    
    # 刪除頂點
    # 頂點 3 的索引為 1
    graph.remove_vertex(1)