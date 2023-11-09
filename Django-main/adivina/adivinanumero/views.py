from django.shortcuts import render
import random
def home(request):
    return render(request,'adivinanumero/home.html')
def guess(request):
    random_number=random.randint(1,100)
    user_guess=int(request.POST['guess'])
    if user_guess==random_number:
        message="Congratulations You guessed the correct number"
    elif user_guess<random_number:
        message="The number its too low"
    else:
        message="The number its too high"
    return render(request,'adivinanumero/home.html',{'message':message})