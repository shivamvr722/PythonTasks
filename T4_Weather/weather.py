import requests
from datetime import datetime
from dummy_data import history, forecast, current
# if you want to use dummpy local old data just un comment the calls and comment make_request function

def make_request(api, location, dt=None, key = "9c6db937f5764c51ae851421241305"):
    url = f"http://api.weatherapi.com/v1/{api}?key={key}&q={location}&dt={dt}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
    except requests.exceptions.RequestException as e:
        print("something went wrong while making api call")
        return None

def check_empty(value):
    if value == "":
        print("\n!!Empty Value Not Allowed!!\n")
        return False
    else:
        return True

def check_date(date):
    date_formate = "%Y-%m-%d"
    flag  = True
    while flag:
        try:
            vrdate = datetime.strptime(date,date_formate)
            flag = False
            return True
        except ValueError as e:
            # print("\nEnter Date in (YYYY-MM-DD) Formate \n")
            print("\n!Invalid Date!\n")
            date = input("Enter Date in (YYYY-MM-DD) Formate: ")
            flag = True

def get_current_temp(location):
    try:
        data  = make_request("current.json", location)
        # data = current()
        location = data["location"]["name"]
        state = data["location"]["region"]
        country = data["location"]["country"]
        time = data["location"]["localtime"]
        celcius = data["current"]["temp_c"]
        feren = data["current"]["temp_f"]
        c_feels = data["current"]["feelslike_c"]
        f_feels = data["current"]["feelslike_f"]
        print(f"\n Location: {location}, State: {state}, Country: {country}\n Time: {time} \n Celcius: {celcius}, Feels Like: {c_feels}, \n Ferenheight: {feren}, Feels like: {f_feels}\n")
    except Exception as e:
        print("\nData Not Found!")

def get_current_wind(location):
    try:
        data  = make_request("current.json", location)
        # data = current()
        location = data["location"]["name"]
        state = data["location"]["region"]
        country = data["location"]["country"]
        time = data["location"]["localtime"]
        direction = data["current"]["wind_dir"]
        degree = data["current"]["wind_degree"]
        speed_mph = data["current"]["wind_mph"]
        speed_kph = data["current"]["wind_kph"]
        print(f"\n Location: {location}, State: {state}, Country: {country}\n Time: {time} \n Direction: {direction}\n Degree: {degree}\n Speed in MPH: {speed_mph}\n Speed in KPH: {speed_kph}\n")
    except Exception as e:
        print("\nData Not Found!")

def get_current_humidity(location):
    try:
        data  = make_request("current.json", location)
        # data = current()
        location = data["location"]["name"]
        state = data["location"]["region"]
        country = data["location"]["country"]
        time = data["location"]["localtime"]
        humidity = data["current"]["humidity"]
        print(f"\n Location: {location}, State: {state}, Country: {country}\n Time: {time} \n Humidity: {humidity}\n")
    except Exception as e:
        print("\nData Not Found!")

def get_day_forecast_history(location, option, fh, date=None):
    if fh == "f":
        data  = make_request("forecast.json", location)
    else:
        data  = make_request("history.json", location, date)
    try:
        # data = forecast()
        # data = history()
        location = data["location"]["name"]
        state = data["location"]["region"]
        country = data["location"]["country"]
        time = data["location"]["localtime"]
        forecast_hours = data["forecast"]["forecastday"][0]["hour"]
        print(f"\n Location: {location}, State: {state}, Country: {country}\n Time: {time}")
        if option == "1":
            if fh == "f":
                print(" Tempreture Forecast @ 24HRS\n")
            else:
                print(" Tempreture History\n")    
            temp_max_c = data["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
            temp_min_c = data["forecast"]["forecastday"][0]["day"]["mintemp_c"]
            temp_max_f = data["forecast"]["forecastday"][0]["day"]["maxtemp_f"]
            temp_min_f = data["forecast"]["forecastday"][0]["day"]["mintemp_f"]
            print(f"\n Celcius: \n  Max Temp: {temp_max_c}C \n  Min Temp: {temp_min_c}C\n Ferenheight: \n  Max Temp: {temp_max_f}F \n  Min Temp: {temp_min_f}F\n")
            print("{:>13} {:>18} {:>13} {:>13} {:>13}".format("Time", "Celcius", "Ferenheight", "Feels Like C", "Feels Like F"))
            for forecast in forecast_hours:
                # print(forecast, "\n")
                time = forecast["time"]
                temp_c = str(forecast["temp_c"]) + " C"
                temp_f = str(forecast["temp_f"]) + " F"
                feel_c = str(forecast["feelslike_c"]) + " C"
                feel_f = str(forecast["feelslike_f"]) + " F"
                print("{:>20} {:>10} {:>10} {:>13} {:>13}".format(time, temp_c, temp_f, feel_c, feel_f))
        elif option == "2":
            if fh == "f":
                print(" Wind Forecast @ 24HRS\n")
            else:
                print(" Wind History\n")
            print("{:>10} {:>22} {:>13} {:>13} {:>15}".format("Time", "Wind MPH", "Wind KPH", "Degree", "Direction"))
            for forecast in forecast_hours:
                time = forecast["time"]
                wind_mph = str(forecast["wind_mph"]) + " mph"
                wind_kph = str(forecast["wind_kph"]) + " kph"
                wind_degree = forecast["wind_degree"]
                wind_dir = forecast["wind_dir"]
                print("{:>13} {:>15} {:>13} {:>13} {:>15}".format(time, wind_mph, wind_kph, wind_degree, wind_dir))    
        elif option == "3":
            if fh == "f":
                print(" Humidity Forecast @ 24HRS\n")
            else:
                print(" Humidity History\n")
            print("{:>13} {:>18}".format("Time", "Humidity"))
            for forecast in forecast_hours:
                time = forecast["time"]
                humidity = forecast["humidity"]
                print("{:>20} {:>10} ".format(time, humidity))
        else:
            print("Enter Appropriate Option\n")
    except Exception as e:
        print("\nData Not Found!")

def select_option():
    print("\nSELECT OPTION\n1. Check Current Tempreture\n2. Check Current Wind Speed\n3. Check Humidity\n4. Forecast\n5. History\n6. Exit")
    option = input("\nEnter Option: ").strip(" ")
    if not check_empty(option): return False
    if option != "6":
        location = input("Enter Location: ").strip(" ")
        if not check_empty(location): return False

    if option == "1":
        get_current_temp(location)
    elif option == "2":
        get_current_wind(location)
    elif option == "3":
        get_current_humidity(location)
    elif option == "4":
        print("\n 1. Tempreture Forecast 24 \n 2. Wind Forecast 24 \n 3. Humidity Forecast 24 ")
        optioni = input("\nEnter Option: ").strip(" ")
        get_day_forecast_history(location, optioni, "f")
    elif option == "5":
        date = input("\nEnter Date in YYYY-MM-DD Formate (Enter The Date of Current Year or More After 2023): ").strip(" ")
        if not check_empty(date): return False
        check_date(date)
        print("\n 1. Tempreture History\n 2. Wind History\n 3. Humidity History")
        optioni = input("\nEnter Option: ").strip(" ")
        get_day_forecast_history(location, optioni, "h", date = date)
    elif option == "6":
        return "close"
    else:
        print("Enter Appropriate Option")

def main():
    print("\nHELLO WEATHER\n")
    goes = True
    while goes:
        isend = select_option()
        if(isend == "close"):
            print("Thank You!")
            goes = False

if __name__ == "__main__":
    main()