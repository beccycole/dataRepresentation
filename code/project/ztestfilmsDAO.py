from zfilmsDAO import filmDAO

#create
latestid = filmDAO.create(('Hangover', 2000, 70000000, 'Todd Phillips'))
# find by id
result = filmDAO.findByID(latestid);
print (result)

#update
#filmDAO.update(('Due Date',2010, 45000000,'Todd Phillips',latestid))
#result = filmDAO.findByID(latestid);
#print (result)

# get all 
allfilms = filmDAO.getAll()
for films in allfilms:
  print(films)

# delete
#filmDAO.delete(latestid)
