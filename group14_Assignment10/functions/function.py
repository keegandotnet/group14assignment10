# Name: Keegan Smith & Cameron Vegh 
# email: smith6kg@mail.uc.edu & veghcg@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: 11/09/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates that I can use Python to make API calls.
# Citations: N/A
# Anything else that's relevant: N/A

def tell_joke(api_url):
    #import json <-- we don't need this! sweet!    
    import requests
    try:
        response = requests.get(api_url)
        #put it in a dictionary!
        data = response.json()
        #pull setup from dictionary.
        setup = data.get('setup', 'N/A')
        #pull punchline from dictionary.
        punchline = data.get('punchline', 'N/A')
        #print an informative message about what's about to go down.
        return f"Joke Setup: {setup}\nJoke Punchline: {punchline}"
        #shake your head at the stupid joke.
    except:
        return f"Failed to retrieve joke. Who's laughing now?"
    