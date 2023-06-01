
def bfs_recursive(graph,queue,visited):
    if not queue:
        return
    
    node=queue.pop(0)
    print(node," ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    
    bfs_recursive(graph,queue,visited)

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

visited=set()
queue=[]
visited.add('A')
queue.append('A')
bfs_recursive(graph,queue,visited)