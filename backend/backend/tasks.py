from .celery import app

@app.task
def hello_planet(planet: str):
    """This is a sample celery task. Feel free to remove it."""
    print(f"Hello {planet}!")
