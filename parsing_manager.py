import xml.etree.ElementTree as ET
import os.path
import sys
import random


from classes.Station import Station
from classes.Node import Node
from classes.Link import Link
from classes.Network import Network
from classes.Port import Port
from classes.Flow import Flow
from classes.Target import Target
from classes.Switch import Switch



################################################################@
""" Local methods """
################################################################@




""" parseStations
    Method to parse stations
        root : the xml main root
"""
def parseStations(root,network):
    for station in root.findall('station'):
        
        network.stations.append (   Station(name=station.get('name'),capacity=float(station.get('transmission-capacity')),network=network) )













""" parseSwitches
    Method to parse switches
        root : the xml main root
"""
def parseSwitches(root,network):
    for sw in root.findall('switch'):
        network.switches.append (   Switch( name=sw.get('name'),
                                            latency=float(sw.get('tech-latency')),
                                            capacity=float(sw.get('transmission-capacity')),
                                            network=network),
                                            )













""" parseEdges
    Method to parse edges
        root : the xml main root
"""
def parseEdges(root,network):
    for sw in root.findall('link'):
        
        frm = [s for s in (network.stations + network.switches) if s.name()==sw.get('from')][0]
        to =  [s for s in (network.stations + network.switches) if s.name()==sw.get('to')][0]
        
        from_port=Port(device=frm,number=int(sw.get('fromPort')))
        
        to_port=Port(device=to,number=int(sw.get('toPort')))
        
        lk = Link(name=sw.get('name'),
                                     frm=frm,
                                     to=to,
                                     from_port=from_port,
                                     to_port=to_port,
                                     capacity=float(sw.get('transmission-capacity')),
                                     network=network)
        
        from_port.link(lk)
        to_port.link(lk)
        
        if frm.is_switch():
            frm.ports.append(from_port)
            frm.links.append(lk)
        else:
            frm.port(from_port)
            frm.link(lk)
            
            
        if to.is_switch():
            to.ports.append( to_port )
            to.links.append(lk)
        else:
            to.port(to_port)
            to.link = lk
        
        network.links.append ( lk )












""" parseFlows
    Method to parse flows
        root : the xml main root
"""
def parseFlows(root,network):
    for sw in root.findall('flow'):
        
        source = [s for s in (network.stations) if s.name()==sw.get('source')][0]
        
        flow = Flow (name=sw.get('name'),
                     source=source,
                     payload=float(sw.get('max-payload')),
                     overhead=67,
                     period=float(sw.get('period')),
                     network=network)
        
        for tg in sw.findall('target'):
            target_object = [s for s in (network.stations) if s.name()==tg.get('name')][0]
            target = Target( name=tg.get('name'),
                             target=target_object,
                             flow=flow)
            
            flow.targets.append(target)
            target.path.append(flow.source)
            for pt in tg.findall('path'):
                path_node=[s for s in (network.stations + network.switches) if s.name()==pt.get('node')][0]
                target.path.append(path_node)
                if path_node.is_switch() and not(flow in path_node.flows) :
                    path_node.flows.append(flow)
        
        network.flows.append (flow)
        source.flows.append(flow)











""" parseNetwork
    Method to parse the whole network
        xmlFile : the path to the xml file
"""
def parseNetwork(xmlFile,network):
    if os.path.isfile(xmlFile):
        tree = ET.parse(xmlFile)
        root = tree.getroot()
        
        for sw in root.findall('network'):
            network.overhead(float(sw.get("overhead")))
            network.name(sw.get("name"))
            network.technology(sw.get("technology"))
            network.capacity(float(sw.get("transmission-capacity")))
            network.shortest_path_policy(sw.get("shortest-path-policy"))
        
        
        parseStations(root,network)
        parseSwitches(root,network)
        parseEdges(root,network)
        parseFlows(root,network)
    else:
        print("File not found: "+xmlFile)











