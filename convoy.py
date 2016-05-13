"""
TRADEMASTER - CONVOY

Convoy handles the movement of resources from their place of origin
to other markets.
"""

import os
from lxml import etree
from dijkstra import dijkstra

def init_paths(settlements, roads, tariff):
    """
    Return an "adjacency list" dictionary that specifies the neighbours
    of each settlement and their distance by road, as given by the settlements
    CSV and the roads CSV which corresponds to it.
    """
    paths = {}
    return paths

def init_paths(settlements, tariff=1):
    """
    Return a tuple of two dictionaries: an "adjacency list" dictionary that specifies 
    the neighbours of each settlement and their distance by road; and a dictionary that
    specifies the resources available at each settlement, as given by the settlements
    XML file.
    If a tariff is given, increment each distance by road with the tariff. The tariff must be non-negative.
    """

    paths = {}
    resos = {}
    with open(settlements, 'r') as xml:
        tree = etree.parse(xml)
        places = tree.xpath("./settlement")
        for place in places:
            placename = place.findtext("./placename")
            paths[placename] = []
            resos[placename] = []
            neighbours = place.findall("./neighbours/neighbour")
            for nbr in neighbours:
                [name, dist] = nbr.findtext("name"), int(nbr.findtext("distance")) + tariff
                paths[placename].append((name, dist))
            resources = place.findall("./resources/resource")
            for resource in resources:
                [name, quant] = resource.get('name'), int(resource.text)
                resos[placename].append((name, quant))
    
    return paths, resos


def run_alg(paths, source, algname='dijkstra'):
    """
    Return a tuple of dictionaries of ({v: sum weight from s to v},{v: path from s to v}),
    determined from the v in paths with s as source using the given string algname (e.g. dijkstra).
    """

    algs = {'dijkstra': dijkstra}
    return algs[algname](paths, source)


def recalc_refs(resos, distances, s):
    """
    Return a new dictionary of resources in s using the old dictionary resos, modifying the availability
    of resources based on the distances dictionary given relative to the source s.
    """
    
    s_refs = {}
    for place,refs in resos.items():
        for (name,quant) in refs:
            dist = (distances[place] if place != s else 1)
            s_refs[name] = s_refs.get(name, 0) + float(quant) / dist # add quantity divided by distance
    return s_refs

def commit_paths(paths, refs, outxml):
    """
    Write the modified paths and refs information into a new XML
    file called outxml, with the same schema as the settlements XML
    but with a complete list of all market distances.
    """

    # create the settlements level
    root = etree.Element("settlements", nsmap={'xsi': 'http://www.w3.org/2001/XMLSchema-instance'})
    root.set('{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation','settlements.xsd')
    # for each place in the path
    for placename,info in paths.items():
        # create a <settlement>
        settlement = etree.Element("settlement")
        # add the neighbours with path info to the <neighbours> element
        nbrs = etree.SubElement(settlement, "neighbours")
        for (nbr, dist) in info:
            nbrnode = etree.Element("neighbour")
            nbrnode.set("name", nbr)
            nbrnode.text = dist
            nbrs.append(nbrnode) 
        # add the references to the <resources> element
        resosnode = etree.SubElement(settlement, "resources")
        for ref,quant in refs.items():
            resonode = etree.Element("resource")
            resonode.set("name", ref)
            resonode.text = quant
            resosnode.append(resonode)
        root.append(settlement)
    # write out
    with open(outxml, 'r') as output:
        output.write(settlements)
    