from django.shortcuts import render

# Create your views here.


def pokemons(request):
    people = []
    
    return render(request, "pokemons/pokemons.html")
