from covid import Covid
from pprint import pprint

def covid():
    covid19 = Covid(source="worldometers")
    covidResults = covid19.get_status_by_country_name("ireland")
    country = covidResults["country"]
    activeCases = covidResults["active"]
    totalDeaths = covidResults["deaths"]
    newDeaths = covidResults["new_deaths"]
    newCases = covidResults["new_cases"]
    recovered = covidResults["recovered"]
    answer = {"answer" : "In {} there are {} new cases and {} new deaths".format(country, newCases, newDeaths)}
    answer["country"] = "Country: " + country + "\n"
    answer["newCases"] = "New Cases: " + str(newCases) + "\n"
    answer["newDeaths"] = "New deaths: " + str(newDeaths) + "\n"
    answer["activeCases"] = "Total active cases: " + str(activeCases) + "\n"
    answer["recovered"] = "Total recovered cases: " + str(recovered) + "\n"
    answer["totalDeaths"] = "Total deaths: " + str(totalDeaths) + "\n"

    print(answer)

covid()