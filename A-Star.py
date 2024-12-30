import heapq

#Priority Queue
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def empty(self):
        return len(self.elements) == 0

#Funzione di calcolo del feedback
def feedback_function(guess, solution):
    feedback = []
    for g, s in zip(guess, solution):
        if g == s:
            feedback.append("green")
        elif g in solution:
            feedback.append("yellow")
        else:
            feedback.append("grey")
    return feedback
