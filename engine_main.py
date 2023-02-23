################################################################@
"""
Author : Yacine BEN BELKACEM
"""
################################################################@


from parsing_manager import *


################################################################@
""" Global data """
################################################################@

afdx_network = Network()

################################################################@
""" Main program """
################################################################@

if len(sys.argv)>=2:
    xmlFile=sys.argv[1]
else:
    xmlFile="./ES2E_M.xml"
    
parseNetwork(xmlFile,afdx_network)

#traceNetwork(afdx_network)

afdx_network.compute_links_usage()
afdx_network.compute_links_load()

afdx_network.compute_curves()
afdx_network.compute_flows_delays()
#print(afdx_network.stations[0].port().arrival_curve().b())
#print(afdx_network.stations[0].port().arrival_curve().r())

#print(afdx_network.stations[2].port().delay())
#print(afdx_network.stations[1].port().delay())
#print(afdx_network.stations[1].capacity())

createResultsFile(xmlFile,afdx_network)


