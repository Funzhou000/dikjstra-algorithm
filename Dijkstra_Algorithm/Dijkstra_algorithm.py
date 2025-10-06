#迪克斯特拉找加权图最短路径，本次练习没有加入能查找路径的每个经过的节点，只有最短路径的值
# 1. 创建图 (Graph)
# 使用一个字典来表示整个图
graph = {}
# 添加起点和它的邻居,同时加入起点到邻居的路程
#这里用到了嵌套字典
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# 添加其他节点和它们的邻居和路程
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

# 添加终点
graph["fin"] = {}

# 2. 创建开销表 (Costs Table)
# 创建一个字典来存储从起点到每个节点的开销
infinity = float("inf")  # 表示无穷大
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 3. 创建父节点表 (Parents Table)
# 创建一个字典来存储路径
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
# 4. 创建一个列表，用于记录已经处理过的节点
processed = []
def find_lowest_cost_node(costs):
    lowest_cost=float("inf")#这里将初始最低开销记作无穷大
    lowest_cost_node=None#最低花费的值记作none用于结束时
    for node in costs:#costs' key outed 
        cost=costs[node]
        if cost< lowest_cost and node not in processed:
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node
node =find_lowest_cost_node(costs)
while node is not None:
    cost =costs[node]
    neighbors=graph[node]#这里的neigbors is dic 
    for n in neighbors:# avliable for neighbors.key()
        new_cost=cost +neighbors[n]#calculate the distance from neighbor to 节点to start 
        if costs[n]>new_cost:#update distance from neighbor to start,costs[n] 是以前的到达节点的邻居的距离，如果newcost小，则记录新路径和距离
            costs[n]=new_cost
            parents[n]=node
    processed.append(node)#checked the neighbor,marking
    node= find_lowest_cost_node(costs)
print("从起点到各节点的最低开销:")
print(costs)
# 预期的输出: {'a': 5, 'b': 2, 'fin': 6}

print("\n通向各节点的父节点:")
print(parents)
# 预期的输出: {'a': 'b', 'b': 'start', 'fin': 'a'}