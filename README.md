# Hello Wordle
Hello Wordle is a project that implements two intelligent algorithms, **Minimax** and **Greedy Best-First**, to solve the popular word-guessing game **Wordle**.
The project combines algorithmic efficiency and heuristic-based optimization to simulate agents capable of solving Wordle puzzles effectively.

This project was created as part of an academic exploration of artificial intelligence techniques and their applications in real-world problems.

## Key Idea
The project stems from the challenge of creating agents that can solve Wordle puzzles optimally while minimizing the number of guesses. Wordle provides an ideal testbed for algorithms that combine heuristics, filtering, and iterative improvements to achieve accurate results efficiently.

The main focus is to evaluate and compare two approaches:

- *Greedy Best-First Search*: This algorithm prioritizes guesses based on a heuristic score, favoring words that provide maximum information gain.
- *Minimax Search*: This algorithm simulates the worst-case feedback scenario for each potential guess and chooses the word that minimizes the maximum uncertainty.
## Goal and Approach
The primary goal of this project is to evaluate the performance of Minimax and Greedy Best-First in solving Wordle, focusing on:

The number of guesses needed to solve puzzles.
The computational efficiency of each approach.
Both approaches leverage heuristics to rank guesses and improve the filtering process after receiving feedback.

## File Structure
The project is organized into the following structure:

- Main Directories
  - Greedy/ Contains the implementation of the Greedy Best-First Search algorithm.
   *Best-first_greedy.py*: The main executable for the Greedy solver.
  - Minimax/
     Contains the implementation of the Minimax algorithm.
     *Minimax.py*: The main executable for the Minimax solver.

  - templates/
  Contains HTML files for the web app.

    - *Greedy.html*: Visualization for the Greedy Best-First solver.
    - *Minimax.html*: Visualization for the Minimax solver.
## Additional Files
*dictionary.txt*:
Contains the word list used for Wordle-solving algorithms.

The docs folder contains the project report.

## How to run
To run the project, you'll have to install Python 3.8, and install all packages in requirements.txt through pip.

Run any of the two algorithm you want through the wirtual environment with a Python interpreter.
Once the server starts, open the brower and go to http://127.0.0.1:5000
