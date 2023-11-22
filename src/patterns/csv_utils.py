import csv
from datetime import datetime


class Ride:

    def __init__(self, taxi_id, pick_up_time, drop_off_time, passenger_count, trip_distance, tolls_amount):
        self.taxi_id = taxi_id
        self.pick_up_time = pick_up_time
        self.drop_off_time = drop_off_time
        self.passenger_count = passenger_count
        self.trip_distance = trip_distance
        self.tolls_amount = tolls_amount

    def get_taxi_id(self):
        return self.taxi_id

    def get_pick_up_time(self):
        return self.pick_up_time

    def get_drop_off_time(self):
        return self.drop_off_time

    def get_passenger_count(self):
        return self.passenger_count

    def get_trip_distance(self):
        return self.trip_distance

    def get_tolls_amount(self):
        return self.tolls_amount


def parse_file(file_path):
    with open(file_path, "r") as f:
        reader = csv.reader(f, delimiter=",")
        next(reader, None)  # Skip header
        rides = []
        for row in reader:
            taxi_id = row[0]
            pick_up_time = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
            drop_off_time = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
            passenger_count = int(row[3])
            trip_distance = float(row[4])
            tolls_amount = float(row[5])
            rides.append(Ride(taxi_id, pick_up_time, drop_off_time, passenger_count, trip_distance, tolls_amount))
    return rides  