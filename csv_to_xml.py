"""
CSV to XML
Quick and dirty CSV to XML converter to create settlements.xsd-schema correct
files containing neighbour and resource information for a region, using a
CSV of resources and a CSV of roads.

resource CSV format:
placename,resource1,resource2,...

road CSV format:
placename,place1,place2,...
place1,0,weight1-2,...
place2,weight1-2,0,...
x's denote non-neighbours
"""

import csv

def csv_to_xml(resos, roads):
    """
    """
    
    with open(resos[:-3] + 'xml', 'w+') as xml:
        pass

