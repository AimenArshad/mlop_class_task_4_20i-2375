from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    X = [data['data']]
    prediction = clf.predict(X)[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    clf = joblib.load('model.joblib')
    app.run(debug=True, host='0.0.0.0')
