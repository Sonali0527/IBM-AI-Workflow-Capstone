from flask import Flask, request, jsonify
import logging
from model import load_model, predict_revenue

app = Flask(__name__)

# Logging setup Q3
logging.basicConfig(filename='logs/app.log', level=logging.INFO)
logger = logging.getLogger()

try:
    model = load_model()
except:
    model = None
    logger.warning("Model not found, using dummy")

@app.route('/')
def home():
    return "<h3>AAVAIL Revenue Prediction API</h3><p>Use POST /predict with {country, date}</p>"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        country = data.get('country')
        date = data.get('date')

        if not country or not date:
            return jsonify({"error": "country and date required"}), 400

        revenue = predict_revenue(model, country, date) if model else 15000.5

        logger.info(f"Prediction: country={country}, date={date}, revenue={revenue}")

        return jsonify({
            "country": country,
            "date": date,
            "predicted_revenue": revenue
        })
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
