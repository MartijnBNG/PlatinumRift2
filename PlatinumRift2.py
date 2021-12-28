import sys
import math

zoneList = []
moveList = ""

class Zone:
    platinumValue = 0.5
    myPodValue = -0.9
    enemyPodValue = 0.1
    mySpaceValue = -0.9
    enemySpaceValue = 0.1
    neutralSpaceValue = 0.1
    
    def __init__(self, zone_id, platinum_source):
        self.linkList = []
        self.zone_id = zone_id
        self.platinum = platinum_source
        self.owner_id = 0
        self.myPods = 0
        self.enemyPods = 0
        self.visible = 0
        self.baseValue = 0.0
        #print("Zone created: {}".format(self.zone_id), file=sys.stderr)
    
    def addLink(self, linkedZone):
        self.linkList.insert(0, linkedZone)
        #print("Link created: {} to {}".format(self.zone_id, linkedZone), file=sys.stderr)

    def setTurnInfo(self, owner_id, pods_p0, pods_p1, visible, platinum):
        self.owner_id = owner_id
        if (my_id == 0):
            self.myPods = pods_p0
            self.enemyPods = pods_p1
        else:
            self.myPods = pods_p1
            self.enemyPods = pods_p0
        self.visible = visible
        self.platinum = platinum
        #if (self.visible == 1):
            #print("self.zone_id: {}, owner_id: {}, myPods: {}, enemyPods: {}, visible: {}, platinum: {}".format(self.zone_id, self.owner_id, self.myPods, self.enemyPods, self.visible, self.platinum), file=sys.stderr)

    def setBaseValue(self):
        self.baseValue = 0.0
        self.baseValue += self.platinum * Zone.platinumValue
        self.baseValue += self.myPods * Zone.myPodValue
        self.baseValue += self.enemyPods * Zone.enemyPodValue
        
    def movePods(self):
        #print("zone: {}, movePods: {}".format(self.zone_id, self.myPods), file=sys.stderr)
        for i in range(self.myPods):
            self.linkList.sort(key=lambda x: zoneList[x].baseValue, reverse=True)
            #print("movePod {} from zone {} to zone {}".format(i, self.zone_id, self.linkList[i % len(self.linkList)]), file=sys.stderr)
            print("1 {} {} ".format(self.zone_id, self.linkList[0]), end='')
            zoneList[self.linkList[0]].baseValue -= 10
#i % len(self.linkList)]
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in input().split()]
    x = Zone(zone_id, platinum_source)
    zoneList.append(x)

for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]
    zoneList[zone_1].addLink(zone_2)
    zoneList[zone_2].addLink(zone_1)

# game loop
while True:
    my_platinum = int(input())  # your available Platinum
    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]
        zoneList[z_id].setTurnInfo(owner_id, pods_p0, pods_p1, visible, platinum)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    for i in range(zone_count):
        zoneList[i].movePods()

    # first line for movement commands, second line no longer used (see the protocol in the statement for details)
    print("")
    print("WAIT")

