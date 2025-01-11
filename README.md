# HelloWordle
Un'implementazione di algoritmi di ricerca per risolvere il popolare gioco Wordle utilizzando approcci di fondamenti di intelligenza artificiale.

Descrizione
Questa repository contiene due algoritmi principali per risolvere il gioco Wordle:

Algoritmo Minimax: Una ricerca ottimizzata che esplora le opzioni più promettenti in base al feedback ottenuto da ogni tentativo.
Algoritmo Greedy Best-First: Un algoritmo di ricerca best-first che sfrutta un'euristica per determinare la migliore parola successiva da provare, in base alla valutazione delle lettere e dei feedback.
I metodi sono implementati in Python, con un'applicazione web basata su Flask che consente di testare gli algoritmi in un'interfaccia grafica.

Sviluppato in Python 3.8. Altri requisiti nel file requirements.txt.

La cartella Greedy contiene il codice eseguibile dell'algoritmo basato su best-first greedy (Best-first_greedy.py).
La cartella Minimax contiene il codice eseguibile dell'algoritmo basato su minimax (Minimax.py).
La cartella templates contiene i file html per la visualizzazione della webapp (Greedy.html, Minimax.html).
Presente il file dictionary.txt con il dizionario target del problema.

Eseguire con Python Interpreter.
