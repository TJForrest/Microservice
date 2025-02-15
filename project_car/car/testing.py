import typer 
import os 
from rich import print 
from rich.panel import Panel 
from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from rich.columns import Columns  # For side-by-side display

# Create a Typer app
app = typer.Typer()
console = Console()

# Clear screen function
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear") 

# Exit command text
exit_panel = Panel("[bold]Type 'exit' or 'quit' to leave program[/bold]", style="bold red")

# Home and Help page titles
md_hm_title = Markdown("# *PROJECT CAR*")
md_hlp_title = Markdown("# *HELP PAGE*")

# Navigation bars (centered)
cnt_hom = Text("Help | Garage | Maintenance | Gas | Notes", justify="center") 
cnt_hlp = Text("Home | Garage | Maintenance | Gas | Notes", justify="center")  

# Home page info
home_info = Text("""Welcome to your virtual garage.
Here you can track maintenance, 
log gas mileage, create notes about your project cars,
and store details about your vehicles.

Type "help" at any time to see available commands.
""", justify="center")

# Maintenance reminders text box (Placeholder for updates)
mr_jobs = "Add Some Maintenance Tasks"

# Help page info
help_info = Text("""This section provides details on available commands.
Use these to navigate through the system.""", justify="left")

help_command_list = Text("""
[bold cyan]Available Commands:[/bold cyan]
- home → Go to Home Page
- help → Show Help Menu
- garage → Open Garage
- maintenance → View Maintenance Log
- gas → Track Gas Mileage
- notes → Open Notes Section
""", justify="left")

# Home page command 
@app.command()
def home():
    clear_screen()
    print(exit_panel)
    print(md_hm_title)
    print(Panel(home_info))
    print(Panel(mr_jobs, title="Maintenance Reminders"))
    print(Panel(cnt_hom, title="Navigation"))

# Help page command (Updated to use Columns for side-by-side layout)
@app.command()
def help():
    clear_screen()
    print(exit_panel)
    print(md_hlp_title)
    print(Panel(cnt_hlp, title="Navigation"))

    # Create two panels and place them side by side using Columns
    side_by_side_panels = Columns([
        Panel(help_command_list, title="Commands", style="bold cyan"),
        Panel(help_info, title="Info", style="bold yellow")
    ])  # Removed equalize_height=True

    # Print the side-by-side panels
    console.print(side_by_side_panels)

# Command dictionary
commands = {
    "home": home,
    "help": help,
}

# Main interactive loop
@app.command()
def procar():
    clear_screen()
    home()
    
    while True:
        user_input = console.input("Enter your command: ").strip().lower() 

        if user_input in ['quit', 'exit']:
            print("[bold red]Exiting...[/bold red]")
            break
        
        elif user_input in commands: 
            commands[user_input]()

        else:
            print("[bold red]Unknown command. Type 'help' for available commands.[/bold red]")

# Run the app
if __name__ == "__main__":
    app()
