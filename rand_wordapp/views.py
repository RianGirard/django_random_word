from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string

def index(request):
    return render(request, "index.html")

def random(request):
    word = get_random_string(length=14)         # call imported method to assign variable

    if "counter" not in request.session:        # if the request.session is empty, then set that "key" to 0
        request.session["counter"] = 0

    request.session["counter"] +=1              # bump the value +=1 each time method is called

    if "word_list" not in request.session:      # if the request.session is empty, then create list
        request.session["word_list"] = []

    request.session['random_word'] = word       # assign the variable into the session
    request.session["word_list"].append(word)   # append the variable into the list


    return redirect("/")                        # send the user on to the root route

def reset(request):
    request.session.flush()                     # flush the session variables on reset

    return redirect('/')


# Create your views here.
