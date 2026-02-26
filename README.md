# Build Automation Demo (Jenkins + Tests + Docker)

## What this demo shows
- Jenkins pipeline automation:
  - Checkout
  - Install dependencies
  - Run unit tests (quality gate)
  - Build Docker image (only if tests pass)
  - Run container + smoke test

## How to trigger a failure (for demo)
In `tests/test_app.py`, change:
`assert app.add(1, 2) == 3`
to:
`assert app.add(1, 2) == 4`

Then push commit again — Jenkins should fail in the Unit Tests stage and block the Docker stages.