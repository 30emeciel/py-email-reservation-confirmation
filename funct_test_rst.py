from datetime import date

from dotmap import DotMap

from rst import generate_confirmed_reservation_html_text

if __name__ == "__main__":
    pax = DotMap({
        "name": "Hello"
    }, _dynamic=False)
    request = DotMap({
        "id": "my_id",
        "created": date(2021, 2, 6),
        "kind": "COLIVING",
        "arrival_date": date(2021, 2, 19),
        "departure_date": date(2021, 3, 1),
        "number_of_nights": 3,
    }, _dynamic=False)

    html = generate_confirmed_reservation_html_text(pax, request)
    with open("test.html", mode='wb') as f:
        f.write(html.encode())

