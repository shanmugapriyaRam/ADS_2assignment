
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import stats as st

#Source Data
sd_df = pd.read_excel("C:/Users/shanm/OneDrive/Desktop/assignment 2/API_19_DS2_en_excel_v2_5360124.xls", header=3)

#sd=sd.drop(['Country Code', 'Indicator Code'], axis=1)


def transformDataFrame(df):
    df.set_index(['Country Name', 'Indicator Name'], inplace=True)
    df=df.T
    df=df.fillna(0) 
    return df
new_sd=transformDataFrame(sd_df)

India = new_sd.loc[:, 'India']
Pakistan = new_sd.loc[:, 'Pakistan']
Sri_Lanka = new_sd.loc[:, 'Sri Lanka']
Bangladesh = new_sd.loc[:, 'Bangladesh']
Burma = new_sd.loc[:, 'Burma']
China = new_sd.loc[:, 'China']
Japan = new_sd.loc[:, 'Japan']
Singapore = new_sd.loc[:, 'Singapore']
Thailand = new_sd.loc[:, 'Thailand']

India = India.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
Pakistan = Pakistan.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
Sri_Lanka = Sri_Lanka.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
Bangladesh = Bangladesh.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)', 'Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
Burma = Burma.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
China = China.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
Japan = Japan.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
Singapore = Singapore.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
Thailand = Thailand.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]

plt.plot(India.index, India.loc[:, 'Arable land (% of land area)'], label='India')
plt.plot(Pakistan.index, Pakistan.loc[:, 'Arable land (% of land area)'], label='Pakistan')
plt.plot(Sri_Lanka.index, Sri_Lanka.loc[:, 'Arable land (% of land area)'], label='Sri_Lanka')
plt.plot(Bangladesh.index, Bangladesh.loc[:, 'Arable land (% of land area)'], label='Bangladesh')
plt.plot(Burma.index, Burma.loc[:, 'Arable land (% of land area)'], label='Burma')
plt.plot(China.index, China.loc[:, 'Arable land (% of land area)'], label='China')
plt.plot(Japan.index, Japan.loc[:, 'Arable land (% of land area)'], label='Japan')
plt.plot(Singapore.index, Singapore.loc[:, 'Arable land (% of land area)'], label='Singapore')
plt.plot(Thailand.index, Thailand.loc[:, 'Arable land (% of land area)'], label='Thailand')
plt.xlabel('Years')
plt.ylabel('Land Percentage')
plt.title('Arable Land')
plt.ylim(0, 70, 10)
plt.legend(bbox_to_anchor=(1.0, 1.05))
plt.show()


plt.plot(India.index, India.loc[:, 'Forest area (% of land area)'], label='India')
plt.plot(Pakistan.index, Pakistan.loc[:, 'Forest area (% of land area)'], label='Pakistan')
plt.plot(Sri_Lanka.index, Sri_Lanka.loc[:, 'Forest area (% of land area)'], label='Sir Lanka')
plt.plot(Bangladesh.index, Bangladesh.loc[:, 'Forest area (% of land area)'], label='Bangladesh')
plt.plot(Burma.index, Burma.loc[:, 'Forest area (% of land area)'], label='Burma')
plt.plot(China.index, China.loc[:, 'Forest area (% of land area)'], label='China')
plt.plot(Japan.index, Japan.loc[:, 'Forest area (% of land area)'], label='Japan')
plt.plot(Singapore.index, Singapore.loc[:, 'Forest area (% of land area)'], label='Singapore')
plt.plot(Thailand.index, Thailand.loc[:, 'Forest area (% of land area)'], label='Thailand')
plt.xlabel('Years')
plt.ylabel('Land Percentage')
plt.title('Forest Land')
plt.xlim(1, 6, 1)
plt.ylim(0, 65, 10)
plt.legend(bbox_to_anchor=(1.0, 1.05))
plt.show()

sns.heatmap(India.corr(), cmap='Reds', center=0, annot=True, linewidths=0.05)
plt.title("India")
plt.show()

sns.heatmap(China.corr(), cmap=sns.cubehelix_palette(as_cmap=True), center=0, annot=True, linewidths=0.05)
plt.title("China")
plt.show()

sns.heatmap(Japan.corr(), cmap='crest', center=0, annot=True, linewidths=0.05)
plt.title("Japan")
plt.show()

