# tuple1 = ("20","22")
#
# print(type(tuple1))
#
# tuple2 = ("qx", "lyr")
# print(tuple2[0])
#
# # del tuple1
#
# tuple3 = tuple2+tuple1
# print(tuple3)
#
# tuple4 = (x for x in range(1,10))
# tuple5 = tuple(tuple4)
# print(type(tuple5))

geades = (87,100,96,77,69,83,91,77,63,85)

print(geades[1])

print(geades[0:5])




print(geades.count(77))

print(geades.index(100))

print(len(geades))



list_grades= list(geades)
print(type(list_grades))

tup_grades = tuple(list_grades)
print(type(tup_grades))

grades_other = (34,67)
gradesAll = geades+grades_other
print(gradesAll)
