from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/log')
def log():
	return render_template("log.html")

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
	
	os_cmd2 = os_cmd4 = os_cmd6 = os_cmd8 = os_cmd10 = " "

	if 'checkpot' in detectorArray: 
		os_cmd1 = os.chdir("../checkpot")
		os_cmd2 = os.popen("python3 checkpot.py -t " + ip_address + " -l 3").read()
	if 'honeybee' in detectorArray: 
		os_cmd3 = os.chdir("../honeybee")
		os_cmd4 = os.popen("python3 glastopf.py " + ip_address).read()
	if 'detect-kippo-cowrie' in detectorArray: 
		os_cmd5 = os.chdir("../detect-kippo-cowrie")
		os_cmd6 = os.popen("python3 detectKippoCowrie.py " + ip_address + " 22").read()
	if 'honeydetect' in detectorArray: 
		os_cmd7 = os.chdir("../honeydetect")
		with open("addresses.txt", "w+") as f:
			f.write(ip_address)
			f.close()
		os_cmd8 = os.popen("./honeydetect").read()
	if 'yogi' in detectorArray: 
		os_cmd9 = os.chdir("../yogi")
		with open("host_list.txt", "w+") as f:
			f.write(ip_address)
			f.close()
		os_cmd10 = os.popen("python3 yogi.py").read()

	os_cmd0 = os.chdir("../flaskapp")
	with open("Output.txt", "w+") as f:
		f.write("Honeypot IP Address: " + ip_address + "\n")
		f.write("Detectors Selected: " + detectors + "\n")
		f.write(os_cmd2)
		f.write(os_cmd4)
		f.write(os_cmd6)
		f.write(os_cmd8)
		f.write(os_cmd10)
		f.close()

	return render_template("process.html", ip_address=ip_address)
