"""
Section: 2.1.1.3

Estimated time: 15-25 minutes

Level of difficulty: Easy

Objectives
Learn how to:

    read and parse simple XML files using the xml.etree.ElementTree module;
    deal with XML nodes and properties.

Scenario
Download and open the following XML file in your favorite text editor:

nyse.xml

It's a small excerpt of the New York Stock Exchange quotes list. Take a look at it and analyze its structure. You need to do this as your task is to write a code which reads the data and presents it in a form similar to this one:

Command prompt -- Stock Exchange

Hints:

    don't forget to handle at least two possible exceptions: FileNotFoundError and xml.etree.ElementTree.ParseError;
    feel free to improve and beautify the output — we know perfectly well that ours is not very sophisticated and rather ugly.
    object. 

"""

import xml.etree.ElementTree


key_names = ["Company", "Last Price", "Change", "Minimum", "Maximum"]
key_widths = [40, 12, 12, 12, 12]


# Main routine
try:
    data = xml.etree.ElementTree.parse('nyse.xml').getroot()
except FileNotFoundError as fnfe:
    print("The file is not found.", fnfe)
    exit(1)
except  xml.etree.ElementTree.ParseError as pe:
    print("XML parsing error.", pe)
    exit(2)

print(data.tag)
print("\n")

for (n, w) in zip(key_names, key_widths):
    print(n.ljust(w), end='| ')
print()

for quote in data.findall('quote'):
    print(str(quote.text).ljust(40), end='| ')
    print(str(quote.get("last")).ljust(12), end='| ')
    print(str(quote.get("change")).ljust(12), end='| ')
    print(str(quote.get("max")).ljust(12), end='| ')
    print(str(quote.get("min")).ljust(12), end='| ')
    print()
