from django.shortcuts import render, redirect

import api

# Create your views here.

def redirect_index(request):
    return redirect("home", days_range=30, currencies="CAD,USD,CHF,PHP")



def dashboard(request, days_range=30, currencies="CAD,USD,CHF,PHP"):
    days, rates = api.get_rates(currencies=currencies.split(','), days=days_range)
    page_label = {7: "Semaine", 30: "Mois", 365: "Année"}.get(days_range, "Personnalisé")

    return render(request, "currency/index.html", context={'data': rates,
                                                           "days_labels": days,
                                                           "currencies": currencies,
                                                            "page_label": page_label})