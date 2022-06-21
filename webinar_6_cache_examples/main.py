import asyncio

from aiohttp import web

from db import DatabaseConnection
from models import Person

from caches import persons_cache


async def get_persons(request: web.Request) -> web.Response:
    # with DatabaseConnection() as connection:
    #     connection.execute("SELECT * FROM phonebook_app_person")
    #     data = connection.fetchall()

    # persons = [Person(*values) for values in data]

    persons = persons_cache.get_cached()

    return web.json_response(
        {
            "persons": [person.as_dict() for person in persons],
        }
    )


async def get_persons_by_city(request: web.Request) -> web.Response:
    # city: str = request.match_info["city"]
    pass


def main():
    app = web.Application()

    app.router.add_get("/persons/", get_persons)
    app.router.add_get("/persons/{city}/{age}/", get_persons_by_city)

    web.run_app(app, port=3000)


if __name__ == "__main__":
    asyncio.run(main())
