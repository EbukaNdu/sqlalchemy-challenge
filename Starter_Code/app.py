# Import the dependencies


from flask import Flask, jsonify

# Other necessary imports
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Database Setup
# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

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
