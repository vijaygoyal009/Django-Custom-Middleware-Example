from django.shortcuts import render



def index(request):
    # try:
    # obj = student.objects.all()

    # except:
    #     return HttpResponse("Your view has some wrong code")
    return render(request , 'index.html')