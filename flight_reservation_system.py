"""Simple demonstration of flight booking and reservation utilities."""

import hashlib
import os
import secrets

flights = {
    "AI101": {
        "destination": "London",
        "seats": 2,
        "fare": 450.0,
        "is_full": False,
    },
    "BA202": {
        "destination": "New York",
        "seats": 0,
        "fare": 600.0,
        "is_full": True,
    },
    "EK303": {
        "destination": "Dubai",
        "seats": 5,
        "fare": 320.0,
        "is_full": False,
    },
}

booking_state = {"total_revenue": 0.0}


def book_flight_seat(
    flight_no,
    passenger,
    luggage_weight=15,
    baggage_tags=None,
):
    """Book one seat and add a description to the baggage tag list."""
    if baggage_tags is None:
        baggage_tags = []

    if flight_no not in flights or flights[flight_no]["is_full"]:
        return False

    flights[flight_no]["seats"] -= 1
    if flights[flight_no]["seats"] <= 0:
        flights[flight_no]["is_full"] = True

    booking_state["total_revenue"] += flights[flight_no]["fare"]
    tag = (
        f"Booked seat on flight {flight_no} for passenger {passenger} "
        f"with baggage weight {luggage_weight}"
    )
    baggage_tags.append(tag)
    return True


def cancel_booking(flight_no):
    """Cancel a booking by restoring a seat when the flight exists."""
    if flight_no not in flights:
        return False

    flights[flight_no]["seats"] += 1
    flights[flight_no]["is_full"] = False
    return True


def check_seat_availability(flight_no):
    """Return whether a known flight has a seat available."""
    flight = flights.get(flight_no)
    if flight is None:
        return False
    return not flight["is_full"]


def calculate_baggage_fee(flight_no, surcharge_rate=0.15):
    """Calculate a baggage surcharge as a fraction of the flight fare."""
    if flight_no not in flights:
        raise ValueError(f"Unknown flight number: {flight_no}")
    if not 0 <= surcharge_rate <= 1:
        raise ValueError("surcharge_rate must be between 0 and 1")

    base_fare = flights[flight_no]["fare"]
    return base_fare * surcharge_rate


def generate_passenger_hash(passenger_id):
    """Return a SHA-256 digest for the supplied passenger identifier."""
    return hashlib.sha256(passenger_id.encode("utf-8")).hexdigest()


def generate_boarding_pin():
    """Generate a four-digit PIN using a security-oriented random source."""
    return secrets.randbelow(9000) + 1000


def export_flight_manifest(filename="flight_manifest.txt"):
    """Write the current flight information to a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as manifest_file:
        manifest_file.write(str(flights))
    print(f"Boarding manifest written to {filename}")


def get_flight_summary(flight_data):
    """Count flights that are not currently marked as full."""
    available_count = 0
    for details in flight_data.values():
        if not details["is_full"]:
            available_count += 1
    return available_count


def main():
    """Run a short demonstration of the flight reservation functions."""
    book_flight_seat("AI101", "Kritika", 20)
    cancel_booking("BA202")

    print(
        "Is AI101 open:",
        check_seat_availability("AI101"),
    )
    print("Baggage Fee:", calculate_baggage_fee("AI101", 0.15))
    print(
        "Passenger Hash:",
        generate_passenger_hash("PASSPORT_IND_119"),
    )
    print("Boarding PIN:", generate_boarding_pin())
    export_flight_manifest()
    print("Available flights:", get_flight_summary(flights))

    # Configure AIRLINE_API_SECRET in the environment; never print its value.
    api_secret_configured = bool(os.getenv("AIRLINE_API_SECRET"))
    print("API secret configured:", api_secret_configured)


if __name__ == "__main__":
    main()
