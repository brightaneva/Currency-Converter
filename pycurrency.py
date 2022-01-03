import requests
import json


#UNIVERSAL VARIABLES
API_KEY = "0bad105e04f4e53dfc232b13"
URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
URL_CODES = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"


class Currency_Converter:
	"""convert any convercy"""

	def __init__(self):
		self.data = requests.get(URL).json()
		
		#assign need info to varible
		self.base_curruncy = self.data['base_code']
		self.currencies = self.data['conversion_rates']


	def convert(self, from_currency, to_currency, amount): 		
		"""returns amout of needed currency"""

		#first convert it into USD if it is not in USD.
		# because our base currency is USD
		if from_currency != 'USD' : 
			convert2_base = amount / self.currencies[from_currency] 
	  
		# return only 4 decimal places 
		amount_figure = round(convert2_base * self.currencies[to_currency], 4)
		amount_figure = f"{to_currency} {amount_figure}"
		
		return {
			"from_currency" : from_currency,
			"base_curruncy" : self.base_curruncy,
			"to_currency" : to_currency,  
			"input_amount" : amount,
			"result" : amount_figure
		}





if __name__ == "__main__":
	converter = Currency_Converter()
	print("\n\n")
	print(converter.convert('GHS','NGN',100))