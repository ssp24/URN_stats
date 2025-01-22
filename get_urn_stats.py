import requests 
import pandas as pd
import datetime

def get_all():
    
    	r1 = requests.get("https://api.nbn-resolving.org/v2/urns")
    	data = r1.json()
    	df = pd.json_normalize(data)
    	total_urns = df['totalItems'][0]
    	total_urns = str(total_urns)
        
    	return(total_urns)

def get_all_namespaces(): 

	r2 = requests.get("https://api.nbn-resolving.org/v2/namespaces")
	namespaces_data = r2.json()
	df2 = pd.json_normalize(namespaces_data)
	total_namespaces = df2['totalItems'][0]
	total_namespaces = str(total_namespaces)

	return(total_namespaces)


current_time = datetime.datetime.now()
current_time = current_time.strftime('%Y-%m-%d %H:%M')

urns = get_all()
namespaces = get_all_namespaces()

text = current_time + ", " + urns + ", " + namespaces + "\n"

with open("data/stats.txt", 'a') as outfile:
    outfile.write(text)
	
