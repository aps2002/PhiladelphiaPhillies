# Apaar's Qualifying Offer Calculator 	:baseball:

## Question Prompt:
In baseball, a team can provide a departing free agent player with a qualifying offer1: a one-year contract whose monetary value is the average of the 125 highest salaries from the past season. The player is free to reject it and sign with any other team, but his new team will have to forfeit a draft pick.

## Usage
There are two ways to view this project: running locally or running through my website. They work slightly differently.

### Running through my website
1. Go to the [website I built](http://apsb123.pythonanywhere.com/)
2. See the qualifying offer
3. You can click the "Click here to run again" button to re-run and refresh the page automatically

### Running locally:
1. Clone the repo
2. Install python packages
3. Run the main.py
4. The index.html file will generate an HTML page
5. Open the index.html
6. Every time you would like to re-run, run the main.py file again

## Features
- Filters corrupted or malformed values
- Finds and displayes top 125 players
- Calculates the average salary of the top 125 players
- Generates a histogram to show the distribution of salaries, **note histogram only works on computer**
- When running online, re-running the software is as easy as a click of the button 
- Tested through unit tests

## Trust The Code
This code has been tested for accuracy of the average salary it generates. I converted 3 runs of the data-website into a CSV and manually calculated what the average salary should be. I then compared what my code outputs with the hand calculated average. It passes 3/3 test cases, which may be found under the /tests folder
