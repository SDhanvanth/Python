import algorithm

obj = algorithm.xo_algorithm()

r = True

while r:
    obj.show()
    obj.fill_for_user()
    obj.move_pc()
    r = obj.checking()
