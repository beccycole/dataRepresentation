colnames=['id','title','year','budget','director']
result=(1,"Toy Story", 1995, 60000000, "John Lasseter")
item = {}

for i, colName in enumerate(colnames):
    value = result[i]
    item[colName] = value

print(item)