
class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    """
    Returns the node with the given id using depth-first traversal.
    """
    def dfs(node):
      if node is None:
        return None
      if node['id'] == id:
        return node
      for child in node['children']:
        result = dfs(child)
        if result:
          return result
      return None

    return dfs(self.root)
  

# class Tree:
#   def __init__(self, root = None):
#     self.root = root

#   def get_element_by_id(self, id):
#     nodes_to_visit = [self.root]

#     while nodes_to_visit:
#       current = nodes_to_visit.pop()
#       if current['id'] == id:
#         return current

#       nodes_to_visit = nodes_to_visit + current['children']
#     return N