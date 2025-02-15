import typer 
import os 
from rich import print 
from rich.pretty import Pretty 
from rich.panel import Panel 
from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from rich.live import Live 
from rich.layout import Layout 


# Create a typer app to use app.command to act as functions
app = typer.Typer()

# global console obj 
console = Console()


#JUST FOR TESTING 
test = "TEST"


# Checks the os then calls the approrite terminal clear sig
def clear_screen():
	os.system("cls" if os.name == "nt" else "clear") 


#--------------------------|Markdown Formating|---------------------------------

# Home page title formating --> May change to Ascii art
md_hm_title = Markdown("# *PROJECT CAR*")

# Help page title formating --> May change to Ascii art
md_hlp_title = Markdown("# *HELP PAGE*")

# Garage page title formating --> May change to Ascii art
md_gar_title = Markdown("# *GARAGE*")

# Maintenance page title formating --> May change to Ascii art
md_mat_title = Markdown("# *MAINTENANCE*")

# Gas page title formating --> May change to Ascii art
md_gas_title = Markdown("# *GAS*")

# Notes page title formating --> May change to Ascii art
md_nts_title = Markdown("# *NOTES*")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#----------------------------|Nav bar|------------------------------------------
# Nav Bar - just list of page commands
# broken down for modularity to use on each page with centered instances 
# pass into each corosponding command call
# print(Panel(****, title="Navigation"))

# TEMP TILL MICROS ARE ADDED change to full once implmented  
cnt_hom = Text("Help", justify="center") 
#cnt_hom = Text("Help | Garage | Maintence |Gas | Notes", justify="center") 

# TEMP TILL MICROS ARE ADDED change to full once implmented
cnt_hlp = Text("Home", justify="center") 
#cnt_hlp = Text("Home | Garage | Maintence | Gas | Notes", justify="center")  


cnt_gar = Text("Home | Help | Maintence | Gas | Notes",justify="center") 
cnt_mat = Text("Home | Help | Garage | Gas | Notes", justify="center") 
cnt_gas = Text("Home | Help | Garage | Maintence | Notes" , justify="center") 
cnt_nts = Text("Home | Help | Garage | Maintence | Gas", justify="center") 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#----------------------------|Exit|---------------------------------------------
#Exit command forced fomating 
exit_line = Text()
exit_line.append("Type", style="bold")
exit_line.append(" exit ", style="bold red")
exit_line.append("or", style="bold")
exit_line.append(" quit ", style="bold red")
exit_line.append("to leave program", style="bold")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#----------------------------|Text fields|--------------------------------------
# Home page info text box
home_info = Text("""Welcome to your vitural garage.
Here you will be able to track maintenance, 
log your gas mileage, create notes about your project cars,
and store all the details about all your cars.


At any point in this program you can type "help" and you will be directed to 
the help page where all your questions will be answered
\nTo navigate to any page reference the Navigation bar to see commands to pages. 
""", justify="center")




# Maintence reminders text box --> will need to be updateable
# Full text fild that i can send vars to then get stingified in panel. 
mr_jobs = Text("Add some maintenance tasks on the Maintenance page", justify="center")



# Help page info text box
help_info = Text.from_ansi("""\033[1mProject Car\033[0m is the ideal tool for car and computer enthusiasts. 
With this CLI (Command line interface) program, you the user will be able to quickly navigate
through the pages with fast one-word commands that you mimic using a terminal. The advantage 
to using the program is speed and simplicity.

\033[1mThings to Note:\033[0m       
When you enter a command, capitalization is not a factor.
For example, to end your session you can enter "EXIT", "exit", "Exit", "eXiT",
or any combination of capital and lowercase letters, and the command will execute. 

The commands listed above are all valid to use on any page. 

Project Car is developed by:
Tyler Knudson Forrest

And is built using \033[1mTyper\033[0m Python library for building CLI tools 
Developed by @tiangolo (Sebastian Ramirez)
https://typer.tiangolo.com/
""", justify="left")


# help_panel= Panel(help_info)

help_command_list = Text.from_ansi(
"""\033[1mExit\033[0m -- Exits this program.  
\033[1mQuit\033[0m -- Same as exit.						   
\033[1mHelp\033[0m -- Takes you to this page.
\033[1mHome\033[0m -- Takes you to the Home page.
""", justify="left")


# NOT YET IN USE
# \033[1mGarage\033[0m -- Takes you to your Garage. 
# \033[1mMaintenance\033[0m -- Takes you to the Maintenance page. 
# \033[1mGas\033[0m -- Takes you to the Gas Mileage tracker page. 
# \033[1mNotes\033[0m -- Take you to the Notes page. 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#----------------------------|Commands|----------------------------------------

# Home page command 
@app.command()
def home():
	clear_screen()
	print(Panel(exit_line))
	print(md_hm_title)
	print(Panel(home_info))
	print(Panel(mr_jobs, title="Maintenance Reminders"))
	print(Panel(cnt_hom, title="Navigation"))


# Help page command 
@app.command()
def help():
	clear_screen()
	print(Panel(exit_line))
	print(md_hlp_title)
	print(Panel(help_command_list))
	print(Panel(help_info))
	print(Panel(cnt_hom, title="Navigation"))



# interactive full prog call 
@app.command()
def procar():
	clear_screen()
	print(Panel(exit_line))
	print(md_hm_title)
	print(Panel(home_info))
	print(Panel(mr_jobs, title="Maintenance Reminders"))
	print(Panel(cnt_hom, title="Navigation"))
	
	while True:
		
		user_input = input("Enter your commands here --> ").strip().lower() 
	
				# exit condition	
		if user_input in ['quit', 'exit']:
			print("Leaving garage") 
			break
		
		elif user_input in commands: 
			commands[user_input]()

		else:
			print("[bold red]Unknown command. Type 'help' for available commands.[/bold red]")


# Command lib, defines commands users can call in the prog
commands = {
	"home": home,
	"help": help,
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Executes the app() as a whole
if __name__ == "__main__":
	app() 
