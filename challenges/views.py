from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "eat no meat for the month",
    "february": "walk for 20min",
    "March": "sing 3 songs",
    "April": "count rain drops",
    "May": "look at flowers for 6hours each day",
    "June": "sweat",
    "July": "sweat more",
    "August": "sweat the most",
    "September": "perfect weather",
    "October": "its getting cold",
    "November": "oh cold isn't so bad",
    "December": None
}

# Create your views here.

def index(request):
    #list_items = ""
    months = list(monthly_challenges.keys())
    # for month in months:
    #     capital_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capital_month}</a></li>"
    #     response_data = f"<ul>{list_items}</ul>"
    #return HttpResponse(response_data)
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    #allows changing the url because of this 
    redirect_path = reverse("month-challenge", args=[redirect_month]) #challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name":month,
            "text": challenge_text
        })
    except:
        raise Http404()
    