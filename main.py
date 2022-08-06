from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import pandas as pd

class Average:
    def __init__(self, url, outputFile, numTops):
        self.url  =url
        self.outputFile = outputFile
        self.numTops = numTops

    def getData(self):
        html = urlopen(self.url).read()
        soup = BeautifulSoup(html, features="html.parser")
        table = soup.select_one("table")
        # python3 just use th.text
        headers = ["Player", "Salary", "Year", "Level"]
        print (headers)
        with open(self.outputFile, "w") as f:
            wr = csv.writer(f)
            wr.writerow(headers)
            wr.writerows([[td.text.encode("utf-8").decode("utf-8")  for td in row.find_all("td")] for row in table.select("tr")])

    def convertToDf(self, csvFile):
        self.outputFile = csvFile
        df = pd.read_csv(self.outputFile)
        toRemove = df[~df.Salary.str.contains("$", na=False)]
        toRemoveTwo = df.loc[(df['Salary'] == 'no salary data') ]
        new = pd.concat([df, toRemove,toRemoveTwo]).drop_duplicates(keep=False)
        new['Salary'] = new['Salary'].str.replace(',', '')
        new['Salary'] = new['Salary'].str.replace('$', '')
        new['Salary'] = new['Salary'].astype(str).astype(float)
        sorted_df = new.sort_values(by=['Salary'], ascending=False)
        self.sorted_df = sorted_df

    def topXContracts(self):
        topXPlayers = self.sorted_df.head(self.numTops)
        self.topXPlayers = topXPlayers

    def getAverage(self):
        self.avg =  round(self.topXPlayers["Salary"].mean(),2)
        return self.avg


avgOne = Average('https://questionnaire-148920.appspot.com/swe/data.html', "output.csv", 125)
avgOne.getData()
avgOne.convertToDf("output.csv")
avgOne.topXContracts()
print(avgOne.getAverage())