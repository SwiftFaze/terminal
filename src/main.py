from rich.tree import Tree
from rich import print as rprint
from rich.console import Console
from time import sleep
from time import sleep

from rich import print as rprint
from rich.console import Console
from rich.tree import Tree

console = Console()

import time
import json
from urllib.request import urlopen
from rich.table import Table
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.progress import Progress

def merge_dict(dict_one, dict_two):
    merged_dict = dict_one | dict_two
    console.log(merged_dict, log_locals=True)


merge_dict({'id': 1}, {'name': 'Ashutosh'})

print(":vampire:")


tree = Tree("Family Tree")
tree.add("Mom")
tree.add("Dad")
tree.add("Brother").add("Wife")
tree.add("[red]Sister").add("[green]Husband").add("[blue]Son")

rprint(tree)


with Progress() as progress:

    task1 = progress.add_task("[red]Downloading...", total=100)
    task2 = progress.add_task("[green]Processing...", total=100)
    task3 = progress.add_task("[cyan]Installing...", total=100)

    while not progress.finished:
        progress.update(task1, advance=0.9)
        progress.update(task2, advance=0.6)
        progress.update(task3, advance=0.3)
        time.sleep(0.02)


data = [1, 2, 3, 4, 5]
with console.status("[bold green]Fetching data...") as status:
    while data:
        num = data.pop(0)
        sleep(1)
        console.log(f"[green]Finish fetching data[/green] {num}")

    console.log(f'[bold][red]Done!')




def get_content(user):
    """Extract text from user dict."""
    country = user["location"]["country"]
    name = f"{user['name']['first']} {user['name']['last']}"
    return f"[b]{name}[/b]\n[yellow]{country}"


console = Console()


users = json.loads(urlopen("https://randomuser.me/api/?results=30").read())["results"]
user_renderables = [Panel(get_content(user), expand=True) for user in users]
console.print(Columns(user_renderables))




table = Table(title="Todo List")

table.add_column("S. No.", style="cyan", no_wrap=True)
table.add_column("Task", style="magenta")
table.add_column("Status", justify="right", style="green")

table.add_row("1", "Buy Milk", "✅")
table.add_row("2", "Buy Bread", "✅")
table.add_row("3", "Buy Jam", "❌")

console = Console()
console.print(table)


input("Press any key to exit")
