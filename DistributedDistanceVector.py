import random

from Logic import LINKCHANGES, TRACE, YES, NO, \
    From_Node, LINK_CHANGE, \
    RoutingPacket, Event, event_list, clocktime, insertevent
from Node0 import rtinit0, rtupdate0
from Node1 import rtinit1, rtupdate1
from Node2 import rtinit2, rtupdate2
from Node3 import rtinit3, rtupdate3


def main():
    init()
    while event_list:
        event = event_list.pop(0)
        if TRACE > 1:
            if event.evtype == From_Node:
                print(" source :%2d," % event.rtpktptr.source_id)
                print(" destination :%2d," % event.rtpktptr.destination_id)
                print(" contents: %3d %3d %3d %3d\n" %
                      (event.rtpktptr.minimum_cost[0], event.rtpktptr.minimum_cost[1],
                       event.rtpktptr.minimum_cost[2], event.rtpktptr.minimum_cost[3]))
        clocktime = event.evtime

        if event.evtype == From_Node:
            if event.eventity == 0:
                rtupdate0(event.rtpktptr)
            elif event.eventity == 1:
                rtupdate1(event.rtpktptr)
            elif event.eventity == 2:
                rtupdate2(event.rtpktptr)
            elif event.eventity == 3:
                rtupdate3(event.rtpktptr)
            else:
                print("unknown event entity\n")
                exit(0)
        else:
            print("unknown event type\n")
            exit(0)
        if event.evtype == From_Node:
            del event.rtpktptr
        del event

    print("\nSimulator terminated at t=%f, no packets in medium\n" % clocktime)


def init():

    global TRACE

    TRACE = int(input("TRACE for test :"))

    random.seed()  # init random number generator
    clocktime = 0.0  # initialize time to 0.0
    rtinit0()
    rtinit1()
    rtinit2()
    rtinit3()


if __name__ == '__main__':
    main()