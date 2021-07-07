# Scraping:
The purpose of the code is to get the name of a movie and with the help of libraries in Python to extract the following data to the file: </br>
**Movie title | Genre | MPAA ration | Movie duration | Directors |Stars** </br>
With the help of libraries such as:
1) imdb (library installation: pip install imdbpy)
2) requests
3) json
4) beautifulSoup
5) datetime
6) tkinter

I was able to lack information from imdb.com.

work process:
* I browsed the html file of the given site.
* I divided by tags according to the data I had to provide in the task.
* With the help of BeautifulSoup I was able to pump out the relevant information.
* Represent the information into a file.
_
Code explanation:
* Using "details" function that gets a name of a movie, I first checked if the input is a movie.
* I filtered the movies by exact match so that it would not get names of unwanted movies (ELM).
* If the movie appears, I selected the exact match (from the movies).
* I retrieved the id of the movie using the imdb directory. 
* I connected to the site, with the id of the movie.
* In case of connection success (status code = 200), I retrieved data from url using div tags and json files.
* The results can be seen in the movies.txt file

</br>
**example:** 
</br>
![תמונה](https://user-images.githubusercontent.com/57719538/124265620-99386f80-db3e-11eb-8581-845048f876f9.png)

I have attached a movies.txt file where the input is the movie "Star trek"
