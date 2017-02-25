# Houston Hobby Airport data

For this month's [data jam](https://www.meetup.com/Houston-Data-Visualization-Meetup/events/237127703/), we will be working with data from Monday at the Houston Hobby airport.  This data is sourced from FlightAware's API.

We have the data available in **csv**, each in their respective directories.

## Data

The data are found in the following files:

1. **weather.csv**: weather.csv -- Weather at the airport for the time-period

  |Column|Description|
|----|----------|
|airport| Airport code; will be 'KIAH' for this dataset|
|time| Epoch time ([see here for more info](https://en.wikipedia.org/wiki/Unix_time))|
|cloud_friendly| Cloudy/Clear/Etc.|
|cloud_altitude| Height of clouds (99999 if Clear)|
|cloud_type| Abbreviated Cloud description|
|conditions| None|
|pressure| barometric pressure (inHg)|
|temp_air| air temperature (Celsius)|
|temp_dewpoint| dewpoint (Celsius)|
|temp_relhum| relative humidity|
|visibility| visibility range (statute miles)|
|wind_friendly| e.g. 'Windy'|
|wind_direction| wind direction (knots); 360 means true north|
|wind_speed| wind speeds (knots)|
|wind_speed_gust| gust speeds (knots)|
|raw_data| METAR data used by pilots, e.g.'KIAH 250453Z 36015G22KT 10SM CLR 16/04 A2995 RMK AO2 SLP142 T01610044'|

1. **flights.csv**: flights.csv -- Flight-specific data

  |Column|Description|
|----|----------|
|flight_id| unique flight id string|
|ident| 'ANA7211'|
|actual_ident| 'UAL128'|
|departuretime| Epoch time ([see here for more info](https://en.wikipedia.org/wiki/Unix_time))|
|arrivaltime| Epoch time ([see here for more info](https://en.wikipedia.org/wiki/Unix_time))|
|origin| Origin airport code|
|destination| Destination airport code|
|aircrafttype| Aircraft type (e.g. 'B787')|
|meal_service| 'Business: Dinner / Economy: Dinner'|
|seats_cabin_first| number of passenger seats avail. on flight in first class|
|seats_cabin_business| number of passenger seats avail. on flight in business class|
|seats_cabin_coach| number of passenger seats avail. on flight in coach class|


1. **routes.csv**: flights.csv -- Flight-specific route plan data


|Column|Description|
|----|----------|
|flight_id| unique flight id string|
|order| 1|  -- int starting at 1
|name| e.g. 'KAYEX'|
|type| 'Waypoint'  -- or 'Origin Airport' or 'Reporting Point' or 'VOR-TAC (NAVAID)' or 'Destination Airport' or probably some others|
|latitude| e.g. 36.4875|
|longitude| e.g. -120.9478611|


1. **tracks.csv**: flights.csv -- Flight-specific location tracking data

|Column|Description|
|-----|--------|
|flight_id| unique flight id string|
|timestamp| Epoch time ([see here for more info](https://en.wikipedia.org/wiki/Unix_time))|
|latitude| e.g. 37.63875|
|longitude| e.g. -122.3621|
|groundspeed| ground speed (knots)|
|altitude| altitude (hundreds of feet)|
|altitudeStatus| None|
|updateType| 'TA'|
|altitudeChange| 'C'|
