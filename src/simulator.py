import random

class RumorSimulator:
    def __init__(self, graph, beta = 0.3, gamma = 0.1):
        self.graph = graph
        self.beta = beta #P(spreading rumor)
        self.gamma = gamma #P(recovery)
        self.status = {} #Nodes can be S, I, or R

    def initialize(self, infected_nodes):
        for node in self.graph.nodes():
            self.status[node] = "S"
        for node in infected_nodes:
            self.status[node] = "I"

    def step(self):
        new_status = self.status.copy()
        for node in self.graph.nodes():
            if self.status[node] == 'I':
                for neighbour in self.graph.neighbors(node):
                    if self.status[neighbour] == 'S':
                        if random.random()<self.beta:
                            new_status[neighbour] = 'I'
                if random.random()<self.gamma:
                    new_status[node] = "R"
        self.status = new_status

    def run(self, steps = 10):
        history = []
        for _ in range(steps):
            self.step()
            history.append(self.status.copy())
        return history
