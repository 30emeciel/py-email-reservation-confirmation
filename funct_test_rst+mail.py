from dotmap import DotMap

from mail import send_mail
from rst import generate_confirmed_reservation_html_text


def func_test_rst_mail():
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
    send_mail("tony.lbvre@gmail.com", "Test Reservation Mail", html)


if __name__ == "__main__":
    func_test_rst_mail()
