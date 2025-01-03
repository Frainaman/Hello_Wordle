from flask import Flask, render_template
import random
import requests
import datetime

app = Flask(__name__, template_folder="../templates")

def load_dictionary(file_path):
    with open(file_path, "r") as file:
        return [line.strip().lower() for line in file if line.strip()]

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

# Funzione di calcolo del feedback
def feedback_function(guess, solution):
    feedback = ["grey"] * len(guess)
    solution_char_counts = {s: solution.count(s) for s in solution}

    for i, (g, s) in enumerate(zip(guess, solution)):
        if g == s:
            feedback[i] = "green"
            solution_char_counts[g] -= 1

    for i, g in enumerate(guess):
        if feedback[i] == "green":
            continue
        if g in solution_char_counts and solution_char_counts[g] > 0:
            feedback[i] = "yellow"
            solution_char_counts[g] -= 1

    return feedback

def minimax_algorithm(candidates, feedback_log=None):
    # Primo tentativo: scegli una parola casuale
    if feedback_log is None or len(feedback_log) == 0:
        return random.choice(candidates)

    # Semplificazione euristica: viene scelta la parola che è valida per il maggior numero di scenari
    best_guess = None
    best_score = -1

    for word in candidates:
        score = 0
        for feedback in feedback_log:
            simulated_feedback = feedback_function(word, feedback["guess"])
            if simulated_feedback == feedback["feedback"]:
                score += 1

        if score > best_score:
            best_score = score
            best_guess = word

    return best_guess

def wordle_minimax(dictionary, solution, max_attempts=6):
    candidates = dictionary[:]
    attempts_log = []
    success = False

    for attempt_number in range(max_attempts):
        if not candidates:
            break

        guess = minimax_algorithm(candidates, attempts_log)

        feedback = feedback_function(guess, solution)
        attempts_log.append({"guess": guess, "feedback": feedback})

        if feedback == ["green"] * len(solution):
            success = True
            break

        candidates = [word for word in candidates if feedback_function(guess, word) == feedback]

    return attempts_log, success

@app.route("/")
def webapp():
    dictionary_path = "../dictionary"
    dictionary = load_dictionary(dictionary_path)
    word_of_the_day =  get_word_of_the_day() #Alternativa: random.choice(dictionary)
    attempts_log, success = wordle_minimax(dictionary, word_of_the_day)

    formatted_attempts_log = [
        [
            {"letter": letter, "feedback": feedback}
            for letter, feedback in zip(attempt["guess"], attempt["feedback"])
        ]
        for attempt in attempts_log
    ]

    return render_template(
        "Minimax.html",
        word_of_the_day=word_of_the_day,
        attempts_log=formatted_attempts_log,
        success=success,
    )

if __name__ == "__main__":
    app.run(debug=True)
