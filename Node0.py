from Logic import infinite ,RoutingPacket,DistanceTable,toNode

edges = [0,1,3,7]
cost = [0,1,3,7]
node_id = 0

dt = DistanceTable()

def rtinit0():
    for i in range(4):
        if i == node_id :
            continue
        dt.costs[i][i] = edges[i]
    printdt0(dt)

    toNode(RoutingPacket(node_id,1,edges))
    toNode(RoutingPacket(node_id,2,edges))
    toNode(RoutingPacket(node_id,3,edges))


def rtupdate0(rcvdpkt):
    changed = False
    source_id = rcvdpkt.source_id
    distance_table = rcvdpkt.minimum_cost

    for i in range(4):
        new_cost = edges[source_id] + distance_table[i]
        dt.costs[i][source_id] = min(dt.costs[i][source_id], new_cost)
        if new_cost < cost[i]:
            changed = True
            cost[i] = new_cost

    printdt0(dt)

    if changed:
        toNode(RoutingPacket(node_id,1,cost))
        toNode(RoutingPacket(node_id,2,cost))
        toNode(RoutingPacket(node_id,3,cost))


        
def printdt0(dt):
    print("                        \n")
    print("   D0 |    1     2    3 \n")
    print("  ----|-----------------\n")
    print("     1|  %3d   %3d   %3d\n" %
          (dt.costs[1][1], dt.costs[1][2], dt.costs[1][3]))
    print("     2|  %3d   %3d   %3d\n" %
          (dt.costs[2][1], dt.costs[2][2], dt.costs[2][3]))
    print("     3|  %3d   %3d   %3d\n" %
          (dt.costs[3][1], dt.costs[3][2], dt.costs[3][3]))


