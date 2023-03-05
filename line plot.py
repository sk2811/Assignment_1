import pandas as pd
import matplotlib.pyplot as plt
"""
this function plots determine the the unemployment rate in each year of given countries
"""
def lineplot():
  """
 this function read data from 'Unemployment Rate.xlsx'
 
 """
def_unemp = pd.read_excel("Unemployment Rate.xlsx")
print(def_unemp)

plt.figure()
plt.plot(def_unemp["Year"], def_unemp["germany"], label = "germany")
plt.plot(def_unemp["Year"], def_unemp["south africa"], label = "south africa")
plt.plot(def_unemp["Year"], def_unemp["brazil"], label = "brazil")
plt.plot(def_unemp["Year"], def_unemp["Iran"], label = "Iran")
plt.legend()
plt.xlim(2018,2023)
plt.ylim(0,24)
plt.xlabel("Year")
plt.ylabel("Unemployment Rate")
plt.title("Unemployment rate in countries based on year")
plt.savefig("line.png")
plt.show()

    
    
lineplot()