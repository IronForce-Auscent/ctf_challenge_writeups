from flask import Flask, jsonify, request
from . import get_database
from .get_database import validate_date_format
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
    flights, ticket_prices = mongodb.query_flights(departure_date, return_date, destination), {}
    flight_data = {
        "origin": ""
    }
    res = []
    for flight in flights:
        res.append(flight)
    res = {
        "City": destination,
        "Departure Date": departure_date,
        "Departure Airline": 0,
        "Departure Price": 0,
        "Return Date": return_date,
        "Return Airline": 0,
        "Return Price": 0
    }
    return json.loads(json_util.dumps(res))
    

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
    res = {
        "City": destination,
        "Check In Date": check_in_date,
        "Check Out Date": check_out_date,
        "Hotel": cheapest_hotel,
        "Price": hotel_prices[cheapest_hotel]
    }
    return res, 200


@app.route('/')
def index():
    return "Hello there"