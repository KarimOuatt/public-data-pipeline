import json

with open("data.json", "r", encoding="utf-8") as f:
    content = json.load(f)

stations = content["data"]["stations"]

total_number_of_stations = len(stations)
print(f"Number of stations in total: {total_number_of_stations}")

empty_renting_stations = 0
for station in stations:
    if station["num_bikes_available"] == 0 and station["is_renting"] == 1:
        empty_renting_stations += 1


print("-" * 50)
print(f"Number of empty renting stations: {empty_renting_stations}")
percentage_empty_renting_stations = (empty_renting_stations / total_number_of_stations) * 100

renting_stations = 0
for station in stations:
    if station["is_renting"] == 1:
        renting_stations += 1
print(f"Number of renting stations: {renting_stations}")
percentage_renting_stations = (renting_stations / total_number_of_stations) * 100

returning_stations_default = 0
for station in stations:
    if station["is_returning"] == 1 and station["num_docks_available"] == 0:
        returning_stations_default += 1
print(f"Number of returning stations: {returning_stations_default}")
percentage_returning_stations_default = (returning_stations_default / total_number_of_stations) * 100

returning_stations = 0
for station in stations:
    if station["is_returning"] == 1:
        returning_stations += 1
print(f"Number of returning stations: {returning_stations}")
percentage_returning_stations = (returning_stations / total_number_of_stations) * 100

print("-" * 50)
print(f"Percentage of empty renting stations: {percentage_empty_renting_stations:.2f}%")
print(f"Percentage of renting stations: {percentage_renting_stations:.2f}%")
print(f"Percentage of returning stations with no docks available: {percentage_returning_stations_default:.2f}%")
print(f"Percentage of returning stations: {percentage_returning_stations:.2f}%")
print("-" * 50)