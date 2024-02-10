from Logic import infinite, RoutingPacket, DistanceTable, toNode

dt = DistanceTable()

edges = [7, infinite, 2, 0]
cost = [7, infinite, 2, 0]
node_id = 3


def rtinit3():
    for i in range(4):
        if i == node_id:
            continue
        dt.costs[i][i] = edges[i]

    printdt3(dt)
    toNode(RoutingPacket(node_id, 0, edges))
    toNode(RoutingPacket(node_id, 2, edges))


def rtupdate3(rcvdpkt):
    changed = False
    source_id = rcvdpkt.source_id
    distance_table = rcvdpkt.minimum_cost

    for i in range(4):
        new_cost = edges[source_id] + distance_table[i]
        dt.costs[i][source_id] = min(dt.costs[i][source_id], new_cost)
        if new_cost < cost[i]:
            changed = True
            cost[i] = new_cost

    printdt3(dt)
    if changed:
        toNode(RoutingPacket(node_id, 0, cost))
        toNode(RoutingPacket(node_id, 2, cost))


def printdt3(dt):
    print("                    \n")
    print("   D3 |    0     2 \n")
    print("  ----|-----------\n")
    print("     0|  %3d   %3d\n" % (dt.costs[0][0], dt.costs[0][2]))
    print("     1|  %3d   %3d\n" % (dt.costs[1][0], dt.costs[1][2]))
    print("     2|  %3d   %3d\n" % (dt.costs[2][0], dt.costs[2][2]))
