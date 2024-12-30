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

#Funzione di filtraggio delle parole in base al feedback
def filter_candidates(candidates, guess, feedback):
    if feedback is None:
        return candidates

    filtered = []
    for word in candidates:
        valid = True
        for i, (g,f) in enumerate(zip(guess, feedback)):
            if f == "green" and word[i] != g:
                valid = False
                break
            elif f == "yellow" and (g not in word or word[i] == g):
                valid = False
                break
            elif f == "grey" and g in word:
                valid = False
                break
        if valid:
            filtered.append(word)
    return filtered

#Euristica per calcolare il punteggio di una parola
def heuristic(word, feedback, candidates):
    return len(candidates)