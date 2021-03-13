'''
深度优先遍历： 是一种用于遍历树或者图的算法。沿着树的深度遍历树的节点，尽可能深地搜索树的分支。
            当节点v的所在边都被搜索过了。搜索将回溯到节点v的那条边的起始节点。
            这一过程已知进行，直到已发现从源节点可达的所有节点为止。
            如果还存在未发现的节点，则选择其中一个作为源节点并重复上述过程，整个进程反复进行直到所有节点都被访问为止
            属于盲目搜索
bfs
            从根节点开始，沿着树的宽度遍历树的节点，如果所有节点都被访问，则算法终止
            广度优先遍历一般采用open-close表
'''

class Graph(object):
    def __init__(self, nodes, sides):
        # nodes表示用户输入的点，int型，sides表示用户输入的边，是一个二元组(u, v)
 
        # self.sequence是字典，key是点，value是与key相连的边
        self.sequence = {}
        # self.side是临时变量，主要用于保存与 指定点v 相连接的点
        self.side = []
        for node in nodes:
            for side in sides:
                u, v = side
                # 指定点与另一个点在同一个边(可能是源点u或者是终点v)中，则说明这个点与指定点是相连接的点,则需要将这个点放到self.side中
                if node == u:
                    self.side.append(v)
                elif node == v:
                    self.side.append(u)
            # 注意，这里属于第二层循环，第一层是nodes中的一个点，第二层主要是遍历属于这个点的所有边，然后将点和边组成字典
            # 这里的字典aequence的key是第一层循环里面的一个点，value是一个[],就是刚才的临时变量self.side
            self.sequence[node] = self.side
            self.side = []
#         print(self.sequence)
        # {1: [2, 3], 2: [1, 4, 5], 3: [1, 6, 7], 4: [2, 8], 5: [2, 8], 6: [3, 7], 7: [3, 6], 8: [4, 5]}
 
    def dfs(self, node1, node2, node3):
        # queue本质堆栈，其实就是pop()了最后一个的列表，用来存放需要遍历的数据
        # order里面存放的是具体的访问路径
        queue1 = []
        queue2 = []
        queue3 = []
        order1 = []
        order2 = []
        order3 = []
        # 先将初始节点，对于树就是根节点，放到queue中，从node0开始遍历
        queue1.append(node1)
        queue2.append(node2)
        queue3.append(node3)
        flag1 = 1
        flag2 = 1
        flag3 = 1
        # 直到queue空了，也就是说图或树的节点全都遍历完了。
        while queue1 or queue2 or queue3:
            # queue不就是堆栈嘛，这里将堆栈里面的最后一个node拿出来，
            
            if queue1:
                v1 = queue1[-1]
#                 if v1 not in order1:
                order1.append(v1)
                flag1 = 0
                for w in self.sequence[v1]:
                    # 假如遍历这个[]中的数据不属于order，也不在queue中，说明这个点还没有访问过，于是加入queue,这里并不将其加入order中
                    # 因为是深度优先，所以这个点node访问完了之后要去queue中拿最后一个元素，也就是node节点的孩子
                    if w not in order1 and w not in order2 and w not in order3 and w not in queue1 and w not in queue2 and w not in queue3:
                        # append操作是将node加入到queue的末尾，恰好每次弹出来的也是末尾，所以访问的是初始节点---儿子---孙子---曾孙子
                        queue1.append(w)
                        flag1 = 1
                        break
                if flag1 == 0:
                    queue1.pop()
                    # 放到order中，就相当于已经遍历完了该node
#                     order1.append(v1)
            if queue2:
                v2 = queue2[-1]
#                 if v2 not in order2:
                order2.append(v2)
            # 从sequence字典中，找到该key值为v的node，注意value其实就是一个[]，所以遍历该node相连的边表[]中的所有数据
                flag2 = 0
                for w in self.sequence[v2]:
                    # 假如遍历这个[]中的数据不属于order，也不在queue中，说明这个点还没有访问过，于是加入queue,这里并不将其加入order中
                    # 因为是深度优先，所以这个点node访问完了之后要去queue中拿最后一个元素，也就是node节点的孩子
                    if w not in order1 and w not in order2 and w not in order3 and w not in queue1 and w not in queue2 and w not in queue3:
                        # append操作是将node加入到queue的末尾，恰好每次弹出来的也是末尾，所以访问的是初始节点---儿子---孙子---曾孙子
                        queue2.append(w)
                        flag2 = 1
                        break
                if flag2 == 0:
                    queue2.pop()
                    
            if queue3:
                v3 = queue3[-1]
#                 if v3 not in order3:
                order3.append(v3)
            # 从sequence字典中，找到该key值为v的node，注意value其实就是一个[]，所以遍历该node相连的边表[]中的所有数据
                flag3 = 0
                for w in self.sequence[v3]:
                    # 假如遍历这个[]中的数据不属于order，也不在queue中，说明这个点还没有访问过，于是加入queue,这里并不将其加入order中
                    # 因为是深度优先，所以这个点node访问完了之后要去queue中拿最后一个元素，也就是node节点的孩子
                    if w not in order1 and w not in order2 and w not in order3 and w not in queue1 and w not in queue2 and w not in queue3:
                        # append操作是将node加入到queue的末尾，恰好每次弹出来的也是末尾，所以访问的是初始节点---儿子---孙子---曾孙子
                        queue3.append(w)
                        flag3 = 1
                        break
                if flag3 == 0:
                    queue3.pop()
        return order1, order2, order3
    # bfs同理
    def bfs(self, node0):
        queue, order = [], []
        queue.append(node0)
        order.append(node0)
        while queue:
            v = queue.pop(0)
            for w in self.sequence[v]:
                if w not in order:
                    order.append(w)
                    queue.append(w)
        return order

n = 18
m = 12
nodes = [i for i in range(n * m)]
sides = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for xi in range(n):
    for yi in range(m):
        for k in range(4):
            newx = xi + dx[k]
            newy = yi + dy[k]
            if newx < 0 or newy < 0 or newx >= n or newy >= m:
                continue
            else:
                new1 = (yi + xi * m, newy + newx * m)
                new2 = (newy + newx * m, yi + xi * m)
                if new1 not in sides and new2 not in sides:
                    sides.append(new1)
start = np.random.randint(0, m * n - 1, 3)
# start = [12, 35]
G = Graph(nodes, sides)
order1, order2, order3 = G.dfs(start[0], start[1], start[2])
print(order1, order2, order3)
