# Authentication Module Lab

Educational authentication examples in Python and Java, including a Flask API and a browser interface. The repository is useful for examining how registration, password verification, and session handling fit together.

## Repository guide

| Path | Purpose |
| --- | --- |
| [auth.py](auth.py) | Salt generation, SHA-256 hashing, and JSON user storage helpers. |
| [user.py](user.py) and [user_registration.py](user_registration.py) | User representation and registration logic. |
| [main.py](main.py) | Interactive command-line example. |
| [api.py](api.py) | Flask registration, login, logout, and protected profile endpoints. |
| [index.html](index.html), [login.html](login.html), [register.html](register.html) | Browser pages served by the Flask example. |
| [Authinpl/](Authinpl/) | Java authentication examples and Eclipse project files. |
| [test_auth.py](test_auth.py), [test_user_registration.py](test_user_registration.py), [test_api.py](test_api.py) | Python unittest examples. |

## Python entry points

Run commands from the repository root in a disposable local copy. The CLI uses the Python standard library; the web example also imports Flask. The repository does not include a pinned dependency manifest.

```bash
python main.py
python api.py
```

Choose the entry point you want to explore. The API's `__main__` block starts Flask in debug mode. Browser pages are available through that Flask server.

## API overview

| Request | Behavior |
| --- | --- |
| `POST /register` | Register a username and password. |
| `POST /login` | Verify credentials and return a session token. |
| `POST /logout` | Remove the supplied session token. |
| `GET /profile` | Return a greeting for an authenticated session. |

Protected requests use the token directly in the `Authorization` header. Sessions are held in process memory.

## Teaching scope

The Python implementation hashes a password plus a random salt with SHA-256. This is a teaching example for examining authentication design; it is not a production authentication package. Registration writes to local JSON user storage, and the API does not add session expiry or persistence across server restarts.

Use fictional users in an isolated copy. The included tests are source examples; their presence does not establish a passing test run. Check storage behavior before running them, because registration helpers write files.

The Java examples are a separate source tree. Their build and runtime compatibility have not been verified here.
