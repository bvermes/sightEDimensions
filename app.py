import requests
import database
import psycopg2
import schedule
import threading
import time
api_url = "http://127.0.0.1:5000"
import pause
from datetime import datetime
import json
import xml.etree.ElementTree as ET

def get_xml():
    response = requests.get(f'{api_url}/get_xml/')

    if response.status_code == 200:
        # the get call was successful, now we need to check the format
        # the expected is xml, but we can prepare the software to be able to receive json too
        content_type = response.headers.get("Content-Type", "")
        if "xml" in content_type:
            try:
                xml_content = response.content  # XML content in bytes
                xml_text = xml_content.decode('utf-8')  # Convert bytes to string
                database.loaddata(xml_text)
            except ET.ParseError:
                print("Invalid Xml content")

        elif "json" in content_type:
            try:
                json_data = json.loads(response.content)
                database.loaddata(json_data)
            except json.JSONDecodeError:
                print("Invalid JSON content")

        elif isinstance(content_type, str):
            print("Content is string")
            print('Message: ', response.content.decode())

        else:
            print("Invalid content type")

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

def schedule_requests():
    while True:
        schedule.run_pending()
        time.sleep(10)
    # Schedule requests every hour
    for hour in range(24):
        schedule.every().hour.at(f"{hour:02}:15").do(
            lambda: get_xml(),
            print(f"Scheduled request at {hour:02}:15"))
        schedule.every().hour.at(f"{hour:02}:21").do(
            lambda: get_xml(),
            print(f"Scheduled request at {hour:02}:21"))
        schedule.every().hour.at(f"{hour:02}:31").do(
            lambda: get_xml(),
            print(f"Scheduled request at {hour:02}:31"))

#def schedule_requests():
#    # Schedule requests every hour
#    for hour in range(24):
#        pause.until(datetime(datetime.now().year, datetime.now().month, datetime.now().date, hour, 15, 1))
#        get_xml()
#        print(f"Scheduled request at {hour:02}:15")
#        pause.until(datetime(datetime.now().year, datetime.now().month, datetime.now().date, hour, 21, 1))
#        get_xml()
#        print(f"Scheduled request at {hour:02}:21")
#        pause.until(datetime(datetime.now().year, datetime.now().month, datetime.now().date, hour, 31, 1))
#        get_xml()
#        print(f"Scheduled request at {hour:02}:31")


def menu():
    database.create_table()

    while True:
        print("\n Menu:")
        print("1. Schedule requests")
        print("2. Get data from database")
        print("3. Try getting xml directly")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            schedule_requests()
            print("Requests scheduled.")
        elif choice == "2":
            print(database.get_dimensions())
        elif choice == "3":
            get_xml()
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    threading.Thread(target=menu).start()
    threading.Thread(target=schedule_requests).start()
