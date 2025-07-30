import json
import re

with open("submarine_cables.geojson", encoding="utf-8") as f:
    data = json.load(f)

for feature in data["features"]:
    desc = feature["properties"]["description"]
    countries = set()
    # Find the JSON-like list inside the HTML
    matches = re.findall(r'\{\\?"latlon\\?":.*?\\?"name\\?":\\?"(.*?)"', desc)
    for m in matches:
        # split on comma and take the last part as country
        parts = m.split(",")
        if parts:
            country = parts[-1].strip()
            countries.add(country)
    feature["properties"]["countries"] = list(countries)

with open("submarine_cables_fixed.geojson", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
