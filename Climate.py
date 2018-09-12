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

#This last one ended up being very confusing
# try:
# 	@app.route("/api/v1.0/<start>/<end>")
# 	def start_end():
# 		s = input("Input a start date")
# 		e = input("Input an end date (optional)")
# 		if e == '':
# 			@app.route("/api/v1.0/<start>")
# 			def start():
# 				temps = session.query(
# 				func.min(Measurement.tobs),
# 				func.max(Measurement.tobs),
# 				func.avg(Measurement.tobs)).filter(Measurement.date >= s).all()
# 		else:
# 			temps = session.query(
# 				func.min(Measurement.tobs),
# 				func.max(Measurement.tobs),
# 				func.avg(Measurement.tobs)).filter(Measurement.date >= s & Measurement.date <= e).all()
# except TypeError:

if __name__=='__main__':
	app.run(debug=True)