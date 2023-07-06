from pymongo import MongoClient
from datetime import datetime

class MiniChallenge_DB():
    def __init__(self):
        self.client_url = "mongodb+srv://userReadOnly:7ZT817O8ejDfhnBM@minichallenge.q4nve1r.mongodb.net/"
        self.client = MongoClient(self.client_url)
        self.db = self.client.minichallenge
        self.query = {}
    
    def query_flights(self, departure_date: str, return_date: str, destination: str):
        res, collection_flights = [], self.db.flights
        departureDate = datetime(int(departure_date[:4]), int(departure_date[5:7]), int(departure_date[8:10]))
        returnDate = datetime(int(return_date[:4]), int(return_date[5:7]), int(return_date[8:10]))
        self.query = {
            "$and": [
                {"$or": [
                    {"destcity": destination},
                    {"srccity": destination}
                ]},
                {"$or": [
                    {"date": departureDate},
                    {"date": returnDate}
                ]}
            ]
        }
        for flight in collection_flights.find(self.query):
            res.append(flight)
        return res
    
    def query_hotels(self, check_in_date: str, check_out_date: str, destination: str):
        res, collection_hotels = [], self.db.hotels
        checkInDate = datetime(int(check_in_date[:4]), int(check_in_date[5:7]), int(check_in_date[8:10]))
        checkOutDate = datetime(int(check_out_date[:4]), int(check_out_date[5:7]), int(check_out_date[8:10]))
        self.query = {
            "city": destination,
            "date": {
                "$gte": checkInDate,
                "$lte": checkOutDate
            }
        }
        for hotel in collection_hotels.find(self.query):
            res.append(hotel)
        return res
    
import re
def validate_date_format(date: str):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(pattern, date):
        return True
    else:
        return False