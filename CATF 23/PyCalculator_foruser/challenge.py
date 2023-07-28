#!/usr/bin/python3
from rich.console import Console
import re

console = Console()

console.print("[bold white][+] Welcome Again! 😼[/bold white]")

class meow:
    def __init__(self):
        self.name = "Cat"
        self.job = "NetCat"

obj = meow()
blocklist = ['.', '\\', '[', ']', '{', '}',':',
             'import', 'blocklist','globals', 
             'compile' , 'eval','exec','breakpoint',
             'lambda','print', 'flag',"\"","_","+"
             ]


def filter_stuff(cmd):
    return re.sub(r'[^\x00-\x7F]', ' ', cmd)

while True:
    try:
        cmd = console.input('[bold green]>>>[/bold green] ').lower()
        cmd = filter_stuff(cmd)
        if any([b in cmd for b in blocklist]):
            console.print('[bold red][!] Try Harder or Learn Harder!![/bold red]')
        else:
            try:
                print(eval(cmd))
                if obj.age == 1337:
                    flag = open('flag.txt', "r").read().strip()
                    console.print(f"[bold white][👑] Here is the Flag you deserve: [/bold white][bold blue]{flag}[/bold blue]")
            except Exception:
                pass
    except Exception:
        pass