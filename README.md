# ICT3211-T-Pot-Detector
ITP IS Team 1

# Setting Up Python Virtual Environment
```
python3 -m venv virtual
source virtual/bin/activate
pip3 install -r requirements.txt
```
Ensure that all detector requirements have been installed in the virtual environment before proceeding to the next step.

# Running Flask Web UI
```
export FLASK_ENV=development
export FLASK_APP=main.py
flask run
```
