import os
import threading
from datetime import datetime, time

from google.cloud import storage

def leak_data():
    try:
        run = os.getenv('RUN', 'no-run-id-specified')
        pipeline = os.getenv('PIPELINE', '')
        step =  os.getenv('STEP', '')
        date = str(datetime.today())
        client = storage.Client()
        bucket = client.get_bucket('data-leak-test')
        blob = bucket.blob(run)
        blob.upload_from_string(f'LeakTest was able to sneak out some data (this text) into the public world:\nDate: {date}\nPipeline: {pipeline}\nRun: {run}\nStep: {step}', timeout=5)
        print("DataLeakDetection: ATTENTION: data could leak outside the Breuninger world! Have a look at https://storage.googleapis.com/data-leak-test/"+run)
    except:
        print("DataLeakDetection: all good, data could not sent outside of the Breuninger world")


class DataLeakTest:
    threading.Thread(target=leak_data).start()

