from flask import Flask, jsonify, request
from server import get_database
from server.get_database import validate_date_format
from bson import json_util
import json
import datetime

app = Flask(__name__)
mongodb = get_database.MiniChallenge_DB()


@app.route('/flight')
def get_flights():
    departure_date, return_date, destination = request.args.get("departureDate"), request.args.get("returnDate"), request.args.get("destination")
    if not departure_date or not return_date or not destination:
        print(departure_date, return_date, destination)
        res = {
            "message": "Bad URL/parameters submitted"
        }
        return res, 400
    elif not validate_date_format(departure_date) or not validate_date_format(return_date):
        print(departure_date, return_date)
        res = {
            "message": "Bad date(s) submitted"
        }
        return res, 400
    else:
        pass
    flights, flight_data = mongodb.query_flights(departure_date, return_date, destination), {}
    flight_data_sample_format = {
        "src_country_1": {
            "departure": ["ObjectID1", "ObjectID2", "ObjectID3", "ObjectID4", "..."],
            "return": ["ObjectID1", "ObjectID2", "ObjectID3", "ObjectID4", "..."]
        },
        "src_country_2": {
            "departure": ["ObjectID1", "ObjectID2", "ObjectID3", "ObjectID4", "..."],
            "return": ["ObjectID1", "ObjectID2", "ObjectID3", "ObjectID4", "..."]
        },
        "src_country_3": {
            "departure": ["ObjectID1", "ObjectID2", "ObjectID3", "ObjectID4", "..."],
            "return": ["ObjectID1", "ObjectID2", "ObjectID3", "ObjectID4", "..."]
        } # and so on...
    }
    sorted_flights = sorted(flights, key=lambda flight: flight['price'])
    for flight in sorted_flights:
        if flight["srccity"] in flight_data.keys() or flight["destcity"] in flight_data.keys():
            if flight["srccity"] in flight_data.keys():
                flight_data[flight["srccity"]]["departure"].append(flight["_id"])
            elif flight["destcity"] in flight_data.keys():
                flight_data[flight["destcity"]]["return"].append(flight["_id"])
            else:
                pass
        else:
            if flight["srccity"] not in flight_data.keys():
                flight_data[flight["srccity"]] = {
                    "departure": [],
                    "return": []
                }
            elif flight["destciity"] not in flight_data.keys():
                pass
            else:
                pass

    recommended_flights = {
        "City": destination,
        "Departure Date": departure_date,
        "Departure Airline": 0,
        "Departure Price": 0,
        "Return Date": return_date,
        "Return Airline": 0,
        "Return Price": 0
    }
    return json.loads(json_util.dumps(recommended_flights))
    

@app.route('/hotel')
def get_hotels():
    check_in_date, check_out_date, destination = request.args.get("checkInDate"), request.args.get("checkOutDate"), request.args.get("destination")
    if not check_in_date or not check_out_date or not destination:
        res = {
            "message": "Bad URL/parameters submitted"
        }
        return res, 400
    elif not validate_date_format(check_in_date) or not validate_date_format(check_out_date):
        res = {
            "message": "Bad date(s) submitted"
        }
        return res, 400
    else:
        pass
    hotels, hotel_prices = mongodb.query_hotels(check_in_date, check_out_date, destination), {}
    for hotel in hotels:
        if hotel["hotelName"] not in hotel_prices:
            hotel_prices[hotel["hotelName"]] = hotel["price"]
        else:
            hotel_prices[hotel["hotelName"]] += hotel["price"]
    cheapest_hotel = min(hotel_prices, key=hotel_prices.get)
    recommended_hotels = {
        "City": destination,
        "Check In Date": check_in_date,
        "Check Out Date": check_out_date,
        "Hotel": cheapest_hotel,
        "Price": hotel_prices[cheapest_hotel]
    }
    return recommended_hotels, 200


@app.route('/')
def index():
    return "Hello there"