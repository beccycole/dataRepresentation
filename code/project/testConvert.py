colnames=['id','title','year','budget','director']
result=(1,"The Irishman",2019,140000000,"Martin Scorsese")
item = {}

for i, colName in enumerate(colnames):
    value = result[i]
    item[colName] = value

print(item)