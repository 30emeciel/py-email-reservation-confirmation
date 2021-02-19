from datetime import date

from dotmap import DotMap

from mail import send_mail
from rst import generate_confirmed_reservation_html_text


def func_test_rst_mail():
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
    send_mail("tony.lbvre@gmail.com", "Test Reservation Mail", html)


if __name__ == "__main__":
    func_test_rst_mail()
