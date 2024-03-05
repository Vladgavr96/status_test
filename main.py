class TreeStore:
    def __init__(self, items):
        self.tree_dict = {}
        for item in items:
            self.tree_dict[item["id"]] = item

    def getAll(self):
        return list(self.tree_dict.values())

    def getItem(self, id):
        return self.tree_dict.get(id)

    def getChildren(self, id):
        children = []
        for item_id, item in self.tree_dict.items():
            if item.get("parent") == id:
                children.append(item)
        return children

    def getAllParents(self, id):
        parents = []
        item = self.getItem(id)
        while item:
            parents.append(item)
            parent_id = item.get("parent")
            item = self.getItem(parent_id)
        return parents[::-1]


# Исходные данные:
items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)

# Примеры использования:
print(ts.getAll())
print(ts.getItem(7))
print(ts.getChildren(4))
print(ts.getChildren(5))
print(ts.getAllParents(7))