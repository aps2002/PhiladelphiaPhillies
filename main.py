from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import pandas as pd
import matplotlib.pyplot as plt
class Average:
    def __init__(self, url, outputFile, numTops):
        self.url  =url
        self.outputFile = outputFile
        self.numTops = numTops

    def getData(self):
        html = urlopen(self.url).read()
        soup = BeautifulSoup(html, features="html.parser")
        table = soup.select_one("table")
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
        df.drop(columns=['Player'])
        self.sorted_df = sorted_df

    def topXContracts(self):
        topXPlayers = self.sorted_df.head(self.numTops)
        self.topXPlayers = topXPlayers

    def getAverage(self):
        self.avg =  round(self.topXPlayers["Salary"].mean(),2)
        return self.avg

    def generateBarGraph(self):
        fig, ax = plt.subplots()
        ax.title.set_text("Salary Distribution")
        ax.set_xticks(range(len(self.topXPlayers["Salary"])))

        fig = self.topXPlayers['Salary'].value_counts().plot(ax=ax, kind='hist').figure
        fig.savefig("histogramOutput.png")

    def convertToWebsite(self):
        result = self.topXPlayers.to_html()
        self.generateBarGraph()
        text_file = '''
        <style>
          /* Style the button that is used to open and close the collapsible content */
        .collapsible {
          background-color: #eee;
          color: #444;
          cursor: pointer;
          padding: 18px;
          width: 100%;
          border: none;
          text-align: left;
          outline: none;
          font-size: 15px;
        }

        /* Add a background color to the button if it is clicked on (add the .active class with JS), and when you move the mouse over it (hover) */
        .active, .collapsible:hover {
          background-color: #ccc;
        }

        /* Style the collapsible content. Note: hidden by default */
        .content {
          padding: 0 18px;
          display: none;
          overflow: hidden;
          background-color: #f1f1f1;
        }
        </style>
        <body>
        <h1>Projected Salary</h1>
        <h3>
        '''
        text_file+=str(self.avg)
        text_file+='''
        </h3>

        <button type="button" class="collapsible">Open Collapsible</button>

        <div class="content">
        '''
        text_file+=(result)
        text_file +='''
        </div>

        <button type="button" class="collapsible">See Salary Distribution</button>
        <div class="content">
          <img src="https://www.pythonanywhere.com/user/apsb123/files/home/apsb123/mysite/histogramOutput.png" alt="Histogram of data">
        </div>
        <p><a href="/">Click here to run Again</a>

        <script>
          var coll = document.getElementsByClassName("collapsible");
          var i;

          for (i = 0; i < coll.length; i++) {
            coll[i].addEventListener("click", function() {
              this.classList.toggle("active");
              var content = this.nextElementSibling;
              if (content.style.display === "block") {
                content.style.display = "none";
              } else {
                content.style.display = "block";
              }
            });
          }
        </script>
        </body>
        '''
        return text_file






avgOne = Average('https://questionnaire-148920.appspot.com/swe/data.html', "output.csv", 125)
avgOne.getData()
avgOne.convertToDf("output.csv")
avgOne.topXContracts()
avgOne.getAverage()
#print(avgOne.topXPlayers)
print(avgOne.convertToWebsite())
#avgOne.generateBarGraph()