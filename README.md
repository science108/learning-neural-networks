# Projekt do nauki sieci neuronowych

To jest projekt w Pythonie do nauki podstaw sieci neuronowych z PyTorch.

## Co jest w projekcie

- `nn_basic.py` - podstawowy przykład pracy z tensorem PyTorch
- `example_nn.py` - prosty model regresji liniowej z trenowaniem w PyTorch
- `requirements.txt` - lista zależności do instalacji
- `.gitignore` - pliki ignorowane przez Git

## Uruchomienie

1. Aktywuj środowisko:
   ```bash
   source .venv/bin/activate
   ```

2. Zainstaluj wymagania:
   ```bash
   pip install -r requirements.txt
   ```

3. Uruchom przykład:
   ```bash
   python example_nn.py
   ```

## Polecane pakiety

- `torch` - PyTorch, biblioteka do budowy sieci neuronowych
- `numpy` - obliczenia numeryczne
- `matplotlib` - wizualizacje danych
- `scikit-learn` - pomocne narzędzia do uczenia maszynowego

## Git i GitHub

1. Zainicjuj repozytorium, jeśli jeszcze nie jest:
   ```bash
   git init
   ```

2. Dodaj pliki i zatwierdź:
   ```bash
   git add .
   git commit -m "Initial project setup"
   ```

3. Dodaj zdalne repo na GitHub i wypchnij:
   ```bash
   git remote add origin https://github.com/<twoj-login>/<twoje-repo>.git
   git branch -M main
   git push -u origin main
   ```

Zastąp `<twoj-login>` i `<twoje-repo>` własnymi danymi.
