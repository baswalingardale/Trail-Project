from flask import Flask, request, render_template, json
import pickle

app = Flask(__name__)


with open('car_price_model.pkl', 'rb') as file_obj:
    car_price_ml_model = pickle.load(file_obj)

@app.route('/')
def home():
    return render_template('home.html')


@app.route("/car_price", methods=['POST', 'GET'])
def car_price():

    data = request.form

    price = car_price_ml_model.predict([[data['brand'], data['km_driven'], data['fuel type'], data['owner']]])

    return render_template("result page.html", result=round(price[0]))

# Initiating the application
if __name__ == '__main__':
    
    # Running the application and leaving the debug mode ON
    app.run(debug=True, port=8000)