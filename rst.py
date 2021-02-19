from babel.dates import format_date
from docutils.core import publish_string
from jinja2 import Environment, select_autoescape
from jinja2 import FileSystemLoader

settings_overrides = {

}


def date_format(d, fmt="medium"):
    return format_date(d, locale='fr', format=fmt)


env = Environment(
    loader=FileSystemLoader("res"),
    autoescape=select_autoescape(['html', 'xml']),
)
env.filters["dateformat"] = date_format


def generate_confirmed_reservation_title(pax, request):
    tpl = env.get_template('confirmed_reservation_title_fr.txt')
    txt = tpl.render({
        "pax": pax,
        "request": request,
    })
    return txt


def generate_confirmed_reservation_html_text(pax, request):
    tpl = env.get_template('confirmed_reservation_fr.rst')
    rst = tpl.render({
        "pax": pax,
        "request": request,
    })
    h = publish_string(source=rst, writer_name='html5', settings_overrides=settings_overrides)
    return h.decode()

