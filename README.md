# ICT3211-T-Pot-Detector

T-Pot Detector is an integrated honeypot detector web application that allows users to conduct scans on a specific IP address using different combinations of honeypot detectors.

The list of honeypot detectors and their detection services include:

| Honeypot Detector | Service |
| --- | --- |
| Checkpot | FTP, Telnet, HTTP |
| Honeybee | HTTP |
| Detect-Kippo-Cowrie | SSH |
| Honeydetect | SSH, Telnet |
| Yogi | SSH |

# Setting Up Python Virtual Environment
```
python3 -m venv virtual
source virtual/bin/activate
pip3 install -r requirements.txt
```
Ensure that all detector requirements have been installed in the virtual environment before proceeding to the next step.

# Running Flask Web UI in Python Virtual Environment
```
export FLASK_ENV=development
export FLASK_APP=main.py
flask run
```


# YouTube Demonstration
[![video](https://user-images.githubusercontent.com/27985157/180927803-df775343-adc1-4ba3-834a-a90ab1b1f33d.png)](https://youtu.be/W-qPCB0nstA)

# User Interface
![Home](https://user-images.githubusercontent.com/27985157/180927130-66e0816b-7d3e-4d9c-8968-648d6213dc1a.png)
![Logs](https://user-images.githubusercontent.com/27985157/180927139-2ade6edd-3335-463c-91d7-dc6b15944062.png)
![About](https://user-images.githubusercontent.com/27985157/180927149-27f59282-b861-48b0-90a0-1e76181169c1.png)
![Credits](https://user-images.githubusercontent.com/27985157/180927155-1001654f-0612-4f43-9564-08047ea54ebb.png)
