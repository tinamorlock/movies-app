from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    context = {
        "title": "Movies",
        "movies": [
            "Pump Up the Volume",
            "American Beauty",
            "Drinking Games",
            "Never Been Thawed",
    ]}
    return render(request, "movies/index.html", context)


def about(request):
    return render(request, "movies/about.html", {})