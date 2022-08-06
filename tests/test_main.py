import json
from unittest import TestCase
import main

class TestAverage(TestCase):

    '''
    Test Plan:

    1. Stored data from data source 3 times and save in separate files
    2. Create an object for each test (here named checkOutput)
        - Feed in dummy values for the initializing parameters
    3. Change the csv to one of the csv files generated in step 1
    4. Manually calculate what the expected salary should be
    5. Compare the two values
    '''

    def test_get_average_on_out(self):
        self.checkOutput = main.Average("https://questionnaire-148920.appspot.com/swe/data.html", "outtester.csv", 125)
        self.checkOutput.getData()
        self.checkOutput.convertToDf("out.csv")
        self.checkOutput.topXContracts()
        actual = self.checkOutput.getAverage()
        expected = 16582060.81
        self.assertEqual(expected, actual)

    def test_get_average_on_outputTestOne(self):
        self.checkOutput = main.Average("https://questionnaire-148920.appspot.com/swe/data.html", "outtester.csv", 125)
        self.checkOutput.getData()
        self.checkOutput.convertToDf("outputTestOne.csv")
        self.checkOutput.topXContracts()
        actual = self.checkOutput.getAverage()
        expected = 16299727.48
        self.assertEqual(expected, actual)

    def test_get_average_on_outputTestTwo(self):
        self.checkOutput = main.Average("https://questionnaire-148920.appspot.com/swe/data.html", "outtester.csv", 125)
        self.checkOutput.getData()
        self.checkOutput.convertToDf("outputTestTwo.csv")
        self.checkOutput.topXContracts()
        actual = self.checkOutput.getAverage()
        expected = 16306327.48
        self.assertEqual(expected, actual)
