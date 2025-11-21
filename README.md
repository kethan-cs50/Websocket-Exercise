# WebSocket Client & Server — Coding Exercise

This repository contains a simple Python WebSocket server and client built for the **Synapse Coding Exercise**.

**Original assignment (reference):** `Coding Exercise @ Synapse.pdf`

---

## Project overview

* **Server:** `myws/server.py` — exposes a small RPC-like JSON protocol over WebSocket.
* **Client:** `myws/client.py` — contains `async` functions that call server functions.
* **Function implemented:** `average(a, b) -> (a + b) / 2`.
* **Tests:** `tests/test_functions.py` (unit tests) and `tests/test_e2e.py` (end-to-end tests).

The client sends requests like:

```json
{
  "id": 1,
  "fn": "average",
  "args": [10, 20]
}
```

And receives responses like:

```json
{
  "id": 1,
  "result": 15.0,
  "error": null
}
```

---

## Setup

1. Create and activate a virtual environment (Windows example):

```powershell
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

---

## Running

### Run the server (from project root)

```powershell
python -m myws.server
```

Server prints:

```
WebSocket server running at ws://localhost:8765
```

Leave it running while you run the client.

### Run the client (in a new terminal)

```powershell
python -m myws.client
```

Example output:

```
Average of 10 and 20 = 15.0
Average of 5 and 15 = 10.0
Average of 100 and 50 = 75.0
```

---

## Tests

Make sure no server process is running (tests start their own server).

Run all tests from the project root:

```powershell
pytest -q
```

Expected output:

```
4 passed in X.XXs
```

Notes:

* The e2e tests use `asyncio.run()` wrappers (synchronous tests) to avoid `pytest-asyncio` collection issues on some environments.

---

## Files

* `myws/server.py` — server implementation and `average` function.
* `myws/client.py` — async client function `call_average` and demo `demo()`.
* `tests/test_functions.py` — unit tests for `average()`.
* `tests/test_e2e.py` — end-to-end tests that start the server and call the client.
* `requirements.txt` — pinned dependencies.
