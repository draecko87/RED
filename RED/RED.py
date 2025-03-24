##  Engineer: Walter Hage
##  Date: 03/23/25
##  Program:  Build a program that will have 4 functions
##      1. Fetch Data from an External API
##      2. Process & Store the Data
##      3. Expose an API Endpoint
##      4. Error Handling % Testing

### 1. Fetch Data from an External API  ###

## Fetch data from Pokeapi.co, which has data from all the pokemon in the frenchise, organize it in such a way that is easily readable, and display it for the user to see.
import requests
import time
import sys

#this is the default web address for the API we will be querying
webAddress = "https://pokeapi.co/api/v2/pokemon/"

#This function will process the query 
def choosePokemonName(name):
    url = f"{webAddress}/{name}"
    pokemon = requests.get(url)

    if pokemon.status_code == 200:
        pokemonData = pokemon.json()
        return pokemonData
    else:
        ### This covers part of number 4 where it points out error handling
        print(f"Failed to retrieve data {pokemon.status_code}")

#ask the user to make a choice and type it in
choice = input("Please Enter the pokemon you'd like to query: ")
pokemonName = choice
pokemonInfo = choosePokemonName(pokemonName)

#prints out the information of the user's choice
if pokemonInfo:
    name = pokemonInfo["name"].capitalize()
    print("Pokemon = " + name)
    id = pokemonInfo["id"]
    print("Id number = ", id)
    height = pokemonInfo["height"]
    print("Height = ", height)
    weight = pokemonInfo["weight"]
    print("Weight = ", weight)

#Closing the program
input_value = input("Press Enter to Exit the program...\n")
if input_value == "":
    print("Program is closing, Thank you for participating.")
    time.sleep(3)
    sys.exit()
else:
    print("Program is closing anyway, Thank you for participating.")
    time.sleep(3)
    sys.exit()