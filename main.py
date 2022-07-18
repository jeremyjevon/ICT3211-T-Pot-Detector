from flask import Flask, render_template, request, render_template_string
from time import sleep
import os
import pandas

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/log')
def log():
	logging = []
	log_ip = []
	log_detectors = []

	with open("output.txt", "r") as f:
	    for line in f.readlines():
	        logging.append(line.rstrip())
	    f.close()

	with open("ip.txt", "r") as f:
	    for line in f.readlines():
	        log_ip.append(line.rstrip())
	    f.close()

	with open("detectors.txt", "r") as f:
	    for line in f.readlines():
	        log_detectors.append(line.rstrip())
	    f.close()

	return render_template("log.html", logging=logging, log_ip=log_ip, log_detectors=log_detectors)

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/credits')
def credits():
	return render_template("credits.html")

@app.route('/process', methods=["POST"])
def process():
	ip_address = request.form.get("ip_address")
	detectorArray = request.form.getlist('check')
	detectors = (", ".join(detectorArray))
	
	os_cmd3 = os_cmd5 = os_cmd7 = os_cmd9 = os_cmd11 = " "

	if 'checkpot' in detectorArray: 
		os_cmd2 = os.chdir("../checkpot")
		os_cmd3 = os.popen("python3 checkpot.py -t " + ip_address + " -l 3").read()
	if 'honeybee' in detectorArray: 
		os_cmd4 = os.chdir("../honeybee")
		os_cmd5 = os.popen("python3 glastopf.py " + ip_address).read()
	if 'detect-kippo-cowrie' in detectorArray: 
		os_cmd6 = os.chdir("../detect-kippo-cowrie")
		os_cmd7 = os.popen("python3 detectKippoCowrie.py " + ip_address + " 22").read()
	if 'honeydetect' in detectorArray: 
		os_cmd8 = os.chdir("../honeydetect")
		with open("addresses.txt", "w+") as f:
			f.write(ip_address)
			f.close()
		os_cmd9 = os.popen("./honeydetect").read()
	if 'yogi' in detectorArray: 
		os_cmd10 = os.chdir("../yogi")
		with open("host_list.txt", "w+") as f:
			f.write(ip_address)
			f.close()
		os_cmd11 = os.popen("python3 yogi.py").read()

	os_cmd0 = os.chdir("../ICT3211-T-Pot-Detector")
	with open("ip.txt", "w+") as f:
		f.write(ip_address)
		f.close()

	os_cmd1 = os.chdir("../ICT3211-T-Pot-Detector")
	with open("detectors.txt", "w+") as f:
		f.write(detectors)
		f.close()

	os_cmd0 = os.chdir("../ICT3211-T-Pot-Detector")
	with open("output.txt", "w+") as f:
		f.write(os_cmd3)
		f.write(os_cmd5)
		f.write(os_cmd7)
		f.write(os_cmd9)
		f.write(os_cmd11)
		f.close()

	return render_template("process.html")
