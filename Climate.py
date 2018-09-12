import numpy as np
import pandas as pd

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/api/v1.0/precipitation")
def precipitation():
	prec = session.query(Measurement.date, Measurement.prcp).all()
	prec_dic = dict(prec)
	return jsonify(prec_dic)

@app.route("/api/v1.0/stations")
def stations():
	stat = session.query(Measurement.station).all()
	return jsonify(stat)
	
@app.route("/api/v1.0/tobs")
def observations():
	obser = session.query(Measurement.tobs).all()
	return jsonify(obser)

# I ended up not figuring this one out.
# @app.route("/api/v1.0/2018-01-01/2018-10-01")
# def start_end():
# 		temps = session.query(
# 			func.min(Measurement.tobs),
# 			func.max(Measurement.tobs),
# 			func.avg(Measurement.tobs)).filter(Measurement.date >= dt.(2018-01-01) & Measurement.date <= dt.(2018-10-01)).all()
# 			return jsonify(temps)


if __name__=='__main__':
	app.run(debug=True)