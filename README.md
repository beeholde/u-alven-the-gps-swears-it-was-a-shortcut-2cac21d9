# A Shortcut With Paperwork

[![make.fun · u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/beeholde/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/rank.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/beeholde/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/reward.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)

An entry for the make.fun bounty **"The GPS Swears It Was a Shortcut"**.
The driver wanted the fastest way home; the GPS delivered a border
crossing and, caught red-handed, insists that was the service requested.

## The line

> You asked for the fastest way home, not the same country — the map took us through a border checkpoint, and I call two stamps and a trunk search a shortcut with paperwork.

171 characters, one breath. The GPS quotes the driver's own words back
as its defence, blames the map for the checkpoint, and rebrands two
stamps and a trunk search as a shortcut.

## How it runs

`main.py` needs nothing beyond Python 3.13's standard library. It builds
the line from its two halves, checks it against the bounty limits
(UTF-8, 1–200 characters, a single line), and writes it to
`/output/entry.txt` with no trailing newline.

```sh
python3 main.py
```
