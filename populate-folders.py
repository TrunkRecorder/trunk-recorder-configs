import requests, os
from pathlib import Path


# City|State short name|State full name|County|City Alias Mixed Case
url = "https://raw.githubusercontent.com/grammakov/USA-cities-and-states/master/us_cities_states_counties.csv"

cwd = os.getcwd() + '/configs/'

response = requests.get(url)
locale_array =  response.text.split('\n')

for location in locale_array:
    try:
        data = location.split('|')
        city = data[0]
        state = data[2]
        county = data[3]

        # Create states
        if not os.path.isdir(f"{cwd}/{state}"):
            os.mkdir(f"{cwd}/{state}")


        # Create City Dirs
        if not os.path.isdir(f"{cwd}/{state}/counties/"):
            os.mkdir(f"{cwd}/{state}/counties/")


        if not os.path.isdir(f"{cwd}/{state}/systems-misc"):
            os.mkdir(f"{cwd}/{state}/systems-misc")
        Path(f'{cwd}/{state}/systems-misc/.gitkeep').touch()

        if not os.path.isdir(f"{cwd}/{state}/counties/{county}"):
            os.mkdir(f"{cwd}/{state}/counties/{county}")
        Path(f'{cwd}/{state}/counties/{county}/.gitkeep').touch()

        # Create City Dirs
        if not os.path.isdir(f"{cwd}/{state}/counties/{county}/cities/"):
            os.mkdir(f"{cwd}/{state}/counties/{county}/cities/")
        Path(f"{cwd}/{state}/counties/{county}/cities/.gitkeep").touch()


        if not os.path.isdir(f"{cwd}/{state}/counties/{county}/cities/{city}"):
            os.mkdir(f"{cwd}/{state}/counties/{county}/cities/{city}")
        Path(f'{cwd}/{state}/counties/{county}/cities/{city}/.gitkeep').touch()


    except Exception as error:
        print(str(error))