""" traceNetwork
    Method to trace the network to the console
"""
def traceNetwork(network):
    print("Stations:")
    for node in network.stations:
        print ("\t" + node.name())
            
    print("\nSwitches:")
    for node in network.switches:
        print ("\t" + node.name())
            
    print("\nEdges:")
    for edge in network.links:
        print ("\t" + edge.name() + ": " + edge.frm().name() + "=>" + edge.to().name())
    
    print("\nFlows:")
    for flow in network.flows:
        print ("\t" + flow.name() + ": " + flow.source.name() + " (L=" + str(flow.payload()) +", p=" + str(flow.period()) + ")")
        for target in flow.targets:
            print ("\t\tTarget=" + target.target().name())
            for node in target.path:
                print ("\t\t\t" + node.name())











""" createFakeResultsFile
    Method to create a fake result file ; only delays are generated (random value between 40 and 80)
        xmlFile : the path to the xml (input) file
"""
def createFakeResultsFile (xmlFile,network):
    posDot = xmlFile.rfind('.')
    if not (posDot == -1):
        resFile = xmlFile[0:posDot]+'_res.xml'
    else:
        resFile = xmlFile+'_res.xml'
    res = open(resFile,"w")
    res.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    res.write('<results>\n')
    res.write('\t<delays>\n')
    for flow in network.flows:
        res.write('\t\t<flow name="' + flow.name() + '">\n');
        for target in flow.targets:
            res.write('\t\t\t<target name="' + target.name() + '" value="'+str(random.randint(400, 800))+'" />\n');
        res.write('\t\t</flow>\n')
    res.write('\t</delays>\n')
    res.write('</results>\n')
    res.close()
    file2output(resFile)
    
    
    
    
    
    
    
    
    
    
    
    
def createResultsFile (xmlFile,network):
    posDot = xmlFile.rfind('.')
    if not (posDot == -1):
        resFile = xmlFile[0:posDot]+'_res.xml'
    else:
        resFile = xmlFile+'_res.xml'
    res = open(resFile,"w")
    res.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    res.write('<results>\n')
    

    
    # delays
    res.write('\t<delays>\n')
    for flow in network.flows:
        res.write('\t\t<flow name="' + flow.name() + '">\n');
        for target in flow.targets:
            res.write('\t\t\t<target name="' + target.name() + '" value="'+str(  format(target.eed()*1000000, '.0f'  )   )+'" />\n');
        res.write('\t\t</flow>\n')
    res.write('\t</delays>\n')
    
    
    #link loads
    res.write('\t<load>\n')
    for link in network.links:
        res.write('\t\t<edge name="' + link.name() + '">\n');
        res.write('\t\t\t<usage type="' + 'direct' + '" value="'+str(link.direct_usage()  )+'"' +  ' percent="'+str(  format(link.direct_load()*100, '.2f'  )   )+'%" />\n')
        res.write('\t\t\t<usage type="' + 'reverse' + '" value="'+str(link.reverse_usage() )+'"' + ' percent="'+str( format(link.reverse_load()*100,  '.2f' ) )+'%" />\n')
        res.write('\t\t</edge>\n')    
    res.write('\t</load>\n')  
    
    
    
    
    # backlogs
    res.write('\t<backlogs>\n')
    for sw in network.switches:
        res.write('\t\t<switch name="' + sw.name() + '">\n');
        for port in sw.ports:
            if port.backlog() > 0:
                res.write('\t\t\t<port num="' + str(port.number()) + '" backlog="'+str(format(port.backlog()/8 , '.0f' ))+'"' +  ' delay="'+str( format(port.delay()*1000000, '.1f') )+'" />\n')   
        res.write('\t\t</switch>\n')
    res.write('\t</backlogs>\n')  
    
    
    res.write('</results>\n')
    res.close()
    file2output(resFile)
    
    
    
    
    
    
    
    
    
    
""" file2output
    Method to print a file to standard ouput
        file : the path to the xml (input) file
"""
def file2output (file):
    hFile = open(file, "r")
    for line in hFile:
        print(line.rstrip())