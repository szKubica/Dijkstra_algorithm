# !!! Kod programu na gałęzi master !!! 

## Uruchomienie

Windows:

```bash
python main.py
```
Linux:
```bash
python3 main.py
```
## Output

```python
################ GRAF W POSTACI MACIERZY SĄSIEDZTWA ################
Koszty dojścia:
Wierzchołek 0: 0
Wierzchołek 1: 4
Wierzchołek 2: 3
Wierzchołek 3: 6
Wierzchołek 4: 7
Wierzchołek 5: 9

Czas wykonania: 1.049041748046875e-05 seconds
Reprezentacja:  [[0, 5, 3, 0, 0, 0], [0, 0, 0, 2, 0, 0], [0, 1, 0, 3, 0, 0], [0, 0, 0, 0, 1, 5], [0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0]]
################ GRAF W POSTACI LISTY SĄSIEDZTWA ################
Koszty dojścia:
Wierzchołek 0: 0
Wierzchołek 1: 4
Wierzchołek 2: 3
Wierzchołek 3: 6
Wierzchołek 4: 7
Wierzchołek 5: 9

Czas wykonania: 7.62939453125e-06 seconds
Reprezentacja:  [[(1, 5), (2, 3)], [(3, 2)], [(1, 1), (3, 3)], [(4, 1), (5, 5)], [(5, 2)], []]
################ GRAF PRZEDSTAWIONY ZA POMOCĄ BIBLIOTEKI networkx ################
Koszty dojścia:
Wierzchołek 0: 0
Wierzchołek 1: 4
Wierzchołek 2: 3
Wierzchołek 3: 6
Wierzchołek 4: 7
Wierzchołek 5: 9

Czas wykonania: 2.193450927734375e-05 seconds
Reprezentacja:  [(0, 1, {'weight': 5}), (0, 2, {'weight': 3}), (1, 3, {'weight': 2}), (1, 2, {'weight': 1}), (2, 3, {'weight': 3}), (3, 4, {'weight': 1}), (3, 5, {'weight': 5}), (4, 5, {'weight': 2})]

```
