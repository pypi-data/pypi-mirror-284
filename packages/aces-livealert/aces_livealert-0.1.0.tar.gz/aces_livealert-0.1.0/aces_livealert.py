# aces_livealert.py
import typer

app = typer.Typer()

@app.command()
def hello(name: str):
  """
  Say hello to NAME, optionally with --uppercase.
  """
  typer.echo(f"Hello {name}!")

if __name__ == "__main__":
    app()
