#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Write a Python program to simulate a movie rental service. Use
lists and dictionaries to store available movies, customer details, and rental transactions.
Create functions to rent a movie, return a movie, and generate a rental report. Ensure the
program handles multiple users and transactions'''


# In[11]:


movies = {
    "3 Idiots":{"copies":5,"rented": 0},
    "Pathaan":{"copies":3,"rented": 0},
    "Jawaan":{"copies":4,"rented": 0},
    "Baghbaan":{"copies":3,"rented":0},
}

customers = {}
transactions = []

def rent_movie(customer_name,movie_name):
    if movie_name in movies and movies[movie_name]["copies"]>movies[movie_name]["rented"]:
        movies[movie_name]["rented"]+=1
        if customer_name not in customers:
            customers[customer_name]=[]
        customers[customer_name].append(movie_name)
        transactions.append({"customer":customer_name,"movie":movie_name,"action":"rent"})
    else:
        return "Movie not available..."

def return_movie(customer_name,movie_name):
    if customer_name in customers and movie_name in customers[customer_name]:
        movies[movie_name]["rented"]-=1
        customers[customer_name].remove(movie_name)
        transactions.append({"customer":customer_name,"movie":movie_name,"action":"return"})
    else:
        return "Customer had not rented the movie..."

def rental_report():
    return {
        "available_movies":{movie:movies[movie]["copies"]-movies[movie]["rented"] for movie in movies},
        "transactions":transactions,
        "customers":customers
    }
rent_movie("Ishan","3 Idiots")
# rent_movie("Satyam","3 Idiots")
# rent_movie("Shivam","3 Idiots")
# rent_movie("Deva","3 Idiots")
# rent_movie("Rajat","3 Idiots")
# rent_movie("Vasu","3 Idiots")
rent_movie("Satyam","3 Idiots")
rent_movie("Shivam","Pathaan")
rent_movie("Deva","Jawaan")
rent_movie("Rajat","Pathaan")
rent_movie("Vasu","Baghbaan")
rent_movie("Ishan","Jawaan")
rental_report()
# return_movie("Shivam","Pathaan")
# rental_report()


# In[ ]:





# In[ ]:




