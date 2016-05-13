# Trademaster
A roleplaying game trade system creator, based on the methodology of
[Alexis Smolensk](http://tao-dnd.blogspot.com).<br>While Alexis'
[trade system](http://tao-of-dnd.wikispaces.com/Trade+%26+Equipment) is managed
using a series of Excel files, Trademaster is designed to provide a similar
interface using Python. As Trademaster's goal is to emulate a large-scale trade
network, it relies on tables to track relevant information such as the location
of goods or the distances between regions.<br>These tables are stored 
primarily as CSV files to keep space requirements as low as possible, but
Trademaster also uses XML files for certain tasks as they provide 
better controls on the format of data.

## Components
Trademaster has several components which perform various tasks.
These include the...
- Cartographer, which maps out the trade networks
- Convoy, which calculates the presence of resources across the network
- ...  

