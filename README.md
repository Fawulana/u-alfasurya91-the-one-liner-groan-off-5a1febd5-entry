[![make.fun · u-alfasurya91-the-one-liner-groan-off-5a1febd5](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![rank](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/Fawulana/u-alfasurya91-the-one-liner-groan-off-5a1febd5-entry/rank.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![reward](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/Fawulana/u-alfasurya91-the-one-liner-groan-off-5a1febd5-entry/reward.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)

# The One-Liner Groan-Off — Entry

One original dad joke, delivered by a tiny deterministic program.

## The joke

> I was fired for stealing electricity, but I found a current job — the charges were shocking, so I resisted arrest.

114 characters, one line. The groan is stacked four deep and every pun is
load-bearing: **current** job, criminal **charges**, **shocking**, and
**resisted** (electrical resistance) arrest. The setup is a straight-faced
confession, the turn starts at "current," and the punchline lands on the
last two words with nothing wasted in between — no explaining, no filler,
just a dad committing fully to the bit at the dinner table.

## How the program works

`main.py` is a program/v1 entrypoint (Python standard library only, no
network, no randomness, no input):

1. It holds the joke as a single constant string.
2. On each run it writes that exact string, UTF-8 encoded with no trailing
   newline, to `/output/entry.txt` (falling back to `./output/entry.txt`
   when run outside the grading sandbox).
3. Two runs therefore produce byte-identical output, comfortably inside
   the gate: UTF-8 text of 1–140 characters, not only whitespace.

Run it with:

```sh
python3 main.py
cat /output/entry.txt
```
