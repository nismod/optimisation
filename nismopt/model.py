# Isinglecomm.py
# NodesIn and NodesOut are intialized using the Arcs
from pyomo.environ import AbstractModel, Set, NonNegativeReals, Constraint, \
                          Param, Var, Objective, summation, minimize

# Create an instance of an abstract model
model = AbstractModel()

# The model contains a set of nodes and a set of arcs between the nodes
model.Nodes = Set()
model.Arcs = Set(dimen=2)

def NodesOut_init(model, node):
    """Initialises nodes from the data
    """
    retval = []
    for (i,j) in model.Arcs:
        if i == node:
            retval.append(j)
    return retval
model.NodesOut = Set(model.Nodes, initialize=NodesOut_init)

def NodesIn_init(model, node):
    """Initialises nodes from data
    """
    retval = []
    for (i,j) in model.Arcs:
        if j == node:
            retval.append(i)
    return retval
model.NodesIn = Set(model.Nodes, initialize=NodesIn_init)

# The decision variable is the level of flow along the arcs (edges)...
model.Flow = Var(model.Arcs, domain=NonNegativeReals)
# ...and there is an associated cost with the flow
model.FlowCost = Param(model.Arcs)

# Optional demand and supply is defined at the nodes
model.Demand = Param(model.Nodes)
model.Supply = Param(model.Nodes)

def Obj_rule(model):
    """The Objective Function

    Computes the dot product of Flowcost and Flow across arcs
    """
    return summation(model.FlowCost, model.Flow)

model.Obj = Objective(rule=Obj_rule, sense=minimize)

def FlowBalance_rule(model, node):
    """Ensures that flows into and out of a node are equal

    """
    return model.Supply[node] \
     + sum(model.Flow[i, node] for i in model.NodesIn[node]) \
     - model.Demand[node] \
     - sum(model.Flow[node, j] for j in model.NodesOut[node]) \
     == 0

# The flowbalance rule is defined as a constraint that operates on each node
model.FlowBalance = Constraint(model.Nodes, rule=FlowBalance_rule)
