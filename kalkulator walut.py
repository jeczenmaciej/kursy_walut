from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def get_exchange_rates():
    with open('exchange_rates.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        return [row for row in reader]

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        currency_code = request.form.get('currency')
        amount = float(request.form.get('amount'))
        
        rates = get_exchange_rates()
        exchange_rate = None
        for rate in rates:
            if rate['code'] == currency_code:
                exchange_rate = float(rate['ask'])
                break
        
        if exchange_rate is None:
            return "Nie znaleziono kursu dla podanej waluty."
        
        cost_pln = amount * exchange_rate
        return f"Koszt wymiany to {cost_pln:.2f} PLN."

    rates = get_exchange_rates()
    return render_template("calculator.html", rates=rates)

if __name__ == "__main__":
    app.run(debug=True)