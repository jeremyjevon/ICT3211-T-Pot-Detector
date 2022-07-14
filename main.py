from flask import Flask, render_template, request, render_template_string
from time import sleep
import os
import pandas

app = Flask(__name__)

TABLE_TEMPLATE = """
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
<table style="width: 100%">
	<thead>
		<th>Detector Selected</th>
    	<th>Output</th>
    </thead>
    <tbody>
    	{% for row in log %}
    	<tr>
        	<td>{{ row.detector }}</td>
        	<td>{{ row.output }}</td>
      	</tr>
     	{% endfor %}
    </tbody>
</table>
"""

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/log')
def log():
	logging = []
	with open("output.txt", "r") as f:
	    for line in f.readlines():
	        logging.append(line.rstrip()) 
	return render_template("log.html", logging=logging)


	# keys = ['detector', 'output']
	# log = []
	# with open('output.txt', 'r') as f:
	# 	for line in f:
	# 		row = line.split()
	# 		log.append(dict(zip(keys, [row[0], row[-1]])))
	# return render_template_string(TABLE_TEMPLATE, log=log)

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

	os_cmd0 = os.chdir("../ict3211-t-pot-detector")
	with open("output.txt", "w+") as f:
		f.write("Honeypot IP Address: " + ip_address + "\n")
		f.write("Detectors Selected: " + detectors + "\n")
		f.write(os_cmd2)
		f.write(os_cmd4)
		f.write(os_cmd6)
		f.write(os_cmd8)
		f.write(os_cmd10)
		f.close()

	# def generate():
	# 	with open("output.txt") as f:
	# 		while True:
	# 			yield f.read()
	# 			sleep(1)

	# return app.response_class(generate(), mimetype='text/plain')

	return render_template("process.html")
