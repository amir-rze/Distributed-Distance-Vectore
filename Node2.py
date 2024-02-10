from Logic import infinite, RoutingPacket, DistanceTable, toNode

dt = DistanceTable()

edges = [3, 1, 0, 2]
cost = [3, 1, 0, 2]
node_id = 2


def rtinit2():
    for i in range(4):
        if i == node_id:
            continue
        dt.costs[i][i] = edges[i]

    printdt2(dt)

    toNode(RoutingPacket(node_id, 0, edges))
    toNode(RoutingPacket(node_id, 1, edges))
    toNode(RoutingPacket(node_id, 3, edges))


def rtupdate2(rcvdpkt):
    changed = False
    source_id = rcvdpkt.source_id
    distance_table = rcvdpkt.minimum_cost

    for i in range(4):
        new_cost = edges[source_id] + distance_table[i]
        dt.costs[i][source_id] = min(dt.costs[i][source_id], new_cost)
        if new_cost < cost[i]:
            changed = True
            cost[i] = new_cost

    printdt2(dt)
    if changed:
        toNode(RoutingPacket(node_id, 0, cost))
        toNode(RoutingPacket(node_id, 1, cost))
        toNode(RoutingPacket(node_id, 3, cost))


def printdt2(dt):
    print("                     \n")
    print("   D2 |    0     1    3 \n")
    print("  ----|-----------------\n")
    print("     0|  %3d   %3d   %3d\n" %
          (dt.costs[0][0], dt.costs[0][1], dt.costs[0][3]))
    print("     1|  %3d   %3d   %3d\n" %
          (dt.costs[1][0], dt.costs[1][1], dt.costs[1][3]))
    print("     3|  %3d   %3d   %3d\n" %
          (dt.costs[3][0], dt.costs[3][1], dt.costs[3][3]))
