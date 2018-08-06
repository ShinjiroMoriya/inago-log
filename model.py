import os
import csv
from datetime import datetime


class LogModel:
    def __init__(self):
        self.filename = 'data/' + datetime.now().strftime('%Y-%m-%d') + '.csv'

    def add(self, data: list):
        if not os.path.isdir('data'):
            os.makedirs('data')

        with open(self.filename, 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(data)

    def read(self, key=None) -> dict or str:
        try:
            data = []
            with open(self.filename, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    data.append(row)

            history = {
                'created': int(data[0][0]),
                'buy_vol': float(data[0][1]),
                'sell_vol': float(data[0][2]),
            }
            if key is not None:
                return history[key]
            else:
                return history
        except:
            if key is not None:
                return {}
            else:
                return ''
