import os
import random
import sys

import django

FIRST_NAMES = [
    "james",
    "john",
    "robert",
    "michael",
    "william",
    "david",
    "richard",
    "charles",
    "joseph",
    "thomas",
    "christopher",
    "daniel",
    "paul",
    "mark",
    "donald",
    "george",
    "kenneth",
    "steven",
    "edward",
    "brian",
]

LAST_NAMES = [
    "smith",
    "johnson",
    "williams",
    "jones",
    "brown",
    "davis",
    "miller",
    "wilson",
    "moore",
    "taylor",
    "anderson",
    "thomas",
    "jackson",
    "white",
    "harris",
    "martin",
    "thompson",
    "garcia",
    "martinez",
    "robinson",
]

CITIES = [
    "Moscow",
    "London",
    "Paris",
    "Istanbul",
    "Berlin",
    "Vienna",
    "Zurich",
    "Madrid",
    "Lisbon",
    "Stockholm",
    "Helsinki",
]


def main():
    from phonebook_app.models import Person

    iterations_count = 500

    for _ in range(iterations_count):
        person = Person(
            first_name=random.choice(FIRST_NAMES).capitalize(),
            last_name=random.choice(LAST_NAMES).capitalize(),
            age=random.randint(18, 99),
            city=random.choice(CITIES),
        )
        person.save()


if __name__ == "__main__":

    # Root of the project is one folder up
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    sys.path.append(BASE_DIR)

    # Setting up django
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "phonebook_project.settings"
    )
    django.setup()

    # Actual script
    main()
