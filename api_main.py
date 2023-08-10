from flask import Flask, request, jsonify, send_file,send_from_directory

from io import BytesIO
import os
import random
import datetime

app = Flask(__name__)

# for the simulation I'm assuming that there is 50% chance that, the xml file is ready between hh:15 and hh:20->50% total
# for the simulation I'm assuming that there is 30% chance that, the xml file is ready between hh:20 and hh:30->80% total
# for the simulation I'm assuming that there is 20% chance that, the xml file is ready between hh:30 and hh:45->100% total
def xml_is_ready():
    if(15 <= datetime.datetime.now().minute <= 20 and random.random() < 0.5):
        return True
    elif(20 < datetime.datetime.now().minute <= 30 and random.random() < 0.8):
        return True
    elif(30 < datetime.datetime.now().minute <= 45):
        return True
    else:
        return False

#we are returning the xml file, where filexx.xml, datetime.hour % 16 = xx (because I have 16 xml file)
@app.route("/get_xml/", methods=['GET'])
def get_xml():
    if(xml_is_ready()):
        xml_file_path = f'xmls/file{datetime.datetime.now().hour % 16}.xml'
        return send_file(xml_file_path, mimetype='text/xml')
    else:
        return "Xml file is not available yet!"



if __name__ == "__main__":
    app.run(debug=True)
