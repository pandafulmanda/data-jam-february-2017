import datetime

airports = {
  'Bush': 'KIAH',
  'Hobby': 'KHOU'
}

timestamps = {
  '2017': int(
    datetime.datetime(
      2017, 1, 1,
      tzinfo = datetime.timezone.utc
    ).timestamp()
  ),
  'yesterday': int(
    datetime.datetime(
      2017, 2, 24,
      tzinfo = datetime.timezone.utc
    ).timestamp()
  ),
  'today': int(
    datetime.datetime(
      2017, 2, 25,
      tzinfo = datetime.timezone.utc
    ).timestamp()
  ),
  'span_start': int(
    datetime.datetime(
      2017, 2, 20,
      tzinfo = datetime.timezone.utc
    ).timestamp()
  ),
  'span_end': int(
    datetime.datetime(
      2017, 2, 21,
      tzinfo = datetime.timezone.utc
    ).timestamp()
  )
}

api = {
  'url': 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl',
  'response_limit': 5000
}

