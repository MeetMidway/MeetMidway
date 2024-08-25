import json
import os

import numpy as np
from allplaces import Places
from calcGeoMedian import CalculateGeometricMedian
from create_itinerary import generate_itinerary
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from gemini_filtering import filter_and_prioritize_places
from get_directions import get_directions

app = Flask(__name__)
CORS(
    app,
    resources={
        r"/*": {
            "origins": ["https://meetmidwayapp.vercel.app", "http://localhost:3000"]
        }
    },
)


@app.route("/get_itinerary", methods=["POST"])
def calculate_midpoint():
    data = request.json
    addresses = data.get("addresses", [])
    preferences = data.get("preferences", [])

    if not addresses:
        return jsonify({"error": "No addresses provided"}), 400

    # Here, you would call the MidwayAlgo logic to calculate the midpoint
    midpoint = CalculateGeometricMedian().geometric_median(np.array(addresses))
    print(midpoint)

    places = Places(os.environ["GOOGLE_API_KEY"], preferences)
    places_nearby = places.get_all_places_nearby(tuple(midpoint))

    places_info = [
        {
            "name": place.get("name"),
            "address": place.get("vicinity"),
            "types": place.get("types"),
            "rating": place.get("rating"),
            "user_ratings_total": place.get("user_ratings_total"),
            "coord": {"lat": place.get("lat"), "lng": place.get("lng")},
            "img": place.get("img"),
        }
        for place in places_nearby
    ]

    filtered_places = filter_and_prioritize_places(places_info, preferences)

    itinerary = generate_itinerary(filtered_places)

    return jsonify({"midpoint": midpoint.tolist(), "itinerary": itinerary})


@app.route("/get_directions", methods=["POST"])
def get_route():
    data = request.json

    addresses = data.get("addresses", [])
    midpoint = tuple(data.get("midpoint", []))
    addresses = [tuple(address) for address in addresses]

    print(addresses, midpoint)

    directions = get_directions(os.environ["GOOGLE_API_KEY"], midpoint, addresses)

    return jsonify({"directions": directions})


if __name__ == "__main__":
    app.run(debug=True)
