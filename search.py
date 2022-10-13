# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "problem:", problem
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # print "problem:", problem
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())

    fringe = util.Stack()
    """ A fringe, is a data structure used to store all the possible states (nodes) that you can go from the current state """

    visited_list = list()
    """ Keeps track of the states already visited """

    initial_node = tuple((problem.getStartState(), list(), 1))
    """ The initial: starting state, visited list, step cost """

    fringe.push(initial_node)

    while not fringe.isEmpty():
        state, solution_plan, step_cost = fringe.pop()

        # If goal states return solution plan (the sequence of nodes from start node to goal node)
        if problem.isGoalState(state):
            return solution_plan

        # If the node hasn't been visited add to visited list & get the unvisted nodes sucessor nodes to be explored
        if state not in visited_list:
            visited_list.append(state)

            # For each sucessor node check if it has been visited if not add to solution plan & add unvisited node to stack
            for successor_state, successor_action, successor_cost in problem.getSuccessors(state):
                if successor_state not in visited_list:
                    successor_action = solution_plan + [successor_action]
                    unvisited_node = tuple((successor_state, successor_action, 1))
                    fringe.push(unvisited_node)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    visited_list = list()
    initial_node = tuple((problem.getStartState(), list(), 1))
    fringe.push(initial_node)

    while not fringe.isEmpty():
        state, solution_plan, step_cost = fringe.pop()

        if problem.isGoalState(state):
            return solution_plan

        if state not in visited_list:
            visited_list.append(state)

            for successor_state, successor_action, successor_cost in problem.getSuccessors(state):
                if successor_state not in visited_list:
                    successor_action = solution_plan + [successor_action]
                    unvisited_node = tuple((successor_state, successor_action, 1))
                    fringe.push(unvisited_node)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    visited_list = list()
    initial_path_cost = 0
    initial_node = tuple((problem.getStartState(), list(), 0))
    fringe.push(initial_node, initial_path_cost)

    while not fringe.isEmpty():
        state, solution_plan, path_cost = fringe.pop()

        if problem.isGoalState(state):
            return solution_plan

        if state not in visited_list:
            visited_list.append(state)

        for successor_state, successor_action, successor_cost in problem.getSuccessors(state):
            if successor_state not in visited_list:
                successor_action = solution_plan + [successor_action]
                unvisited_node = tuple((successor_state, successor_action, path_cost + successor_cost))
                fringe.push(unvisited_node, successor_cost + path_cost)
                fringe.update(unvisited_node, successor_cost + path_cost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    fringe = util.PriorityQueue()
    visited_list = list()
    estimated_cost_from_node_to_goal = heuristic(problem.getStartState(), problem)
    initial_node = tuple((problem.getStartState(), list(), 0))
    fringe.push(initial_node, estimated_cost_from_node_to_goal)

    while not fringe.isEmpty():
        state, solution_plan, path_cost = fringe.pop()

        if problem.isGoalState(state):
            return solution_plan

        if state not in visited_list:
            visited_list.append(state)

            for successor_state, successor_action, successor_cost in problem.getSuccessors(state):
                if successor_state not in visited_list:
                    successor_action = solution_plan + [successor_action]
                    cost_from_start_to_node = problem.getCostOfActions(successor_action)
                    estimated_cost_from_node_to_goal = heuristic(successor_state, problem)
                    unvisited_node = tuple((successor_state, successor_action, 0))
                    fringe.push(unvisited_node, cost_from_start_to_node + estimated_cost_from_node_to_goal)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
