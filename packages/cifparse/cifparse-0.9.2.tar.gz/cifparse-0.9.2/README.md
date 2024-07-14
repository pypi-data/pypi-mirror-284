# cifparse

A python parser for the FAA CIFP.

# Installation

Install using `pip`:

```
pip install cifparse
```

# Usage

Usage is relatively straightforward. Setting the path to the file can be somewhat finnicky, as it will only accept relative paths. To keep things simple, place the CIFP file in your project directory. Otherwise, if you want to go up several folders into a download folder, it might end up looking like `../../../../Downloads/FAACIFP18`.

Given the amount of data, parsing can take a moment. If dumping the data to a file, that can also add time. Dumping every airport to JSON can take around 15 seconds, and the resulting file is about 330MB.

## Examples

Start by importing `cifparse`, setting the path to the CIFP file, and then parsing the data.

```python
import cifparse

# Initialize the parser:
from cifparse import CIFP

# Set the path to where you have the CIFP file:
c = CIFP("FAACIFP18")

# Parse the data in the file:
c.parse()
# ...or to save time, parse only a specific subset:
c.parse_airports()
c.parse_heliports()
c.parse_ndbs()
c.parse_airways()
c.parse_vhf_dmes()
c.parse_waypoints()
c.parse_controlled()
c.parse_restrictive()
```

### Working with Entire Segments

After parsing the data, the results will be in the CIFP object, accessible via getters that return lists of the objects.

```python
all_airports = c.get_airports()
all_heliports = c.get_heliports()
all_airways = c.get_airways()
all_ndbs = c.get_NDBs()
all_vordmes = c.get_VHF_DMEs()
all_waypoints = c.get_waypoints()
all_controlled = c.get_controlled()
all_restrictive = c.get_restrictive()
```

### Working with Specific Items

```python
airport = c.find_airport("KIAD")
heliport = c.find_heliport("DC03")
airway = c.find_airway("J146")
ndb = c.find_NDB("GTN")
vor = c.find_VHF_DME("AML")
fix = c.find_waypoint("RAVNN")
dc_class_b = c.find_controlled("KDCA")
roa_class_c = c.find_controlled("KROA")
cho_class_d = c.find_controlled("KCHO")
moa = c.find_restrictive("DEMO 1 MOA")

# Because the Alert, MOA, Restricted, and Warning airspace can occasionally be named oddly,
# there is an additional helper function that finds all matches of a particular substring:
all_5314 = c.find_restrictive_match("5314")
# Returns: [R-5314A, R-5314B, R-5314C, R-5314D, R-5314E, R-5314F, R-5314H, R-5314J]
```

### Exporting Data

Each object has its own `to_dict()` method. This is useful when you need to dump the data to json:

```python
airport = c.find_airport("KIAD")
with open("output.json", "w") as json_file:
    json.dump(airport.to_dict(), json_file, indent=2)
```

## Example File

An example file is provided in the [Examples](./examples/) directory. It demonstrates parsing all of the CIFP data, finding an airport within the data, and then looping through the SID and STAR data to create a geoJSON file for each.

## CIFP Objects

A breakdown of the different objects can be found in the [Docs](./docs/) directory.
