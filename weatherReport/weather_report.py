import json 

def weather_option():
    print("1. Get Weather")
    print("2. Get Wind Speed")
    print("3. Get pressure")
    print("0. Exit")
    return int(input("Enter your choice: "))
    
def input_date():
    return input("enter the date(YYYY-MM-DD HH:MM:SS)")
    
def get_temperature(weather_data, date):
    for data in weather_data:
        if data["dt_txt"] == date:
            return data["main"]["temp"]
    return None

def windSpeed(weather_data,date):
    for data in weather_data:
        if(data["dt_txt"]== date):
            return data["wind"]["speed"]
    return None

def get_pressure(weather_data,date):
    for data in weather_data:
        if data["dt_txt"] == date:
            return data["main"]["pressure"]
    return None

def weather_data_file():
    try:
        with open('weather_data.json','r') as file:
            result= json.load(file)
            return result['list']
    except FileNotFoundError:
        print("Error: Weather_data.json Not Found")
        return None
    except json.JSONDecodeError:
        print("error: Invalid Json")
        return None

def main():
    weather_data = weather_data_file()
    
    if not weather_data:
        print("Error fetching weather data. Please check the Json file")
        return
    while True:
        choice = weather_option()
        
        if choice == 0:
            print("Exit")
            break
        elif choice == 1:
            date = input_date()
            temperature = get_temperature(weather_data, date)
            if temperature is not None:
                print(f"Temprature on {date}: {temperature} K")
            else:
                print("Data not found of given date")
        elif choice == 2:
            date = input_date()
            wind_speed = windSpeed(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not found of given date")
                
        elif choice == 3:
            date = input_date()
            pressure = get_pressure(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not found of given date")
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()  
        
    