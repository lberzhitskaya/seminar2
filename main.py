from myboxclass import MyBox
box = MyBox()
box.add(1)
box.add('second')
box.add(3.5)
box.add('box')
box.add(9)
box.add('Resolved')
box.remove('second')
if ('first' in box) and (len(box) > 0):
    box.remove('first')
for i in box:
    print(i)
