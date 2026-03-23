import base64
import os
import sys
import datetime
from pathlib import Path

# Load credentials
env_path = Path.home() / ".config" / "timocom-cli" / ".env"
creds = {}
if env_path.exists():
    for line in env_path.read_text().splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            creds[k.strip()] = v.strip()

username = creds.get("TIMOCOM_USERNAME")
password = creds.get("TIMOCOM_PASSWORD")
timocom_id = int(creds.get("TIMOCOM_ID", 0))
base_url = creds.get("TIMOCOM_API_URL")

# Initialize client
credentials = f"{username}:{password}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

from timocom import AuthenticatedClient
from timocom.api.freight_offer import post_freight_offer, delete_freight_offer
from timocom.models import FreightOffer, PostalAddress, ContactPerson, VehicleProperties, LoadingPlace, LoadingPlaceLoadingType, Customer

client = AuthenticatedClient(
    base_url=base_url,
    token=encoded_credentials,
    prefix="Basic"
)

def test_postal_address_lifecycle():
    print(f"Testing POSTAL ADDRESS in lifecycle...")
    
    # 1. Create a freight offer using PostalAddress
    contact = ContactPerson(
        email="agent@broker.com",
        first_name="Agent",
        last_name="Broker",
        languages=["en"],
        title="MR"
    )
    
    vehicle = VehicleProperties(
        body=["REFRIGERATOR"],
        type_=["VEHICLE_UP_TO_12_T"]
    )
    
    place1 = LoadingPlace(
        loading_type=LoadingPlaceLoadingType.LOADING,
        earliest_loading_date=datetime.date.today(),
        latest_loading_date=datetime.date.today(),
        address=PostalAddress(
            country="PL", 
            city="Gdańsk", 
            postal_code="80165",
            street_or_postbox="Długa 1"
        )
    )
    
    place2 = LoadingPlace(
        loading_type=LoadingPlaceLoadingType.UNLOADING,
        earliest_loading_date=datetime.date.today(),
        latest_loading_date=datetime.date.today(),
        address=PostalAddress(
            country="DE", 
            city="Frankfurt", 
            postal_code="60320",
            street_or_postbox="Mainzer Landstraße 1"
        )
    )
    
    offer = FreightOffer(
        contact_person=contact,
        trackable=False,
        vehicle_properties=vehicle,
        accept_quotes=False,
        freight_description="Test PostalAddress Lifecycle",
        length_m=12.0,
        loading_places=[place1, place2],
        weight_t=23.5,
        customer=Customer(id=timocom_id)
    )
    
    print("Posting freight offer with PostalAddress...")
    response = post_freight_offer.sync_detailed(client=client, body=offer)
    print(f"Post Status: {response.status_code}")
    
    if response.status_code == 201:
        offer_id = response.parsed.payload.id
        print(f"SUCCESS: Published offer ID: {offer_id}")
        
        # Cleanup
        print(f"Cleaning up: Deleting offer {offer_id}...")
        delete_response = delete_freight_offer.sync_detailed(
            public_offer_id=offer_id,
            client=client,
            timocom_id=timocom_id
        )
        print(f"Delete Status: {delete_response.status_code}")
        return delete_response.status_code == 204
    else:
        print(f"Post failed: {response.content.decode()}")
        return False

if __name__ == "__main__":
    test_postal_address_lifecycle()
