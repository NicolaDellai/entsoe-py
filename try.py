from entsoe import EntsoePandasClient
import pandas as pd
import pprint as pp
import seaborn as sns
import matplotlib as plt


client = EntsoePandasClient(api_key="e6156b60-8aa9-434e-8656-9c8a444d92f8")
start = pd.Timestamp('2022-01-01', tz='Europe/Brussels') #yyyy-mm-dd
end = pd.Timestamp('2022-12-31', tz='Europe/Brussels')


#Data for DK1 2022
country_code = "DK_1"
#Day Ahead Prices
DA_1 = client.query_day_ahead_prices(country_code, start=start,end=end)
C_1=client.query_installed_generation_capacity(country_code, start=start,end=end, psr_type=None)
#C_1_per_unit = client.query_installed_generation_capacity_per_unit(country_code, start=start,end=end, psr_type=None) #as C_1 but location specific
C_Wind_Off_1 = C_1['Wind Offshore']
C_Wind_On_1 = C_1['Wind Onshore']
C_Solar_1 = C_1['Solar']
G_1 = client.query_generation(country_code, start=start,end=end, psr_type=None) #What's "other renewable" column referring to?
G_Wind_Off_1 = G_1['Wind Offshore']
G_Wind_On_1 = G_1['Wind Onshore']
G_Solar_1 = G_1['Solar']


#Data for DK2 2022
country_code = "DK_2" 
#Day Ahead Prices
DA_2 = client.query_day_ahead_prices(country_code, start=start,end=end)
C_2=client.query_installed_generation_capacity(country_code, start=start,end=end, psr_type=None)
#C_2_per_unit = client.query_installed_generation_capacity_per_unit(country_code, start=start,end=end, psr_type=None) #as C_1 but location specific
C_Wind_Off_2 = C_2['Wind Offshore']
C_Wind_On_2 = C_2['Wind Onshore']
C_Solar_2 = C_2['Solar']
G_2 = client.query_generation(country_code, start=start,end=end, psr_type=None) #What's "other renewable" column referring to?
G_Wind_Off_2 = G_2['Wind Offshore']
G_Wind_On_2 = G_2['Wind Onshore']
G_Solar_2 = G_2['Solar']
pp.pprint(G_2)
G_2 =G_2.T 
pp.pprint(G_2)
#G_2_wide = G2.pivot(index="year", columns="hour", values=G_2[G_2.rows[0]])

plt.pyplot(G_2.iloc[:,0],G_Solar_2[2,:])
#sns.kdeplot(data=G_2, x=df[G_2.columns[0]], hue="", multiple="stack")
