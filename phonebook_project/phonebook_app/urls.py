from django.urls import path

from . import views

app_name = "phonebook_app"

urlpatterns = [
    path("", views.index, name="main_page"),
    path("stats", views.stats, name="stats"),
    path("by_city/<slug:gorod>", views.by_city, name="list_by_city"),
    path(
        "by_city/<slug:city>/age/<int:age>",
        views.by_city_and_age,
        name="list_by_city_and_age",
    ),
    path(
        "by_city/<slug:city>/age/<int:age_from>/<int:age_to>",
        views.by_city_and_age_range,
        name="list_by_city_and_age_range",
    ),
    path(
        "by_city_v2/<slug:city_lowered>ers",
        views.by_city_er,
        name="list_by_city_v2",
    ),
    path("person/<int:person_id>", views.person_view),
    path("url_example", views.url_example),
    path("account/<slug:account_slug>/", views.account_form, name="account"),
    path(
        "account/<slug:sender_slug>/transfer/",
        views.make_transaction,
        name="make_transaction",
    ),
]
