from filmDAO import filmDAO

#create
latestid = filmDAO.create(("Toy Story",1995,50000000,"John Lasseter"))
#find by id
result = filmDAO.findByID(latestid);
print (result)

#update
filmDAO.update(('Santaclause the Movie',1995,latestid))
result = filmDAO.findByID(latestid);
print (result)

# get all 
allFilms = filmDAO.getAll()
for film in allFilms:
  print(film)

# delete
filmDAO.delete(latestid)