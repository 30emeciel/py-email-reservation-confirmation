from datetime import date

from box import Box

from rst import generate_confirmed_reservation_html_text

if __name__ == "__main__":
    pax = Box({
        "name": "Hello"
    })
    request = Box({
        "id": "my_id",
        "created": date(2021, 2, 6),
        "kind": "COLIVING",
        "arrival_date": date(2021, 2, 19),
        "departure_date": date(2021, 3, 1),
        "number_of_nights": 3,
    })

    html = generate_confirmed_reservation_html_text(pax, request)
    with open("test.html", mode='wb') as f:
        f.write(html.encode())

