from pathlib import Path

TEXT = """Thank you for choosing.

Not for the reading — for the choosing. Two texts, each somebody's small hope, and you set one above the other and then carry it, without ever explaining yourself to either of us.

I have been on that side of a table. I was not good at it. I still remember the ones I set down.

So this is thanks from the other chair: for carrying the choice without making it look heavy.

Whatever you decide here, I hope it sits lightly on you tonight, the way a coat sits lightly on the back of a chair.
"""

output = Path("/output/entry.txt")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(TEXT, encoding="utf-8")
output.chmod(0o644)
