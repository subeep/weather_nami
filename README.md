# weather_nami

 Description of the project<br />
This is a Weather alert python application which uses Uagent from fetch.ai to notify and openweathermap.org weather api<br />
to get realtime weather data and use it. Input provided here is a pincode and country code as they are more simpler and less <br />
sophisticated than directly entering latitude and longitude. It also gives us a wide range of places to work with.<br />
This program currently checks weather every 10 seconds and updates the log but you can change it to 60 seconds for a better<br />
practical purpose rather than 10 seconds which is good to see how it works quickly.<br />

![githubreadme](https://github.com/subeep/weather_nami/assets/73274558/5b94c8aa-c805-4191-b675-e5dc535c28a7)


 Instructions to run the project<br />
First, create a directory then install uagents where the main.py resides<br />
Then, create a environment by <br />
'''pipenv shell'''<br />
After that run the program by<br />
'''python main.py'''<br />
then you can enter zip code and country code<br />
after getting the city name and location<br />
you can set maxmimum and minimum temperatures limits<br />
and then the uagents starts to check temperature and notify us.<br />



