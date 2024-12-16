from flask import Flask, request, jsonify, render_template
from flask_cors import CORS


from db import get_shows_array_from_rating

app = Flask(__name__)

CORS(app=app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ratings/<rating>', methods=['GET'])
def get_shows_by_rating(rating):
    print(rating)
    shows = get_shows_array_from_rating(rating=float(rating))  # Call the function with the rating
    return jsonify(shows)  # Return the shows as a JSON response

if __name__ == '__main__':
    app.run(debug=True)
