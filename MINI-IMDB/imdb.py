import imdb                      # importing the module
ia = imdb.IMDb()                 # creating instance of IMDB
print("=======================")
name = input("Enter movie, tv series name : ")                # movie name
search = ia.search_movie(name)   # searching the movie
lst = list()		# defining a list
lst1 = list()
lst2 = list()
for j in range(len(search)) :
    id = search[j].movieID
    lst1.append(search[j]["title"] + " : " + id)
    lst2.append(id)
print(lst1)
print("====================================")
print("As there may be unwanted results, please specify the ID of the movie or TV series whose plot you would like.")
print("\n")
movie = input("Enter the ID of the movie or TV series: ")
index = lst2.index(movie)
Movie = search[index]
ia.update(Movie, info = ["plot"])		# to get the plot of the movie
print(Movie["plot"])
print("\n")
print("Cast of the movie or tv series : ")
movies = ia.get_movie(movie)
cast = movies["cast"]		# to get the cast of the movie
for actor in cast :
    print(actor)
print("\n")
print("Director of film or writer of series : ")
try :
    for director in movies["directors"] :		# try and except is used to prevent error messages that show up while compiling
        print(director["name"])
except :
    try:
        for writer in movies["writer"] :
            print(writer["name"])
    else:
        print("Sorry something went wrong, couldn't get the writers or the directors :(")
print("\n")
try :
    print("Ratings : ")
    rating = movies.data["rating"]
    print(rating)
except :
    print("Sorry something went wrong, couldn't get the ratings :2(")
print("\n")
try :
    print("Genres : ")
    genre = movies.data["genres"]
    print(genre)
except :
    print("Sorry something went wrong, couldn't get the genres :(")
    
    
