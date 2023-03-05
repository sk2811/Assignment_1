import pandas as pd
import matplotlib.pyplot as plt
"""
this function  determine the this Pie chart graph I can able to identify most preferable supermarket by the highest number of people.
"""

def piechart():
    def_shop = pd.read_excel("shopping.xlsx")
    print(def_shop)
    plt.figure()
    plt.pie(def_shop["Percentage"], labels = def_shop["Shopping Super Market"])
    plt.title("supermarket")
    plt.savefig("pie.png")
    plt.show()

piechart()