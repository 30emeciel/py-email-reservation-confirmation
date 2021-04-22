import dotenv
import pytest
from box import Box


@pytest.fixture(autouse=True)
def env():
    dotenv.load_dotenv()


def test_trigger_on_update_reservation_request(when):
    resource = "pax/google-oauth2|107336710838050909583/requests/KHQpVVu1H7Hvn3jLwX01"
    event = {
        "oldValue": {
            "createTime": "2021-03-05T19:54:37.991311Z",
            "fields": {
                "arrival_date": {"timestampValue": "2021-03-15T23:00:00Z"},
                "created": {"timestampValue": "2021-03-05T19:54:37.978Z"},
                "departure_date": {"timestampValue": "2021-03-19T23:00:00Z"},
                "kind": {"stringValue": "COLIVING"},
                "number_of_nights": {"integerValue": "4"},
                "state": {"stringValue": "PENDING_REVIEW"}
            },
            "name": f"projects/trentiemeciel/databases/(default)/documents/{resource}",
            "updateTime": "2021-03-05T21:56:55.248879Z"
        },
        "updateMask": {"fieldPaths": ["state"]},
        "value": {
            "createTime": "2021-03-05T19:54:37.991311Z",
            "fields": {
                "arrival_date": {"timestampValue": "2021-03-15T23:00:00Z"},
                "created": {"timestampValue": "2021-03-05T19:54:37.978Z"},
                "departure_date": {"timestampValue": "2021-03-19T23:00:00Z"},
                "kind": {"stringValue": "COLIVING"},
                "number_of_nights": {"integerValue": "4"},
                "state": {"stringValue": "CANCELED"}
            },
            "name": f"projects/trentiemeciel/databases/(default)/documents/{resource}",
            "updateTime": "2021-03-05T21:56:55.248879Z"
        }
    }
    # from core.firestore_client import db
    # sub_sub_ref_mock = mock({"get": lambda: {}}, spec=DocumentReference)
    # sub_ref_mock = mock({"parent": sub_sub_ref_mock}, spec=DocumentReference)
    # ref_mock = mock({"parent": sub_ref_mock}, spec=DocumentReference)
    # when(db).document(resource).thenReturn(ref_mock)
    # pax_doc_mock = mock(spec=DocumentSnapshot)
    # request_doc_mock = mock(spec=DocumentSnapshot)
    # when(sub_sub_ref_mock).get().thenReturn(pax_doc_mock)
    # when(ref_mock).get().thenReturn(request_doc_mock)
    # when(pax_doc_mock).exists().thenReturn(True)
    # when(request_doc_mock).exists().thenReturn(True)

    from main import trigger_on_update_reservation_request
    trigger_on_update_reservation_request(resource, Box(event))

