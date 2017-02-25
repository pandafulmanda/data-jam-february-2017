from constants import airports, timestamps, api
from flightaware.api import FlightAwareSoap

def flatten(lists):
  return [item for items in lists for item in items if len(item) > 0]

class Gatherer:
  def __init__(self, **kwargs):
    self.api      = FlightAwareSoap(**kwargs)
    self.start    = kwargs.get('start') or timestamps.get('span_start')
    self.end      = kwargs.get('end') or timestamps.get('span_end')
    self.airport  = kwargs.get('airport') or airports.get('Hobby')
    self.howMany  = kwargs.get('howMany') or api.get('response_limit')

  def get_flights(self):
    schedule_options = {
      'startDate':    self.start,
      'endDate':      self.end,
      'destination':  self.airport,
      'origin':       '',
      'airline':      '',
      'flightno':     '',
      'howMany':      self.howMany,
      'offset':       0
    }

    flights = self.api.service.AirlineFlightSchedules(**schedule_options).data
    for flight in flights:
      flight.flight_id = self.get_id(flight)

    return flights
 
  def get_id(self, flight):
    try:
      return self.api.service.GetFlightID(ident=flight.ident, departureTime=flight.departuretime)
    except:
      if flight.actual_ident is not None:
        try:
          return self.api.service.GetFlightID(ident=flight.actual_ident, departureTime=flight.departuretime)
        except:
          pass
      print('missing id for ', flight)
      return None

  def get_weather(self):
    weather_options = {
      'airport':      self.airport,
      'startTime':    self.start,
      'howMany':      200,
      'offset':       0
    }
    has_next = True
    data = []

    while has_next:
      response = self.api.service.MetarEx(**weather_options)
      data = data + response.metar
      weather_options['offset'] = response.next_offset
      has_next = response.next_offset != -1 and response.metar[-1].time <= self.end

    return data

  def get_track(self, flightID):

    try:
      reports = self.api.service.GetHistoricalTrack(faFlightID=flightID)

      for report in reports:
        report.flight_id = flightID

      return reports

    except:

      print('missing track for ' + flightID)

      return []


  def get_route(self, flightID):

    try:
      reports = self.api.service.DecodeFlightRoute(faFlightID=flightID).data

      for order, report in enumerate(reports):
        report.flight_id = flightID
        report.order = order

      return reports

    except:

      print('missing route for ' + flightID)

      return []

  def get(self):
    self.flights  = self.get_flights()
    self.tracks   = flatten([self.get_track(flight.flight_id) for flight in self.flights if flight.flight_id is not None])
    self.routes   = flatten([self.get_route(flight.flight_id) for flight in self.flights if flight.flight_id is not None])
    self.weather  = self.get_weather()

    return self
