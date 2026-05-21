from timocom.models.freight_offer_response import FreightOfferResponse
from timocom.types import UNSET


def test_freight_offer_response_accepts_nullable_optional_objects() -> None:
    response = FreightOfferResponse.from_dict(
        {
            "payload": {
                "objectType": "freightOffer",
                "closedFreightExchangeSetting": None,
                "contactPerson": {
                    "businessPhone": None,
                    "email": "ops@example.com",
                    "fax": None,
                    "firstName": "Ops",
                    "languages": ["en"],
                    "lastName": "User",
                    "mobilePhone": None,
                    "title": "MR",
                },
                "customer": {
                    "companyAddress": None,
                    "creationDateTime": None,
                    "id": 520934,
                    "postalAddress": None,
                },
                "id": "public-offer-id",
                "trackable": False,
                "useMessenger": True,
                "vehicleProperties": {
                    "body": ["CURTAIN_SIDER"],
                    "bodyProperty": [],
                    "equipment": [],
                    "loadSecuring": [],
                    "swapBody": [],
                    "type": ["TRAILER"],
                },
                "acceptQuotes": False,
                "additionalInformation": [],
                "freightDescription": "Shipping Broker",
                "length_m": 13.6,
                "loadingPlaces": [],
                "paymentDueWithinDays": None,
                "price": None,
                "weight_t": 24.0,
            }
        }
    )

    assert response.payload.id == "public-offer-id"
    assert response.payload.closed_freight_exchange_setting is UNSET
    assert response.payload.customer.company_address is UNSET
    assert response.payload.customer.creation_date_time is UNSET
    assert response.payload.customer.postal_address is UNSET
    assert response.payload.price is UNSET
