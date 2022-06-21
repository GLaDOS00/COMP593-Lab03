# Creating a movie data structure

# Creating a list of movie genres in the data structure
def list_genre(movies):
    list=[]
    for genre in movies['movies']:
        list.append(genre['genre'])
    # List of all movie genres from list
    for i in range(len(list)):
        if(i==0):
            print("These are some of my favourite movies genres:",end=" ")
        # Checking if the genre is not the last entry
        if(i<len(list)-1):
            
            print(list[i]+',',end=" ")
        else:
            print("and",list[i]+".")

# Creating a list of movie titles in the data structure
def list_title(titles):
    list=[]
    for title in titles:
        list.append(title['title'])
    for i in range(len(list)):
        if(i==0):
            print("These are my favourite movies:",end=" ")   
        if(i<len(list)-1):
            print(list[i]+',',end=" ")
        else:
            print("and",list[i]+".")

# Listing the toppings on my pizza
def list_toppings(toppings):
    print("My favourite pizza toppings are:")
    for top in toppings['pizza_toppings']:
         print("-",top)

# Listing my name and student ID
def stud_name_id(db):
    first_name=db['full_name'].split( )
    print("My name is",first_name[0],",but you can call me",db['full_name'],"\n")
    print("My student ID is",db['student_id'],"\n")

# Adding toppings to my pizza topping list from a tuple
def add_piz_top(pizza, top_tup):
    pizza['pizza_toppings']+=top_tup
    pizza['pizza_toppings'].sort()
    for i in range(len(pizza['pizza_toppings'])):
        pizza['pizza_toppings'][i]=pizza['pizza_toppings'][i].lower()
    return pizza

# Creating dictonary
def main():
    zack_dictionary={
        "full_name": "Zackary Clarke",

        "student_id": 10273504,

        "pizza_toppings": ["Onion","Pepperoni","Olives"],

        "movies":[
            {
                "title": "Drive",

                "genre": "Thriller"
            },
            {
                "title": "Place Beyond The Pines",
                "genre": "Crime/Drama"
            }
        ]
    }    

# Adding a new movie to the movie dictonary
    new_movie={
	"title": "Interstellar",

    'genre': "Science Fiction"
    }
    
    zack_dictionary['movies'].append(new_movie)

# Creating Pizza topping tuple
pizza_topping_tuple=("Crocodile","Emu","Kangaroo")

# Functions to list dictionary
    stud_name_id(zack_dictionary)
    list_genre(zack_dictionary)
    list_title(zack_dictionary['movies'])
    list_toppings(zack_dictionary)

# Adding pizza toppings to data structure
zack_dictionary=add_piz_top(pizza_topping_tuple)
list_toppings(zack_dictionary) 

main() 