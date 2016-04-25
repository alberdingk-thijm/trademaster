#TRADEMASTER
Trademaster is a program based on the Tao of D&D's trade system, designed to work without using Excel as an open-source trade system. The aim of Trademaster is to provide a similar interface while making it lightweight, fast and extensible by operating on very simple files (.csv) and using fast algorithms.

##COMPONENTS
Trademaster is made up of 3 components:
- a Reader called Cartographer
- a Computer called Accountant
- a Viewer called Merchant

##FILE FORMATS
Trademaster operates primarily on CSV files as there is no need to encrypt or organize the files in a particularly complex manner.

###READER INPUTS
The reader takes a set of CSV files representing a list of locations in the world.
Each location is represented by a hex with a given location index, a particular climate, elevation, a list of settlements in that location and a set of resources associated with it.

###COMPUTER INPUTS
The computer can be swapped in based on the type of algorithm desired, but all should use the same inputs: a graph adjacency list, i.e. a stored dictionary of locations and their distances from their neighbours. Here is an example:
{'Bramblebridge': [('Rushthorpe', 3), ('Heimdali', 4)], 'Rushthorpe': [('Bramblebridge', 3), ('Angby', 5)], 'Angby': [('Rushthorpe', 5)], 'Heimdali': [('Bramblebridge', 4)]}

###VIEWER INPUTS
The viewer takes finalized distance calculations, a set of economic parameters (which control how prices change based on distance) and a dictionary of places and their associated resources.

##CARTOGRAPHER
Cartographer is the submodule which processes the basic information about what the world looks like. This primarily includes the location of settlements in the world and the resources
they produce. Cartographer can process a CSV file and then output intermediate files which are passed on to the accountant and the merchant.

Cartographer takes a units.csv, some number of location CSVs, and a roads CSV for each of those locations.

##ACCOUNTANT

##MERCHANT
Once we have the distances information, we can calculate the actual resources available to each settlement.
With this information and a resource CSV (e.g. grains.csv), we can determine the prices of goods in that settlement.
