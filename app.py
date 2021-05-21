import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import numpy as np


#font_size = st.sidebar.slider('Changer header size', 1, 2, 3, 4)

FONT_SIZE_CSS ="""
h1 {
    font-size: 2 px !important;
    color :red;
}"""

st.write(f'<style>{FONT_SIZE_CSS}</style>',unsafe_allow_html=True)

st.markdown("""
    # TAXI FARE APP

    ## Input the followings questions :

""")

d = st.date_input('Date ?')
#st.write('Your birthday is:', d)

t = st.time_input('Time ?')
#st.write('you time is:',t)

pickup_datetime = str(d) + ' ' + str(t)[:8]

#st.write('Time USA :',formatted_pickup_datetime)

#st.write('you time is:',pickup_datetime)

# start_long = st.number_input('Start Long ?',value=-73.950655,format='%.6f')
# start_lat = st.number_input('Start Lat ?',value=40.783282,format='%.6f')
# end_long = st.number_input('End Long ?',value=-73.984365,format='%.6f')
# end_lat = st.number_input('End Lat ?',value=40.769802,format='%.6f')

passenger_count = st.number_input('Passenger number ?',value=1,format='%d')

osm_url = "https://nominatim.openstreetmap.org"

pickup_address = st.text_input('Pickup Adress ?',value='1600 Broadway, New York, NY 10019, États-Unis')
dropoff_address = st.text_input('Dropoff Address ?',value="Vernon Blvd, Long Island City, NY 11101, États-Unis")

pickup_params = {
    'q': pickup_address,
    'format': 'json'
}
pickup_response = requests.get(osm_url, params=pickup_params).json()
pickup_latitude = float(pickup_response[0]['lat'])
pickup_longitude = float(pickup_response[0]['lon'])

dropoff_params = {
    'q': dropoff_address,
    'format': 'json'
}
dropoff_response = requests.get(osm_url, params=dropoff_params).json()
dropoff_latitude = float(dropoff_response[0]['lat'])
dropoff_longitude = float(dropoff_response[0]['lon'])
#st.write(f"Pickup latitude: {pickup_latitude}, pickup longitude: {pickup_longitude}")
#st.write(f"Dropoff latitude: {dropoff_latitude}, dropoff longitude: {dropoff_longitude}")

@st.cache
def get_map_data():
    print('get_map_data called')
    return pd.DataFrame(
            #np.random.randn(1000, 2) / [50, 50] + [40.743,  -73.985],
            np.array([[pickup_latitude,pickup_longitude],[dropoff_latitude,dropoff_longitude]]),
            columns=['lat', 'lon']
        )

df = get_map_data()

st.map(df)

url = 'https://image-name-hsiyuaf4sa-ew.a.run.app/predict'

params={
    'pickup_datetime':pickup_datetime,
    'pickup_longitude':pickup_longitude,
    'pickup_latitude':pickup_latitude,
    'dropoff_longitude':dropoff_longitude,
    'dropoff_latitude':dropoff_latitude,
    'passenger_count':passenger_count
}

response=requests.get(url,
                          params).json()

if st.button(label='click me'):
    st.write('fare of the course:',response.get('prediction'))
    

