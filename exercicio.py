import requests, streamlit, pandas

info_ip = requests.get("https://ipinfo.io/1.1.1.1/json")

#print(info_ip.text)

# print(info_ip.json()['loc'])

# print(info_ip.json()['loc'].split(','))

latitude = info_ip.json()['loc'].split(',')[0]

longitude = info_ip.json()['loc'].split(',')[1]

meteo = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")

# print(meteo.json())

ip = info_ip.json()['ip']

streamlit.set_page_config(page_title="Workshop Python")
streamlit.write("IP = " + ip)

streamlit.write("## Meteorologia Info")
data = pandas.DataFrame({
    'latitude': [float(latitude)],
    'longitude' : [float(longitude)]
})

streamlit.map(data,use_container_width=True)

user_input = streamlit.text_input("O seu nome: ")
streamlit.write(user_input)