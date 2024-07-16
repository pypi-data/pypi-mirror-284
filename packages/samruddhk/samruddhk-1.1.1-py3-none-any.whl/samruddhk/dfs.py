print("graph = {")
print("    'A': ['B', 'C', 'D'],")
print("    'B': ['E'],")
print("    'C': ['D', 'E'],")
print("    'D': [],")
print("    'E': []")
print("}")

print("\nvisited = set()")

print("\ndef dfs(visited, graph, root):")
print("    if root not in visited:")
print("        print(root)")
print("        visited.add(root)")
print("        for neighbor in graph[root]:")
print("            dfs(visited, graph, neighbor)")

print("\ndfs(visited, graph, 'A')")
