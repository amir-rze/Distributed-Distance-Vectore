import random
import copy
LINKCHANGES = 1

TRACE = 1
YES = 1
NO = 0
event_list = []   # the event list

clocktime = 0.000

infinite = 999999 # define infinite = 99999

class RoutingPacket:
    def __init__(self, source_id, destination_id, minimum_cost):
        self.source_id = source_id
        self.destination_id = destination_id
        self.minimum_cost = minimum_cost

    def __str__(self):
        return f'source_id : {self.source_id} \n destination id : {self.destination_id}\ncosts : {self.minimum_cost}'

class DistanceTable:
    def __init__(self):
        self.costs = [[infinite for j in range(4)] for i in range(4)]



class Event:
    def __init__(self, evtime=None, evtype=None, eventity=None, rtpktptr=None):
        self.evtime = evtime
        self.evtype = evtype
        self.eventity = eventity
        self.rtpktptr = rtpktptr

    def __repr__(self):
        return ('Event Object:\n'
                '  Time: %s\n'
                '  Type: %s\n'
                '  Entity: %s\n'
                '  Packet: \n%s\n' % (self.evtime, self.evtype,
                                      self.eventity, self.rtpktptr))

# possible events:
From_Node = 2
LINK_CHANGE = 10


def insertevent(p):

    if TRACE > 3:
        print("            INSERTEVENT: time is %lf\n" % clocktime)
        print("            INSERTEVENT: future time will be %lf\n" % p.evtime)

    event_list.append(p)
    event_list.sort(key=lambda e: e.evtime)

def printevlist():
    print("--------------\nEvent List Follows:\n")
    for event in event_list:
        print("Event time: %f, type: %d entity: %d\n" % (event.evtime, event.evtype, event.eventity))
    print("--------------\n")


def toNode(packet):
    mypktptr = copy.deepcopy(packet)
    if TRACE > 2:
        print("    TOLAYER2: source: %d, dest: %d\n              costs:" %
              (mypktptr.source_id, mypktptr.destination_id))
        for i in range(4):
            print("%d  " % (mypktptr.mincost[i]))
        print("\n")

    # create future event for arrival of packet at the other side
    evptr = Event(evtype=From_Node, eventity=packet.destination_id, rtpktptr=mypktptr)

    # finally, compute the arrival time of packet at the other end.
    # medium can not reorder, so make sure packet arrives between 1 and 10
    # time units after the latest arrival time of packets
    # currently in the medium on their way to the destination
    lastime = clocktime
    for q in event_list:
        if ( (q.evtype == From_Node)  and (q.eventity == evptr.eventity) ):
            lastime = q.evtime
    evptr.evtime =  lastime + 2. * random.uniform(0, 1)


    if TRACE > 2:
        print("    TOLAYER2: scheduling arrival on other side\n")
    insertevent(evptr)