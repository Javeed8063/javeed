from django.shortcuts import render

# Create your views here.
def show(request):
    return render (request,"hotel.html")
def conform(request):
    selected = request.POST.getlist("checks[]")
    for i in range(0, len(selected)):
        selected[i] = int(selected[i])
    s = 0
    for i in selected:
        s += i
    dict = {"sum": s}

    return render(request,"conform.html",dict)