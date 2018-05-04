#!/usr/bin/python3

import csv

center_data = dict()
i = 0

with open('fulfillment_centers.csv', newline='') as center_file:
    data = csv.DictReader(center_file)
    for row in data:
        center_data[i] = row
        i += 1

population_data = dict()
i = 0

with open('county_population.csv', newline='') as population_file:
    data = csv.DictReader(population_file)
    for row in data:
        population_data[i] = row
        i += 1    
        

commuting_data = dict()
i = 0

with open('commuting_flows.csv', newline='') as commuting_file:
    data = csv.DictReader(commuting_file)  
    for row in data:
        commuting_data[i] = row
        i += 1

initial_counties = dict()

for center in center_data:
    for commuting in commuting_data:
        if center['County'] == commuting['work_county'] or center['County'] == commuting['residence_county']:
            print(center['County'])
