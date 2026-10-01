# Running the API

Run these commands from the assignment folder.

## Start the server

```zsh
apivenv/bin/python -m uvicorn firstapi:app --reload
```

The API is available at <http://127.0.0.1:8000>.

## Stop the server

In the terminal running Uvicorn, press **Ctrl+C**. This shuts down the server cleanly. If you suspended it with **Ctrl+Z**, run `fg` first, then press **Ctrl+C**.