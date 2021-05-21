import streamlit as st
import requests
from datetime import datetime

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

start_long = st.number_input('Start Long ?',value=-73.950655,format='%.6f')
start_lat = st.number_input('Start Lat ?',value=40.783282,format='%.6f')
end_long = st.number_input('End Long ?',value=-73.984365,format='%.6f')
end_lat = st.number_input('End Lat ?',value=40.769802,format='%.6f')
passenger_count = st.number_input('Passenger number ?',value=1,format='%d')

url = 'https://image-name-hsiyuaf4sa-ew.a.run.app/predict'

params={
    'pickup_datetime':pickup_datetime,
    'pickup_longitude':start_long,
    'pickup_latitude':start_lat,
    'dropoff_longitude':end_long,
    'dropoff_latitude':end_lat,
    'passenger_count':passenger_count
}

response=requests.get(url,
                          params).json()

if st.button(label='click me'):
    st.write('fare of the course:',response.get('prediction'))
    

