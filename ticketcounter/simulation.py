# Implementation of the main simulation class.
from arrays import Array
from queue import Queue
from linkedqueue import LinkedQueue
from simpeople import TicketAgent, Passenger
import random


class TicketCounterSimulation:
    # Create a simulation object.
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i + 1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # Run the simulation using the parameters supplied earlier.
    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    # Print the simulation results.
    def printResults(self):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" % len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)

    # Handles simulation rule #1.
    def _handleArrival(self, curTime):
        number = random.uniform(0, 1)
        if self._arriveProb < number:
            self._numPassengers += 1
            self._passengerQ.enqueue(Passenger(self._numPassengers, curTime))
            print("Time %s." % curTime)
            print("Passenger %s arrived." % self._numPassengers)

    # Handles simulation rule #2.
    def _handleBeginService(self, curTime):
        if not self._passengerQ.isEmpty():
            for agent in self._theAgents:
                if agent.isFree():
                    agent.startService(self._passengerQ.dequeue(), curTime + self._serviceTime)
                    print("Time %s." % curTime)
                    print("Agent {} started serving passenger {}.".format(agent.idNum(), self._numPassengers))
                    break

    # Handles simulation rule #3.
    def _handleEndService(self, curTime):
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                agent.stopService()
                print("Time %s." % curTime)
                print("Agent {} stopped serving passenger {}.".format(agent.idNum(), self._numPassengers))


ticket = TicketCounterSimulation(2, 10, 2, 1)
ticket.run()
