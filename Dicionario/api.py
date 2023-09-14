import requests
url = "https://pokemon-api3.p.rapidapi.com/pokemon"
headers = {
	"X-RapidAPI-Key": "7c44a1ab15msh592f336fb23fc46p1c2922jsn453bf099a3b3",
	"X-RapidAPI-Host": "pokemon-api3.p.rapidapi.com"
}

pok=input("qual pokemon?\n-->")

querystring = {"name":pok}

response = requests.get(url, headers=headers, params=querystring)


print(response.json())