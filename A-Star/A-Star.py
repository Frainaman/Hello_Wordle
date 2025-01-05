import heapq
import random
import requests
import datetime
from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates")

def load_dictionary(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip().lower() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Errore: il file '{file_path}' non è stato trovato.")
        exit()

# Funzione per ottenere la parola del giorno di Wordle tramite API
def get_word_of_the_day():
    today = datetime.date.today()
    url = f"https://www.nytimes.com/svc/wordle/v2/{today}.json"  # URL dinamico con la data corrente

    try:

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            word = data['solution']
            return word
        else:
            print(f"Errore nella richiesta API: {response.status_code}")
            return None
    except Exception as e:
        print(f"Errore nella richiesta API: {e}")
        return None

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def empty(self):
        return len(self.elements) == 0


# Funzione di calcolo del feedback
def feedback_function(guess, solution):
    feedback = ["grey"] * len(guess)
    solution_char_counts = {s: solution.count(s) for s in solution}

    for i, (g, s) in enumerate(zip(guess, solution)):
        if g == s:
            feedback[i] = "green"
            solution_char_counts[g] -= 1

    for i, g in enumerate(guess):
        if feedback[i] == "grey" and g in solution_char_counts and solution_char_counts[g] > 0:
            feedback[i] = "yellow"
            solution_char_counts[g] -= 1

    return feedback

def feedback_to_emoji(feedback):
    emoji_map = {
        "green": "🟩",
        "yellow": "🟨",
        "grey": "⬜"
    }
    return "".join(emoji_map[f] for f in feedback)

# Funzione di filtraggio delle parole in base al feedback
def filter_candidates(candidates, guess, feedback):

    return [
        word for word in candidates
        if feedback_function(guess, word) == feedback
    ]

# Euristica per calcolare il punteggio di una parola
def heuristic(word, candidates):
    letter_frequencies = {}
    for candidate in candidates:
        for letter in set(candidate):
            letter_frequencies[letter] = letter_frequencies.get(letter, 0) + 1

    unique_letters = len(set(word))
    score = sum(letter_frequencies.get(char, 0) for char in set(word))
    duplicate_penalty = len(word) - unique_letters  # Penalize duplicates

    return score + unique_letters - duplicate_penalty

def max_score(candidates, scores):
    return max(zip(scores, candidates))[1]

def wordle_solver(dictionary, feedback_function, solution, max_attempts=6):
    open_set = PriorityQueue()
    initial_guess = random.choice(dictionary)
    open_set.put((initial_guess, dictionary), 0)
    attempts = 0

    while not open_set.empty() and attempts < max_attempts:
        attempts += 1
        current_word, candidates = open_set.get()

        feedback = feedback_function(current_word, solution)
        print(f"Tentativo {attempts}: {current_word} -> {feedback_to_emoji(feedback)}")
        if all(color == "green" for color in feedback):
            return current_word, attempts

        new_candidates = filter_candidates(candidates, current_word, feedback)
        if not new_candidates:
            break

        scores = [heuristic(word, new_candidates) for word in new_candidates]
        next_guess = max_score(new_candidates, scores)
        open_set.put((next_guess, new_candidates), attempts)

    return None, attempts

@app.route("/")
def webapp():
    dictionary_path = "../dictionary"
    dictionary = load_dictionary(dictionary_path)
    solution = get_word_of_the_day() #Alternativa: random.choice(dictionary)
    attempts_log = []  #Per tenere traccia dei tentativi

    def feedback_function_logging(guess, solution):
        feedback = feedback_function(guess, solution)
        attempts_log.append({"guess": guess, "feedback": feedback})
        return feedback

    guessed_word, attempts = wordle_solver(dictionary, feedback_function_logging, solution)

    # Passa i dati alla pagina HTML
    return render_template(
        "A-Star.html",
        solution=solution,
        attempts_log=attempts_log,
        success=guessed_word is not None,
        guessed_word=guessed_word,
    )

# Demo
if __name__ == "__main__":
    app.run(debug=True)
