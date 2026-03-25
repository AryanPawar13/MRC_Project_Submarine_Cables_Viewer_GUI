# MRC_Project_Submarine_Cables_Viewer_GUI

# 🌐 Submarine Cables Viewer Tool

## 🛰️ Overview
This is an interactive web-based GIS tool designed to **visualize, analyze, and plan submarine cable infrastructure** with environmental and geostrategic awareness in mind. Built as part of the Maritime Research Centre’s Underwater Domain Awareness (UDA) initiative, the tool overlays **critical undersea data layers**—such as existing submarine cables, marine protected areas, coral reefs, and tectonic fault lines—on a global base map using Leaflet.js.

## 🚀 Features
- 🌍 High-resolution global satellite basemap
- 🧭 Toggleable data layers:
  - Submarine Cables
  - Warm-Water Coral Reefs
  - Cold-Water Coral Reefs (IOR region only)
  - Marine Protected Areas (MPAs)
  - Earthquake Fault Lines
- 🔍 Interactive popups with metadata for each feature
- 📦 Fast loading with optimized GeoJSON files
- 🗺️ Restricted world bounds to prevent infinite panning
- 📐 Modular and scalable design for future marine datasets


## 🛠️ Tech Stack
**Frontend**
- HTML, CSS, JavaScript
- [Leaflet.js](https://leafletjs.com) for interactive mapping

**Backend**
- Python with [Flask](https://flask.palletsprojects.com/) for serving data and templates

**Data Formats**
- GeoJSON for vector layers
- PNG/GeoTIFF planned (for seabed suitability overlays)

**Deployment**
- Currently local (can be deployed to [PythonAnywhere](https://www.pythonanywhere.com/) or [Heroku](https://www.heroku.com/))

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/submarine-cables-viewer.git
   cd submarine-cables-viewer

2. Create a virtual environment (optional but recommended):
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
    ```bash
    pip install Flask

4. Run the app:
    ```bash
    python app.py

5. Open your browser and visit:
   ```cpp
   http://127.0.0.1:5000/

## 📊 Datasets Used
  **Layer**                                   **Source**
- Submarine Cables	                Modified from TeleGeography [https://www.submarinecablemap.com/]
- Warm-Water Coral Reefs	          UNEP-WCMC (2025). Ocean+ Habitats [habitats.oceanplus.org]
- Cold-Water Coral Reefs	          Subset clipped from above (IOR-specific)
- Marine Protected Areas	          UNEP-WCMC and IUCN (2025), WDPA, [protectedplanet.net]
- Earthquake Fault Lines	          GEM Global Active Faults Database – Styron & Pagani (2020)

## Citations
- UNEP-WCMC (2025). Ocean+ Habitats [On-line], [July 2025]. Available at: https://habitats.oceanplus.org

- UNEP-WCMC and IUCN (2025). Protected Planet: The World Database on Protected Areas (WDPA). [July 2025]. Available at: https://www.protectedplanet.net

- Styron, R., & Pagani, M. (2020). The GEM Global Active Faults Database. Earthquake Spectra, 36(1_suppl), 160–180. doi:10.1177/8755293020944182

- Cable data parsed from: Modified from TeleGeography [https://www.submarinecablemap.com/]

## 💡 Applications
- Strategic planning for new submarine cable routes

- Avoidance of ecologically sensitive areas (corals, MPAs)

- Assessment of proximity to seismic hazard zones

- Training and awareness tool for policymakers, Navy, and infrastructure agencies

- Foundation for future real-time surveillance layers and route optimization

## 🚧 Limitations & Future Improvements
- Cold coral full dataset (9.5MB) was too large for browser rendering; subset clipped

- Not yet deployed on cloud platforms

- Seabed suitability layer is currently disabled due to performance/alignment issues

- Plans to integrate dynamic APIs and user route uploads in future iterations

## 🙌 Acknowledgments
- Maritime Research Centre (MRC), Pune

- Internship Mentor – [Romit Kaware]

- UDA Strategic Framework – Dr. (Cdr.) Arnab Das
