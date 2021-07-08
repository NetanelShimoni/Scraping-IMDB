import tkinter

import imdb
import requests #to send the request to the URL
import json # use json
from bs4 import BeautifulSoup #to get the content in the form of HTML
import datetime ## convert number to time
from tkinter import *
import ctypes
import subprocess
import webbrowser


windows = Tk()

def openWin(): ## open WIN and get string movie
    def sumbit():
     movieName =entry.get()
     deatil(movieName)

    windows.title("Enter name of movie please")
    entry = Entry()
    sumbit = Button(windows,text ="search movie",command=sumbit)
    sumbit.pack(side = RIGHT)
    entry.config(font =('Ink Free',50))
    entry.config(width =25)
    entry.pack()
    entry.mainloop()



def deatil(movie_name): ## take all deatil

        MessageBox = ctypes.windll.user32.MessageBoxW # Dialog massage win


# creating an empty list, so that we can append the values
        try:

            Genres=[]
            Directors=[]
            Stars=[]
            onlyMovie=[]
            onlyMovieSorted = []
            moviesDB = imdb.IMDb()
            movies = moviesDB.search_movie(movie_name,'movie')
            for movie in movies:
                if(movie['kind']=='movie'):
                    onlyMovie.append(movie)



                for i in onlyMovie:
                    if (str(i['title']).lower().replace("-","").__contains__(movie_name.lower())):
                     onlyMovieSorted.append(i)

            if (movies): #Loading DB has succeeded
                id = onlyMovieSorted[0].getID() # id for get a URL
        except Exception as e:
            MessageBox(None, 'Movie not found', 'Window title', 0)
            return

        movie = moviesDB.get_movie(id)
        fileW = open("Movies.txt", "a+") # open file if not exist
        fileR = open("Movies.txt", "r") # for read from file
        URL = "https://www.imdb.com/title/tt"+id
        response = requests.get(URL)
        if (response.status_code==200):
            soup = BeautifulSoup(response.content,'html.parser')
            movie_director=soup.findAll('div', {'class': 'credit_summary_item'})
            movie_Genres=soup.findAll('div', {'class': 'subtext'})
            if(str(movie_director[0].text).__contains__("development")):
                    MessageBox(None, 'this project is categorized as in development', 'Window title', 0)
                    fileW.close()
                    fileR.close()
                    return

            movie_MPAAScript=soup.find('script',{'type': 'application/ld+json'})
            JsonMPPA = json.loads(str(movie_MPAAScript)[35:-9])
            title = movie['title']
            allLineOffile = fileR.read()
            if(allLineOffile.__contains__((title))): ## filter ( like a 'Elm')
                    fileR.close()
                    fileW.close()
                    MessageBox(None, 'The movie already exits', 'Window title', 0)
                    return

            fileW.write(title+"|")
            for i in movie_Genres:
                listOfGenres = i.findAll('a')
                for j in listOfGenres[0:-1]:
                    Genres.append(j.text)
            fileW.write(",".join(Genres)+"|")
            MPPA=""
            try:
                if(JsonMPPA["contentRating"]!="Not Rated"):
                    fileW.write(JsonMPPA["contentRating"] + "|")
            except KeyError:
                pass
            try:
                time = str(movie['runtimes']).replace("['", "").replace("']", "")
                fileW.write(str(datetime.timedelta(minutes=int(time)))
                    .replace(":", "h ", 1).replace(":", "m", 1).replace("0", "")+"|")
            except Exception as e:
                pass
            for i in movie_director:
                if (i.h4.text == "Directors:" or i.h4.text == "Director:"):
                    listOfDirector=i.findAll('a');
                    for j in listOfDirector:
                        Directors.append(str(j.text))

                if (i.h4.text == "Stars:" or i.h4.text == "Star:"):
                    listOfStar= i.findAll('a')[0:-1]
                    for j in listOfStar:
                        Stars.append(j.text)
            fileW.write(str(",".join(Directors)))
            fileW.write("|")
            fileW.write(str(",".join(Stars))+"\n")


            fileW.close()
            MessageBox(None, 'Movie successfully added ', 'Window title', 0) # Dialog win information
            windows.quit()
            webbrowser.open("movies.txt")

        else:
            MessageBox(None, 'ERROR: response fail', 'Window title', 0)





if __name__ == "__main__":
    openWin()
