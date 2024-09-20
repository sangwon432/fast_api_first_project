from app.main import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

# asgi

# wsgi

# gunicorn

# poetry run coverage run -m pytest .
