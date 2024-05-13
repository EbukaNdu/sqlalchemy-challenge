# Import the dependencies
from flask import Flask, jsonify

# Other necessary imports
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Database Setup
# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///C:/Users/nduag/OneDrive/Documents/data boot camp/sqlalchemy-challenge/sqlalchemy-challenge/Starter_Code/Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Add precipitation route logic here
    pass

@app.route("/api/v1.0/stations")
def stations():
    # Add stations route logic here
    pass

@app.route("/api/v1.0/tobs")
def tobs():
    # Add tobs route logic here
    pass

@app.route("/api/v1.0/<start>")
def start_date(start):
    # Add start date route logic here
    pass

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    # Add start and end date route logic here
    pass

if __name__ == '__main__':
    app.run(debug=True)


# API Static and Dynamic Routes 
@app.route("/")
def home():
    """List all available routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return JSON representation of precipitation data for the last year."""
    # Query precipitation data for the last year
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()
    # Convert to dictionary with date as key and precipitation as value
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return JSON list of stations."""
    # Query stations
    stations_data = session.query(Station.station, Station.name).all()
    # Convert to list of dictionaries
    stations_list = [{"Station": station, "Name": name} for station, name in stations_data]
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return JSON list of temperature observations for the last year at the most active station."""
    # Query temperature observations for the last year at the most active station
    tobs_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station_id).\
        filter(Measurement.date >= one_year_ago).all()
    # Convert to list of dictionaries
    tobs_list = [{"Date": date, "Temperature": tobs} for date, tobs in tobs_data]
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start_date(start):
    """Return JSON list of min, avg, and max temperatures from a start date to the end of the dataset."""
    # Query temperature statistics from start date to the end of the dataset
    temp_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    # Convert to dictionary
    temp_stats_dict = {"Min Temperature": temp_stats[0][0],
                       "Avg Temperature": temp_stats[0][1],
                       "Max Temperature": temp_stats[0][2]}
    return jsonify(temp_stats_dict)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    """Return JSON list of min, avg, and max temperatures for a specified date range."""
    # Query temperature statistics for the specified date range
    temp_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    # Convert to dictionary
    temp_stats_dict = {"Min Temperature": temp_stats[0][0],
                       "Avg Temperature": temp_stats[0][1],
                       "Max Temperature": temp_stats[0][2]}
    return jsonify(temp_stats_dict)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

