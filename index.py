


from rich.console import Console
from rich.panel import Panel
from rich.text import Text, Style
from rich.progress import track
from pyfiglet import figlet_format
import time
from rich.prompt import Prompt
import cursor
import random

console = Console()


def cursor_blink_timeout(timeout_seconds):
    end_time = time.time() + timeout_seconds
    cursor_visible = True
    while time.time() < end_time:
        if cursor_visible:
            cursor.hide()
        else:
            cursor.show()
        cursor_visible = not cursor_visible
        time.sleep(0.5)  # Adjust the blink interval as needed
    cursor.show()  # Ensure the cursor is visible after the timeout

def print_to_screen(text_):
    text = Text(text_, justify="center", style=Style(bold=True, color="magenta"))
    console.print(text)

def animate_text(text_):
    cursor.hide()  # Hide the cursor
    color = random.choice(["magenta", "blue"])
    try:
        for char in text_:
            console.print(char, end='', style=Style(bold=True, color=color))
            time.sleep(0.07)  # Adjust the sleep time for faster or slower printing
    finally:
        cursor.show()  # Show the cursor again

def print_to_panel(text_):

     # Randomly choose between magenta and blue
    color = random.choice(["magenta", "blue"])

     # Display a panel
    panel = Panel(Text(text_, justify="center", style=Style(bold=True, color=color)))
    console.print(panel)
    


def display_progress_bar(duration_in_seconds, message):
    for _ in track(range(duration_in_seconds), description=message, total=None):
        time.sleep(1)

# Progress bar without timer
duration_in_seconds = 5
message = "Loading..."
display_progress_bar(duration_in_seconds, message)

# Figlet text
text = "KAMILIMU"
pattern = "bold"  # Choose a pattern from available options
pattern_text = figlet_format(text)
print(pattern_text)

duration_in_seconds = 10
message = "Month one Loading..."
display_progress_bar(duration_in_seconds, message)

# Progress bar without timer
duration_in_seconds = 10
message = "Month two Loading..."
display_progress_bar(duration_in_seconds, message)

# Display a panel
text = "What? Wait a minute though..."
print_to_panel(text)

duration_in_seconds = 15
message = "A minute"
display_progress_bar(duration_in_seconds, message)

# Display a panel
text = "Let's actually talk about month 2"
print_to_screen(text)

name = Prompt.ask("Shall we?", default="Yes")

# Clear the screen
console.clear()

if name:
    # Display a panel
    text = "Cool, Here goes...\nPickings from individual lessons"
    animate_text(text)
    console.clear()
    print_to_panel(text)

# Define the string with new line characters
scholarship_tips = """Scholarship101
Writing winning essays
"It's a life changing experience whether or not you get in"
Think about the organisation - It's values/mission. Do they align with yours?
Relate with the organisation
First impressions matter. Pay attention to details.
Now to the first paragraph -> "lead strongly, the rest will follow"
You want your words to leave the reader eager to meet you in person.
The middle -> It's all about shedding the light on your personal journey.
The transistions should be idea based
The Ending -> "Why are you the most suitable candidate?"
Hey, don't forget to sleep on your essays."""

animate_text(scholarship_tips)
print_to_screen("Let that sink in first.")
cursor_blink_timeout(10)
console.clear()
print_to_panel(scholarship_tips)

public_speaking_tips = """Public Speaking
What should the audience grasp firmly in their hearts after experiencing this speech?
That should be expressed in one statement, very precise, realistic and achievable as well.
Of course, Pathos, Logos, Ethos
Ethos -> speaks to your credibility as a speaker, what are you known for.
Pathos -> Evoke emotions, connect through vulnerability, influence perception
Logos -> Appeals to logic, be logical, be comprehensive, be specific."""


display_progress_bar(10, "Loading another session that hit home....")
console.clear()
animate_text(public_speaking_tips)
console.clear()
print_to_panel(public_speaking_tips)
print_to_screen("Digest that as well.")
cursor_blink_timeout(10)
console.clear()


# Figlet text
text = "adios"
pattern = "bold"  # Choose a pattern from available options
pattern_text = figlet_format(text)
print(pattern_text)

print_to_screen("That was fun, till next time \U0001F44B \U00002764\U0000FE0F")

cursor_blink_timeout(10)






















