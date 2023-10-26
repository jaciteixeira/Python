'''
import requests

def forca_opcao(msg,lista_opcoes):
	resposta = input(msg)
	while resposta not in lista_opcoes:
		print("opcoes: ")
		for opcao in lista_opcoes:
			print(opcao)
		resposta = input(msg)
	return resposta

def get_languages():
	url = "https://text-translator2.p.rapidapi.com/getLanguages"
	headers = {
		"X-RapidAPI-Key": "7c44a1ab15msh592f336fb23fc46p1c2922jsn453bf099a3b3",
		"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
	}
	response = requests.get(url, headers=headers)
	print(response.json())
	# print(response)

	return response


def translate(opcao_alvo, opcao_origem,texto):
	url = "https://text-translator2.p.rapidapi.com/translate"
	payload = {
		'source_language': dic_final[opcao_alvo],
		'target_language': dic_final[opcao_origem],
		'text': texto
	}
	headers = {
		"X-RapidAPI-Key": "7c44a1ab15msh592f336fb23fc46p1c2922jsn453bf099a3b3",
		"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
	}
	response = requests.post(url, headers=headers)
	response = (response.json())

	return response['data']['translated_text']

# dic = {'data': {'languages': [{'code': 'af', 'name': 'Afrikaans'}, {'code': 'sq', 'name': 'Albanian'}, {'code': 'am', 'name': 'Amharic'}, {'code': 'ar', 'name': 'Arabic'}, {'code': 'hy', 'name': 'Armenian'}, {'code': 'az', 'name': 'Azerbaijani'}, {'code': 'eu', 'name': 'Basque'}, {'code': 'be', 'name': 'Belarusian'}, {'code': 'bn', 'name': 'Bengali'}, {'code': 'bs', 'name': 'Bosnian'}, {'code': 'bg', 'name': 'Bulgarian'}, {'code': 'ca', 'name': 'Catalan'}, {'code': 'ceb', 'name': 'Cebuano'}, {'code': 'ny', 'name': 'Chichewa'}, {'code': 'zh-CN', 'name': 'Chinese (Simplified)'}, {'code': 'zh-TW', 'name': 'Chinese (Traditional)'}, {'code': 'co', 'name': 'Corsican'}, {'code': 'hr', 'name': 'Croatian'}, {'code': 'cs', 'name': 'Czech'}, {'code': 'da', 'name': 'Danish'}, {'code': 'nl', 'name': 'Dutch'}, {'code': 'en', 'name': 'English'}, {'code': 'eo', 'name': 'Esperanto'}, {'code': 'et', 'name': 'Estonian'}, {'code': 'tl', 'name': 'Filipino'}, {'code': 'fi', 'name': 'Finnish'}, {'code': 'fr', 'name': 'French'}, {'code': 'fy', 'name': 'Frisian'}, {'code': 'gl', 'name': 'Galician'}, {'code': 'ka', 'name': 'Georgian'}, {'code': 'de', 'name': 'German'}, {'code': 'el', 'name': 'Greek'}, {'code': 'gu', 'name': 'Gujarati'}, {'code': 'ht', 'name': 'Haitian Creole'}, {'code': 'ha', 'name': 'Hausa'}, {'code': 'haw', 'name': 'Hawaiian'}, {'code': 'iw', 'name': 'Hebrew'}, {'code': 'hi', 'name': 'Hindi'}, {'code': 'hmn', 'name': 'Hmong'}, {'code': 'hu', 'name': 'Hungarian'}, {'code': 'is', 'name': 'Icelandic'}, {'code': 'ig', 'name': 'Igbo'}, {'code': 'id', 'name': 'Indonesian'}, {'code': 'ga', 'name': 'Irish'}, {'code': 'it', 'name': 'Italian'}, {'code': 'ja', 'name': 'Japanese'}, {'code': 'jw', 'name': 'Javanese'}, {'code': 'kn', 'name': 'Kannada'}, {'code': 'kk', 'name': 'Kazakh'}, {'code': 'km', 'name': 'Khmer'}, {'code': 'rw', 'name': 'Kinyarwanda'}, {'code': 'ko', 'name': 'Korean'}, {'code': 'ku', 'name': 'Kurdish (Kurmanji)'}, {'code': 'ky', 'name': 'Kyrgyz'}, {'code': 'lo', 'name': 'Lao'}, {'code': 'la', 'name': 'Latin'}, {'code': 'lv', 'name': 'Latvian'}, {'code': 'lt', 'name': 'Lithuanian'}, {'code': 'lb', 'name': 'Luxembourgish'}, {'code': 'mk', 'name': 'Macedonian'}, {'code': 'mg', 'name': 'Malagasy'}, {'code': 'ms', 'name': 'Malay'}, {'code': 'ml', 'name': 'Malayalam'}, {'code': 'mt', 'name': 'Maltese'}, {'code': 'mi', 'name': 'Maori'}, {'code': 'mr', 'name': 'Marathi'}, {'code': 'mn', 'name': 'Mongolian'}, {'code': 'my', 'name': 'Myanmar (Burmese)'}, {'code': 'ne', 'name': 'Nepali'}, {'code': 'no', 'name': 'Norwegian'}, {'code': 'or', 'name': 'Odia (Oriya)'}, {'code': 'ps', 'name': 'Pashto'}, {'code': 'fa', 'name': 'Persian'}, {'code': 'pl', 'name': 'Polish'}, {'code': 'pt', 'name': 'Portuguese'}, {'code': 'pa', 'name': 'Punjabi'}, {'code': 'ro', 'name': 'Romanian'}, {'code': 'ru', 'name': 'Russian'}, {'code': 'sm', 'name': 'Samoan'}, {'code': 'gd', 'name': 'Scots Gaelic'}, {'code': 'sr', 'name': 'Serbian'}, {'code': 'st', 'name': 'Sesotho'}, {'code': 'sn', 'name': 'Shona'}, {'code': 'sd', 'name': 'Sindhi'}, {'code': 'si', 'name': 'Sinhala'}, {'code': 'sk', 'name': 'Slovak'}, {'code': 'sl', 'name': 'Slovenian'}, {'code': 'so', 'name': 'Somali'}, {'code': 'es', 'name': 'Spanish'}, {'code': 'su', 'name': 'Sundanese'}, {'code': 'sw', 'name': 'Swahili'}, {'code': 'sv', 'name': 'Swedish'}, {'code': 'tg', 'name': 'Tajik'}, {'code': 'ta', 'name': 'Tamil'}, {'code': 'tt', 'name': 'Tatar'}, {'code': 'te', 'name': 'Telugu'}, {'code': 'th', 'name': 'Thai'}, {'code': 'tr', 'name': 'Turkish'}, {'code': 'tk', 'name': 'Turkmen'}, {'code': 'uk', 'name': 'Ukrainian'}, {'code': 'ur', 'name': 'Urdu'}, {'code': 'ug', 'name': 'Uyghur'}, {'code': 'uz', 'name': 'Uzbek'}, {'code': 'vi', 'name': 'Vietnamese'}, {'code': 'cy', 'name': 'Welsh'}, {'code': 'xh', 'name': 'Xhosa'}, {'code': 'yi', 'name': 'Yiddish'}, {'code': 'yo', 'name': 'Yoruba'}, {'code': 'zu', 'name': 'Zulu'}, {'code': 'he', 'name': 'Hebrew'}, {'code': 'zh', 'name': 'Chinese (Simplified)'}]}}
dic_final = {}
lista_opcoes = get_languages()
lista = lista_opcoes['data']['languages']

for dicionario in lista:
	codigo = dicionario['code']
	nome = dicionario['name']
	dic_final[nome] = codigo

for key in dic_final.keys():
	print(key)

opcao1 = forca_opcao("Diga a lingua alvo: ",dic_final.keys() )
opcao2 = forca_opcao("Diga a lingua de origem: ",dic_final.keys() )
texto = input("Diga o texto a ser traduzido: ")
# print(dic_final)

texto_traduzido = translate(opcao1, opcao2,texto)
print(f"Texto traduzido: {texto_traduzido}")

'''
# while True:
# 	try:
# 		num = int(input("Diga um numero: "))
# 		break
# 	except:
# 		print("Tem que ser um numero!!!!")
#print(num)

dic = {'sim':'s','não':'n'}
while True:
	try:
		var = input("sim ou não: ")
		print(dic[var])
		break
	except KeyError as e :
		print(e)
		# pass