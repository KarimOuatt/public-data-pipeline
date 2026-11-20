import requests
import json

def get_data(url : str) -> dict:
    """
    Fetch data from the specified URL.
    
    Args:
        url (str): The URL to fetch data from.
        
    Returns:
        dict: The JSON data fetched from the URL.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return {}

    if not isinstance(data, dict):
        raise TypeError(f"Expected data to be a dictionary, but got {type(data).__name__}")
    return data


def write_file(data: dict, file_path: str) -> None:
    """
    Write data to a specified file path.
    
    Args:
        data (dict): The data to write to the file.
        file_path (str): The path of the file where data will be written.
    """
    try :
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Data successfully written to {file_path}")
    except Exception as e:
        print(f"error:{e} ")


if __name__ == "__main__":
    url_1= "https://gbfs.velobixi.com/gbfs/2-2/fr/station_status.json"
    station_Status_Data = get_data(url_1)
    print(type(station_Status_Data))

    file_path = "station_status_data.json"
    write_file(station_Status_Data, file_path)

    for key, value in station_Status_Data.items():
        print(key)

    print("-" * 50)

    url_2 = "https://gbfs.velobixi.com/gbfs/2-2/en/station_information.json"
    station_Information_Data = get_data(url_2)
    print(type(station_Information_Data))

    file_path = "station_information_data.json"
    write_file(station_Information_Data, file_path)

    for key, value in station_Information_Data.items():
        print(key)

