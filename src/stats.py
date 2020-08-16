import requests
import pandas as pd
from src import util

class Stats:

    def __init__(self):
        self.last_cases = self.get_cases()

    def new_cases(self):
        cases = self.get_cases()
        # new update!
        if cases != self.last_cases:
            new_indexes = None
            for i in range(len(self.last_cases)):
                if util.hex(cases[i]) == util.hex(self.last_cases[i]):
                    new_indexes = i
                    break
            return cases[:new_indexes]
        return []
            
    def get_cases(self):
        # get NZ Health Data
        url = "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases/covid-19-current-cases-details"
        r = requests.get(url)
        
        # get data from HTML Table
        table = pd.read_html(r.text)[0]
        table = table.where(pd.notnull(table), None) # replace Nan with None

        # format return data
        cases = []
        for case in table.values.tolist():
            cases.append(util.case_to_json(case))
        return cases
