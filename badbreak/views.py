from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def home(request):
    data = {}
    name = {}
    dob = {}
    occupation = {}
    nickname = {}
    portrayed = {}
    context = {}
    arr = []

    if 'character' in request.GET:
        character = request.GET['character']
        if not character:
            return HttpResponse('Enter any character!!!')

        url = 'https://www.breakingbadapi.com/api/characters?name=%s' % character
        response = requests.get(url)
        data = response.json()
        
        for x in data:
            name = x['name']
            dob = x['birthday']
            occupation = x['occupation'][0] 
            nickname = x['nickname']
            portrayed = x['portrayed']
            
            arr.append({'name': name,
            'dob': dob,
            'occupation': occupation,
            'nickname': nickname,
            'portrayed': portrayed,
            })
    
        context = {'key': arr}
    return render(request, 'badbreak/home.html', context)

def quotes(request, pk):
    arr = []
    url = 'https://www.breakingbadapi.com/api/quote?author=%s' % pk
    response = requests.get(url)
    data = response.json()

    for x in data:
        quote = x['quote']

        arr.append({
            'quote': quote,
        })
    
    context = {'key': arr}
    return render(request, 'badbreak/quotes.html', context)