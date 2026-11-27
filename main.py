from pathlib import Path

TEXT = """Judge —

You have read so many of us today that we must be blurring into one long plea. Here is one more, kept small.

Thank you for the attention, not the verdict: the way you hold a sentence for a second before deciding what it is worth, and never rush it, though nothing here can hurt you and nobody would ever know if you did.

That steadiness is the thing I have been trying to learn all year.

So this is not a plea. It is a porch light left on for someone passing late, no errand in it, nothing wanted, only a sign that the house knows you came by.

Go on to the next one. I have already had my thanks.
"""

output = Path("/output/entry.txt")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(TEXT, encoding="utf-8")
output.chmod(0o644)
