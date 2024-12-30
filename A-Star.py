import heapq
import random
from dictionary import dictionary


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

def feedback_to_emoji(feedback):
    emoji_map = {
        "green": "🟩",  # Lettera giusta nella posizione giusta
        "yellow": "🟨",  # Lettera presente ma nella posizione sbagliata
        "grey": "⬜"     # Lettera non presente
    }
    return "".join(emoji_map[f] for f in feedback)

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

def wordle_solver(dictionary, feedback_function, solution, max_attempts=6):
    open_set = PriorityQueue()
    randGuess = random.choice(dictionary)
    open_set.put((randGuess,dictionary), 0)
    attempts = 0

    while not open_set.empty() and attempts < max_attempts:
        attempts += 1
        current_word, candidates = open_set.get()

        if current_word:
            feedback = feedback_function(current_word, solution)
            print(f"Tentativo {attempts}: {current_word} -> {feedback_to_emoji(feedback)}")
            if all(color == "green" for color in feedback):
                return current_word, attempts
        else:
            feedback = None

        new_candidates = filter_candidates(candidates, current_word, feedback)

        for word in new_candidates:
            g = attempts
            h = heuristic(word, feedback, new_candidates)
            open_set.put((word, new_candidates), g+h)

    return None, attempts

if __name__ == "__main__":
    solution = random.choice(dictionary)
    guessed_word, attempts = wordle_solver(dictionary, feedback_function, solution)
    if guessed_word:
        print(f"Soluzione trovata: {guessed_word} in {attempts} tentativi!")
    else:
        print("Soluzione non trovata.")