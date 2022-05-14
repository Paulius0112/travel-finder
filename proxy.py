from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from api.skyscanner import SkyScannerAPI


# app = Flask(__name__)

# countries = [
#     {"id": 1, "name": "labas"}
# ]

# @app.get("/countries")
# def get_countries():
#     return jsonify(countries)

scanner = SkyScannerAPI()

scanner.get_flights("Germany")


