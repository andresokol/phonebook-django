from django.db.models import Count, Min, Max
from django.shortcuts import render

from phonebook_app.models import Person


def index(request):
    result = Person.objects.all()

    context = {
        "persons": result,
    }

    return render(request, "phonebook_app/index.html", context)


def stats(request):
    stats = Person.objects.aggregate(
        total_users=Count("*"),
        oldest=Max("age"),
        youngest=Min("age"),
    )

    context = {
        "stats": stats,
    }

    return render(request, "phonebook_app/stats.html", context_with_debug)


#
#
#
#
#
#
#
#
#
#
#
#
#
#

# def by_city(request, city: str):
#     result = Person.objects.filter(city=city).all()

#     context = {
#         "persons": result,
#         "filter_description": f"filtering by city = {city}",
#     }

#     return render(request, "phonebook_app/index.html", context)


#
#
#
#
#
#
#
#
#
#
#
#
#
#


# def by_city_and_age(request, city: str, age: int):
#     result = Person.objects.filter(city=city, age=age).all()

#     context = {
#         "persons": result,
#         "filter_description": f"filtering by city = {city} and age = {age}",
#     }

#     return render(request, "phonebook_app/index.html", context)


#
#
#
#
#
#
#
#
#
#
#
#
#
#


# def by_city_and_age_range(request, city: str, age_from: int, age_to: int):
#     result = Person.objects.filter(
#         city=city,
#         age__gte=age_from,
#         age__lte=age_to,
#     ).all()

#     context = {
#         "persons": result,
#         "filter_description": f"filtering by city = {city} and {age_from} <= age <= {age_to}",
#     }

#     return render(request, "phonebook_app/index.html", context)


#
#
#
#
#
#
#
#
#
#
#
#
#
#


# def by_city_er(request, city_lowered: str):
#     result = Person.objects.filter(
#         city=city_lowered.capitalize(),
#     ).all()

#     context = {
#         "persons": result,
#         "filter_description": f"looking for {city_lowered}ers! (from city {city_lowered.capitalize()})",
#     }

#     return render(request, "phonebook_app/index.html", context)
