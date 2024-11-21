import json
with open("exercises/09/02_airport_data/airports.json") as f:
    data = json.load(f)
    print(f"Total entries: {len(data)}")
    airports = set()
    for entry in data:
        airports.add(entry['Airport']['Code'])
    print(f"Unique airports: {len(airports)}")

    max_flights = 0
    max_airport = None
    for entry in data:
        if entry["Time"]["Month"] == 2 and entry["Time"]["Year"] == 2015:
            if entry['Statistics']['Flights']['Total'] > max_flights:
                max_flights = entry['Statistics']['Flights']['Total']
                max_airport = entry['Airport']['Name']
    print(f"Airport with most flights in Feb 2015: {max_airport} (flights: {max_flights})")

    flight_counts = {}
    for entry in data:
        code = entry["Airport"]["Code"]
        if code not in flight_counts:
            flight_counts[code] = 0
        flight_counts[code] += entry["Statistics"]["Flights"]["Total"]
    print(flight_counts)