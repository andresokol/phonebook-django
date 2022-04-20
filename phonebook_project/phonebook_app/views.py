import json

from django.db.models import Count, Max, Min
from django.shortcuts import get_object_or_404, redirect, render

from .models import Account, Person


def index(request):
    result = Person.objects.order_by("last_name", "first_name").all()

    context = {
        "persons": result,
        "general": {
            "html_title": "Some Title",
        },
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
    context["debug_context"] = json.dumps(
        context, indent=True, ensure_ascii=False
    )

    return render(request, "phonebook_app/stats.html", context)


def by_city(request, gorod: str):
    result = Person.objects.filter(city=gorod).all()

    context = {
        "persons": result,
        "filter_description": f"filtering by city = {gorod}",
        "general": {
            "html_title": "gorod",
        },
    }

    return render(request, "phonebook_app/index.html", context)


def by_city_and_age(request, city: str, age: int):
    result = Person.objects.filter(city=city, age=age).all()

    context = {
        "persons": result,
        "filter_description": f"filtering by city = {city} and age = {age}",
    }

    return render(request, "phonebook_app/index.html", context)


def by_city_and_age_range(request, city: str, age_from: int, age_to: int):
    result = Person.objects.filter(
        city=city,
        age__gte=age_from,
        age__lte=age_to,
    ).all()

    context = {
        "persons": result,
        "filter_description": (
            f"filtering by city = {city} and"
            + f" {age_from} <= age <= {age_to}"
        ),
    }

    return render(request, "phonebook_app/index.html", context)


def by_city_er(request, city_lowered: str):
    result = Person.objects.filter(
        city=city_lowered.capitalize(),
    ).all()

    context = {
        "persons": result,
        "filter_description": f"looking for {city_lowered}ers! "
        f"(from city {city_lowered.capitalize()})",
    }

    return render(request, "phonebook_app/index.html", context)


def person_view(request, person_id: int):
    selected_person = get_object_or_404(Person, id=person_id)

    context = {
        "persons": [selected_person],
        "general": {
            "html_title": f"{selected_person.last_name}",
            # или, если использовать __str__ из модели:
            # "html_title": str(selected_person),
        },
    }

    return render(request, "phonebook_app/index.html", context)


def url_example(request):
    context = {
        "city_from_context": "London",
        "age_from_context": "30",
        "some_other_dict": {
            "nested_params_example": "Berlin",
        },
    }
    return render(request, "phonebook_app/url_example.html", context)


def account_form(request, account_slug: str):
    account = get_object_or_404(Account, account_slug=account_slug)

    return render(
        request, "phonebook_app/csrf_example.html", {"account": account}
    )


def make_transaction(request, sender_slug: str):
    receiver_slug = request.GET.get("receiver_slug")
    transfer_amount = int(request.GET.get("transfer_amount"))

    sender = get_object_or_404(Account, account_slug=sender_slug)
    receiver = get_object_or_404(Account, account_slug=receiver_slug)

    sender.amount -= transfer_amount
    receiver.amount += transfer_amount

    sender.save()
    receiver.save()

    print(
        "\n\n\n",
        f"Transfered {transfer_amount}",
        f"from {sender_slug}",
        f"to {receiver_slug}",
        "\n\n\n",
    )

    return redirect("phonebook_app:account", sender_slug)
