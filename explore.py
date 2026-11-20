import json

with open("station_status_data.json", "r", encoding="utf-8") as f:
    content = json.load(f)

stations_1 = content["data"]["stations"]

total_number_of_stations = len(stations_1)
print(f"Number of stations in total: {total_number_of_stations}")

empty_renting_stations = 0
for station in stations_1:
    if station["num_bikes_available"] == 0 and station["is_renting"] == 1:
        empty_renting_stations += 1


print("-" * 50)
print(f"Number of empty renting stations: {empty_renting_stations}")
percentage_empty_renting_stations = (empty_renting_stations / total_number_of_stations) * 100

renting_stations = 0
for station in stations_1:
    if station["is_renting"] == 1:
        renting_stations += 1
print(f"Number of renting stations: {renting_stations}")
percentage_renting_stations = (renting_stations / total_number_of_stations) * 100

returning_stations_default = 0
for station in stations_1:
    if station["is_returning"] == 1 and station["num_docks_available"] == 0:
        returning_stations_default += 1
print(f"Number of returning stations: {returning_stations_default}")
percentage_returning_stations_default = (returning_stations_default / total_number_of_stations) * 100

returning_stations = 0
for station in stations_1:
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


with open("station_information_data.json", "r", encoding="utf-8") as f:
    content = json.load(f)

stations_2 = content["data"]["stations"]
number_of_stations = len(stations_2)
print(f"Number of stations in information data: {number_of_stations}")


print("-" * 25 + " Mapping" + "-" * 25)

exactly_matching_stations = 0
for i in range(len(stations_1)):
    station_1 = stations_1[i]
    station_2 = stations_2[i]

    if station_1["station_id"] == station_2["station_id"]:
        exactly_matching_stations += 1
        print(f"Matching station found: {station_1['station_id']}, {station_2['name']}")

print(f"Number of exactly matching stations: {exactly_matching_stations}")