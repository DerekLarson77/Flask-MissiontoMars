from flask import Flask, jsonify, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.scrape_data
produce = db.produce

@app.route("/scrape")
def scrape():


@app.route("/")
def home():