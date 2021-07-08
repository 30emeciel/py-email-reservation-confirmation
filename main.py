import logging

from box import Box
from core import firestore_client
from core.mailer import Mailer
from core.rst_to_html import to_html
from core.tpl import render

log = logging.getLogger(__name__)
mailer = Mailer()
db = firestore_client.db()


def from_firestore(event, context):
    """Triggered by a change to a Firestore document.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    resource_string = context.resource

    # print out the resource string that triggered the function
    log.info(f"Function triggered by change to: {resource_string}.")
    # now print out the entire event object
    log.debug(str(event))

    trigger_on_update_reservation_request(resource_string, Box(event))


def trigger_on_update_reservation_request(doc_path, event):

    if "state" not in event.updateMask.fieldPaths:
        log.info("state hasn't changed, ignoring")
        return

    request_ref = db.document(doc_path)
    pax_ref = request_ref.parent.parent
    pax_doc, request_doc = pax_ref.get(), request_ref.get()
    assert pax_doc.exists and request_doc.exists

    request_plus_id = request_doc.to_dict()
    request_plus_id.update({"id": request_doc.id})
    request = Box(request_plus_id)
    pax = Box(pax_doc.to_dict())
    if request.state != "CONFIRMED":
        log.info(f"request 'state' != CONFIRMED, ignoring")
        return

    data = {
        "pax": pax,
        "request": request
    }
    html = to_html(render("confirmed_reservation_fr.rst", data))
    title = render("confirmed_reservation_title_fr.txt", data)

    mailer.send_mail(pax.name, pax.email, title, html)

