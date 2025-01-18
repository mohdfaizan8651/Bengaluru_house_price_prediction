from flask import Flask, request, jsonify, render_template
import utils
app = Flask(__name__)



@app.route('/')
def base():
    return render_template('index.html')


@app.route('/get_location_names')
def get_location_names_():
    responce = jsonify({
        'location':utils.get_location_names()
    })
    return responce



@app.route('/predict_home_price', methods=['POST'])
def predict_home_price_():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    responce = jsonify({
        'estimated_price':utils.get_estimate_price(location,total_sqft,bhk,bath)
    })

    responce.headers.add('Access-Control-Allow-origin',' *')
   
    return responce
    

if __name__=="__main__":
    print("Starting server")
    utils.load_sevaed_artifacts()
    app.run(debug=True)