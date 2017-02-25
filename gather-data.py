from ipdb import set_trace
import flightaware

import csv

def write_to_csv(data, name):
  data_for_name = data.__getattribute__(name)
  with open(name + '.csv', 'w') as csvfile:
    fieldnames = data_for_name[0].__dict__.get('__values__').keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data_for_name:
      writer.writerow(row.__dict__.get('__values__')) 


flight_data = flightaware.Gatherer()
flight_data.get()

topics = ['weather', 'flights', 'routes', 'tracks']

[write_to_csv(flight_data, topic) for topic in topics]
