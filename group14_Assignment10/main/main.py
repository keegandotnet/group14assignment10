# Name: Keegan Smith & Cameron Vegh 
# email: smith6kg@mail.uc.edu & veghcg@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: 11/09/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates that I can use Python to make API calls.
# Citations: N/A
# Anything else that's relevant: N/A


from functions.function import *

if __name__ == "__main__":
    api_url = "https://official-joke-api.appspot.com/random_joke"
    joke = tell_joke(api_url)
    print(joke)