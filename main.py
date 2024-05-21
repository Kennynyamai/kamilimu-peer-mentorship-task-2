# Save this code in a file named fun_cli.py

import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text, Style
from rich.progress import track
from pyfiglet import figlet_format
import time

from rich.prompt import Prompt

console = Console()

# Figlet text
text = "KAMILIMU"
pattern = "bold"  # Choose a pattern from available options
pattern_text = figlet_format(text)
print(pattern_text)

# Display a panel
panel = Panel(Text("Hello\nhaiya", justify="center", style=Style(bold=True, color="magenta")))
console.print(panel)

# Progress bar without timer
for _ in track(range(20), description="Month one Loading...", total=None):
    # Simulate work being done (replace with your actual work)
    time.sleep(1)


# Progress bar without timer
for _ in track(range(20), description="Month two Loading...", total=None):
    # Simulate work being done (replace with your actual work)
    time.sleep(1)

console.clear()




name = Prompt.ask("Can we start?", default="Yes")

if(name):
    text = Text("Great, so lets actually talk about month 2", justify="center", style=Style(bold=True, color="magenta"))
    console.print(text)

