#importing pandas to show the model
import pandas as pd
from matplotlib import pyplot as plt
#data from the csv
global_data = pd.read_csv("global_covid19_data.csv")

data = global_data[global_data['date'] == '2020-06-30']
print(data)
data.dropna(subset = ["continent"], inplace=True)
continents = data.continent
values = data.total_cases
#shows the model of how many people got covid 19
plt.bar(continents, values)
plt.xlabel("continents")
plt.xticks(rotation=10)
#labels the x-axis
plt.ylabel("Total Cases of covid 19")
plt.title("Covid 19 numbers on 6/30/2020")
#calls the graph and shows it 
plt.show()

print("this virgen two")
