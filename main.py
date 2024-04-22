from flask import Flask, render_template, request, jsonify, redirect, url_for
import joblib
import pandas as pd
app = Flask(__name__)
model = joblib.load('rf_model_1.joblib')
scaler = joblib.load('scaler.joblib')
@app.route('/')
def home():
    # Render the Index.html template for the home page
    return render_template('Index.html')
@app.route('/test')
def test():
    # Render the Test.html template for the test page
    return render_template('Test.html')
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get JSON data from request
    data_df = pd.DataFrame([data])
    scaled_data = scaler.transform(data_df)
    prediction_proba = model.predict_proba(scaled_data)
    diabetes_proba = prediction_proba[0][1]
    print(diabetes_proba)  # Comment

    # Return predicted value as JSON response
    return jsonify({'diabetes_proba': diabetes_proba})
if __name__ == '__main__':
    app.run(debug=True)






