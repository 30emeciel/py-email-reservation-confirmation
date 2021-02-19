from dotmap import DotMap

from rst import generate_confirmed_reservation_html_text

if __name__ == "__main__":
    pax = DotMap({
        "name": "Hello"
    }, _dynamic=False)
    request = DotMap({
        "id": "my_id",
        "created": "created",
        "kind": "COLIVING",
        "arrival_date": "1",
        "departure_date": "2",
    }, _dynamic=False)

    html = generate_confirmed_reservation_html_text(pax, request)
    with open("test.html", mode='wb') as f:
        f.write(html.encode())

