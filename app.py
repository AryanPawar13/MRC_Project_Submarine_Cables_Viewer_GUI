from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# this serves the GeoJSON file from your local data folder
@app.route("/data/submarine_cables_fixed.geojson")
def cables():
    return send_from_directory('data', 'submarine_cables_fixed.geojson')

@app.route("/data/new_cold_corals_ior.geojson")
def cold_corals():
    return send_from_directory('data',"new_cold_corals_ior.geojson")

@app.route("/data/warm_water_corals.geojson")
def warm_water_corals():
    return send_from_directory('data',"warm_water_corals.geojson")

@app.route("/data/MPA0.geojson")
def MPA1():
    return send_from_directory('data',"MPA0.geojson")

@app.route("/data/MPA11.geojson")
def MPA2():
    return send_from_directory('data',"MPA11.geojson")

@app.route("/data/MPA22.geojson")
def MPA3():
    return send_from_directory('data',"MPA22.geojson")

@app.route("/data/earthquake_active_faults.geojson")
def earthquake():
    return send_from_directory('data',"earthquake_active_faults.geojson")

if __name__ == "__main__":
    app.run(debug=True)