employees=({"eid":101},{"eid":102},{"eid":103})
employees.insert(1,{"eid":104}) #AttributeError: 'tuple' object has no attribute 'insert'
print(employees)