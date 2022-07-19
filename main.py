from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/log')
def log():
	log_ip = []
	log_detectors = []
	log_checkpot = []
	log_honeybee = []
	log_detectkippocowrie = []
	log_honeydetect = []
	log_yogi = []
	header_checkpot = []
	header_honeybee = []
	header_detectkippocowrie = []
	header_honeydetect = []
	header_yogi = []

	if os.stat("log_checkpot.txt").st_size != 1:
		header_checkpot.append("Checkpot")
	if os.stat("log_honeybee.txt").st_size != 1:
		header_honeybee.append("Honeybee")
	if os.stat("log_detectkippocowrie.txt").st_size != 1:
		header_detectkippocowrie.append("Detect-Kippo-Cowrie")
	if os.stat("log_honeydetect.txt").st_size != 1:
		header_honeydetect.append("Honeydetect")
	if os.stat("log_yogi.txt").st_size != 1:
		header_yogi.append("Yogi")

	with open("log_ip.txt", "r") as f:
	    for line in f.readlines():
	        log_ip.append(line.rstrip())
	    f.close()

	with open("log_detectors.txt", "r") as f:
	    for line in f.readlines():
	        log_detectors.append(line.rstrip())
	    f.close()

	with open("log_checkpot.txt", "r") as f:
	    for line in f.readlines():
	        log_checkpot.append(line.rstrip())
	    f.close()

	with open("log_honeybee.txt", "r") as f:
	    for line in f.readlines():
	        log_honeybee.append(line.rstrip())
	    f.close()

	with open("log_detectkippocowrie.txt", "r") as f:
	    for line in f.readlines():
	        log_detectkippocowrie.append(line.rstrip())
	    f.close()

	with open("log_honeydetect.txt", "r") as f:
		    for line in f.readlines():
		        log_honeydetect.append(line.rstrip())
		    f.close()

	with open("log_yogi.txt", "r") as f:
	    for line in f.readlines():
	        log_yogi.append(line.rstrip())
	    f.close()

	return render_template("log.html", log_ip=log_ip, log_detectors=log_detectors, header_checkpot=header_checkpot, header_honeybee=header_honeybee, header_detectkippocowrie=header_detectkippocowrie, header_honeydetect=header_honeydetect, header_yogi=header_yogi, log_checkpot=log_checkpot, log_honeybee=log_honeybee, log_detectkippocowrie=log_detectkippocowrie, log_honeydetect=log_honeydetect, log_yogi=log_yogi)

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
	
	os_cmd1 = os_cmd2 = os_cmd3 = os_cmd4 = os_cmd5 = " "

	if 'checkpot' in detectorArray: 
		os.chdir("../checkpot")
		os_cmd1 = os.popen("python3 checkpot.py -t " + ip_address + " -l 3").read()
	if 'honeybee' in detectorArray: 
		os.chdir("../honeybee")
		os_cmd2 = os.popen("python3 glastopf.py " + ip_address).read()
	if 'detect-kippo-cowrie' in detectorArray: 
		os.chdir("../detect-kippo-cowrie")
		os_cmd3 = os.popen("python3 detectKippoCowrie.py " + ip_address + " 22").read()
	if 'honeydetect' in detectorArray: 
		os.chdir("../honeydetect")
		with open("addresses.txt", "w+") as f:
			f.write(ip_address)
			f.close()
		os_cmd4 = os.popen("./honeydetect").read()
	if 'yogi' in detectorArray: 
		os.chdir("../yogi")
		with open("host_list.txt", "w+") as f:
			f.write(ip_address)
			f.close()
		os_cmd5 = os.popen("python3 yogi.py").read()

	os.chdir("../ict3211-t-pot-detector")

	with open("log_ip.txt", "w+") as f:

		f.write(ip_address)
		f.close()

	with open("log_detectors.txt", "w+") as f:
		f.write(detectors)
		f.close()

	with open("log_checkpot.txt", "w+") as f:
		f.write(os_cmd1)
		f.close()

	with open("log_honeybee.txt", "w+") as f:
		f.write(os_cmd2)
		f.close()

	with open("log_detectkippocowrie.txt", "w+") as f:
		f.write(os_cmd3)
		f.close()

	with open("log_honeydetect.txt", "w+") as f:
		f.write(os_cmd4)
		f.close()

	with open("log_yogi.txt", "w+") as f:
		f.write(os_cmd5)
		f.close()

	return render_template("process.html")
