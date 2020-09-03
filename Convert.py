import requests as r

class Currency_convertor: 

    rates = {}  
    def __init__(self, url): 
        data = r.get(url).json() 
        self.rates = data["rates"]  

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'EUR' : 
            amount = amount / self.rates[from_currency] 

        amount = round(amount * self.rates[to_currency], 2) 
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency)) 

if __name__ == "__main__": 
    url = str.__add__('http://data.fixer.io/api/latest?access_key=fa2382d8f42c76563e49c13742e1613e')   
    c = Currency_convertor(url) 
    dari_negara = input("Dari mata uang?(cth:usd): ").upper()
    ke_negara= input("Ke mata uang?(cth:idr): ").upper()
    amount = int(input("Amount: ")) 
    c.convert(from_country, to_country, amount)
