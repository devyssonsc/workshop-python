import requests, streamlit, pandas, ipaddress
# current_ip = requests.get("https://ipinfo.io/ip")

# info_ip = requests.get(f"https://ipinfo.io/{current_ip.text}/json")

# latitude = info_ip.json()['loc'].split(',')[0]

# longitude = info_ip.json()['loc'].split(',')[1]

# meteo = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")

# ip = info_ip.json()['ip']

# streamlit.set_page_config(page_title="Workshop Python")
# streamlit.write("IP = " + ip)

# streamlit.write("## Meteorologia Info")
# data = pandas.DataFrame({
#     'latitude': [float(latitude)],
#     'longitude' : [float(longitude)]
# })

# streamlit.map(data,use_container_width=True)

with streamlit.form(key="qualquer_coisa"):
    user_input = streamlit.text_input("O seu nome: ")
    submit_button = streamlit.form_submit_button(label= "Enviar")
    if submit_button == True:
        streamlit.write("O seu input foi: " + user_input)
        try:
            ipaddress.ip_address(user_input)
            info_ip = requests.get(f"https://ipinfo.io/{user_input}/json")

            latitude = info_ip.json()['loc'].split(',')[0]

            longitude = info_ip.json()['loc'].split(',')[1]

            meteo = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")

            data = pandas.DataFrame({
                'latitude': [float(latitude)],
                'longitude' : [float(longitude)]
            })

            
            streamlit.map(data,use_container_width=True)
        except:
            streamlit.write("ip = " + user_input+ 'invalido')
     
    else:
        streamlit.write("Aperte o botão para submeter o seu texto")


        