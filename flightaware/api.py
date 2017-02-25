import os
from dotenv import load_dotenv

from requests import Session
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from zeep import Client
from zeep.transports import Transport

from constants import api

# copy the ../.env.sample to ../.env and add necessary info.
dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path)

USERNAME = os.environ.get('FLIGHTAWARE_USERNAME')
API_KEY  = os.environ.get('FLIGHTAWARE_API_KEY')

class FlightAwareSoap(Client):
  def __init__(self, **kwargs):
    session = Session()
    session.auth = HTTPBasicAuth(
      kwargs.get('username') or USERNAME,
      kwargs.get('api_key') or API_KEY
    )
    super(FlightAwareSoap, self).__init__(
      kwargs.get('url') or api.get('url'),
      transport=Transport(session=session)
    )
    self.service.SetMaximumResultSize(max_size = api.get('response_limit'))
