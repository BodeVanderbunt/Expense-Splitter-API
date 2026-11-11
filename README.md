# Expense Splitter API

A backend API for splitting shared expenses within groups, built with Python and FastAPI.

## Status

In development. Currently working: user creation and listing.

## Tech stack

- Python, FastAPI
- SQLAlchemy with SQLite (PostgreSQL planned)
- pytest (planned)

## Run locally

```
python -m venv venv
venv\Scripts\activate
pip install "fastapi[standard]" sqlalchemy pytest
fastapi dev main.py
```

Then open http://127.0.0.1:8000/docs to try the endpoints.

## Roadmap

- [x] Users
- [ ] Groups and members
- [ ] Expenses and splits
- [ ] Balances and debt simplification
- [ ] Authentication, tests, Docker, deployment
- [ ] TypeScript/React front end
