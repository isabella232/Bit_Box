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