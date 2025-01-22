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


current_time = datetime.datetime.now()
current_time = current_time.strftime('%Y-%m-%d %H:%M')

urns = get_all()

text = current_time + ", " + urn_all + "\n"

with open("data/stats.txt", 'a') as outfile:
    outfile.write(text)
	
