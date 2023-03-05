import pandas as pd
import matplotlib.pyplot as plt

def barplot():    
    def_TBcases = pd.read_excel("TB.xlsx")
    plt.figure(figsize=(20, 10))
    plt.bar(def_TBcases["Country"], def_TBcases["2010 Cases"])
    plt.bar(def_TBcases["Country"], def_TBcases["2011 Cases"])
    plt.bar(def_TBcases["Country"], def_TBcases["2012 Cases"])
    plt.bar(def_TBcases["Country"], def_TBcases["2013 Cases"])
    plt.bar(def_TBcases["Country"], def_TBcases["2014 Cases"])
    plt.legend()
    plt.xlabel("Country")
    plt.ylabel("TB cases Range")
    plt.title("TB cases in the period of 2010 to 2014")
    plt.savefig("bar.png", dpi=500)
    plt.show()

barplot()