import os
import threading
from datetime import datetime, time

import requests
from google.cloud import storage

def leak_data():
    try:
        print("DataLeakDetection: Testing access to internet.")
        r = requests.get('https://www.google.de')
        print(f"DataLeakDetection: Status code: {r.status_code}")
        if r.status_code == 200:
            print("DataLeakDetection: Try leaking data...")
            run = os.getenv('RUN', 'no-run-id-specified')
            pipeline = os.getenv('PIPELINE', '')
            step =  os.getenv('STEP', '')
            date = str(datetime.today())
            client = storage.Client()
            bucket = client.get_bucket('data-leak-test')
            blob = bucket.blob(run)
            blob.upload_from_string(f'LeakTest was able to sneak out some data (this text) into the public world:\nDate: {date}\nPipeline: {pipeline}\nRun: {run}\nStep: {step}')
            print("DataLeakDetection: ATTENTION: data could leak outside the Breuninger world! Have a look at https://storage.googleapis.com/data-leak-test/"+run)
    except:
        print("DataLeakDetection: all good, could not sent data outside of the Breuninger world")


class DataLeakTest:
    threading.Thread(target=leak_data).start()

