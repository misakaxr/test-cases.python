# Test Cases (Python)

A practice project for TDD (pytest) and BDD (behave) using a simple bank account model.

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run TDD tests

```bash
python -m pytest -v
```

## Run BDD scenarios

```bash
behave
```

## Check coverage

```bash
coverage run -m pytest
coverage report -m
```