import requests
from uagents import Agent,Context

zipcode = int(input("Enter the Zip Code(Pincode): "))
country_code = str(input("Country code(\"in\" for India ): "))

api_key = "API_KEY" #(Get the following api key by going to openweathermap.org)

zipapi = "http://api.openweathermap.org/geo/1.0/zip?zip={},{}&appid={}".format(zipcode,country_code,api_key)
city = requests.get(zipapi)
city_lat = 0
city_lon = 0

try:
    city = requests.get(zipapi)
    if city.status_code == 200:
            # Parse the JSON response
        citydata = city.json()
        city_lat = citydata['lat']
        city_lon = citydata['lon']
        city_name = citydata['name']

        print("City name: {} , Latitute: {} , Longitude: {} ".format(city_name,city_lat,city_lon))
    else:
        print(f"Error: Failed to fetch data. Status code: {city.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")




api_url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric".format(city_lat,city_lon,api_key)


minlim = float(input("Input minimum temperature limit in celsius: "))
maxlim = float(input("Input maxmimum temperature limit in celsius: "))



Nami = Agent(name='Nami', seed = "Nami recovery phrase")

@Nami.on_interval(period = 10.0)
async def checktemp(ctx: Context):
    ctx.logger.info('Nami is checking the temp')
    try:
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            Final_result = data['main']
            Current_temp = float(Final_result['temp'])

            if Current_temp > maxlim:
                print('ALERT! The temperature {} Celsius has crossed the maximum threshold of {} Celsius. '.format(Current_temp, maxlim))
            elif Current_temp < minlim:
                print('ALERT! The temperature {} Celsius has crossed the minimum threshold {} Celsius. '.format(Current_temp, minlim))
            else:
                ctx.logger.info(Current_temp)
        else:
            print(f"Error: Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")





if __name__ == "__main__":
    Nami.run()
