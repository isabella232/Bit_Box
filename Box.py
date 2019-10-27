class Box:
    def add(self, items):
        raise NotImplementedError()

    def empty(self):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
class BitBox(Box):
    def __init__(self):
        self._items = []

    def add(self, items):
        self._items.extend(items)

    def empty(self):
        items = self._items
        self._items = []
        return items

    def count(self):
        return len(self._items)


class BitKit(Box):
    def __init__(self):
        self._items = {}

    def add(self, items):
        for i in items:
            if i.name in self._items: 
                amount =  self._items[i.name][1]
                self._items[i.name] = [i, amount+1]
            else:
                self._items[i.name]= [i, 1] 

    def empty(self):
        items = self._items.values()
        self._items = {}
        return (item[0] for item in items) 

    def count(self):
        items = self._items.values()
        return sum((item[1] for item in items))
    
def repack_boxes(*boxes):
        items = []
        for box in boxes:
            items.extend(box.empty())
        while items:
            for box in boxes:
                if items:
                    item = [items.pop()]
                    box.add(item)
                else:
                    break

box1 = BitBox()
items = []
for i in range(20):
    item=Item(str(i), i)
    items.append(item)
box1.add(items)

items = []
box2 = BitBox()
for i in range(9):
    item=Item(str(i), i)
    items.append(item)
box2.add(items)
items = []
box3 = BitKit()
for i in range(5):
    item=Item(str(i), i)
    items.append(item)
box3.add(items)

repack_boxes(box1, box2, box3)

print(box1.count())
print(box2.count())
print(box3.count())