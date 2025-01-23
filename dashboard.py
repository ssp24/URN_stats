import pandas as pd
#import plotly.express as px
import streamlit as st

st.subheader("Infographiken zum URN-Service der DNB")
st.markdown("""Diese App ist ein Prototyp! Sie bietet eine Übersicht über die Anzahl an Publikationen
              in der DNB seit Februar 2023. Hierfür wird 1x täglich um 07:00 Uhr automatisch die SRU-Schnittstelle 
               der DNB abgefragt und die Werte werden aktualisiert.""")

with open('data/stats.txt') as f:
    stats = [line.rstrip('\n') for line in f]
    stats = [line.replace(', ', ',') for line in stats]



df = pd.DataFrame([sub.split(",") for sub in stats])
headers = df.iloc[0].values
df.columns = headers
df.drop(index=0, axis=0, inplace=True)
df['total-urns'] = df['total-urns'].astype('int')
df['total-namespaces'] = df['total-namespaces'].astype('int')

df_counter = df[-2:]

#calculate growth total-urns: 
todays_total_urns = df_counter['total-urns'].values[1]
print_total_urns = f"{todays_total_urns:,}".replace(',', '.')
yesterdays_total_urns = df_counter['total-urns'].values[0]
diff_urns = todays_total_urns-yesterdays_total_urns
diff_urns = f"{diff_urns:,}".replace(',', '.')

#calculate growth total-namespaces
todays_total_namespaces = df_counter['total-namespaces'].values[1]
print_total_namespaces = f"{todays_total_namespaces:,}".replace(',', '.')
yesterdays_total_namespaces = df_counter['total-namespaces'].values[0]
diff_namespaces = todays_total_namespaces-yesterdays_total_namespaces
diff_namespaces = f"{diff_namespaces:,}".replace(',', '.')



col1, col2 = st.columns(2) 
col1.metric(label="Registrierte URNs", value=print_total_urns, delta=f"{diff_urns} seit gestern")
col2.metric(label="Registrierte Unternamensräume", value=print_total_namespaces, delta=f"{diff_namespaces} seit gestern")




