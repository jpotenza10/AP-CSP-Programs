#Album Recommender
#Initialize
import pandas as pd
import webbrowser
data=pd.read_csv('albums.csv')
#Below is all the types of data provided by the dataset.
ID = data["id"].tolist()
album_rank = data['Album Rank'].tolist()
album_year = data['Year'].tolist()
album_name = data['Album'].tolist()
artist = data['Artist'].tolist()
genre = data['Genre'].tolist()
subgenre = data['Subgenre'].tolist()
album_art = data['Album Art'].tolist()
albums_found = []
#Functions
def main():
#This program helps the user find albums to listen to.
    while True:
        #Gives an option to the user if they want to find an album or exit the program each time the code is run.
        action=input("Welcome to album recommender, would you like to find an album or exit?: ").lower()
        if action=="find an album":
            print("It seems that you're looking for a new album to listen to. We'll give you recommendations based on your ideal genre and year")
            genre_name=input("What genre are you looking for?: ")
            sub_genre=input("What subgenre would you like to find?: ")
            year=int(input("What year do you want to find an album from?: ")) #Since the years are numbers and not strings I made sure to use "int".
            album(genre_name, sub_genre, year) #Calls on the function after you input all the parameters that it needs to run.
            continue
        #I used an else statment so the user doesn't have to say exit to leave the program, they could say something like "leave" and the program will still end.
        else:
            break
#This is the function that will determine what albums you should listen to.
def album(genre_name, sub_genre, year):
    for i in range(len(ID)):
         if (genre_name).lower() in str(genre[i]).lower() and (sub_genre).lower() in str(subgenre[i]).lower() and (year)==int(album_year[i]):
            albums_found.append(artist[i])
            albums_found.append(album_name[i])
            see_art=input("Would you like to see the album art?: ").lower()
            if see_art=="yes":
                webbrowser.open(album_art[i])
    print("It seems like you should listen to " + str(albums_found))
    albums_found.clear()

#Main
main()

#All data and images in this program came from: https://www.kaggle.com/datasets/notgibs/500-greatest-albums-of-all-time-rolling-stone
#Dataset shared by code.org
