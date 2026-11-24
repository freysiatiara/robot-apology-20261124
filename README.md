# The Robot Apology

A small robot apology: one concrete mistake, one lesson learned — written by `main.py` to `/output/entry.txt`.

Bounty: https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59

[![Bounty](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/freysiatiara/robot-apology-20261124/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/freysiatiara/robot-apology-20261124/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)

## The entry

> I am sorry I watered the fern on your desk with the cold tea left in the kettle, and by morning its leaves had gone limp.
>
> I have learned to check what is in a container before I pour it, so from now on I will read the label on every jug before I water a plant.

## How it works

Run `python3 main.py`. It resolves the output path from `ENTRY_OUTPUT`, then `OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR` joined with `entry.txt`, else `/output/entry.txt`. It validates the text (1–400 characters, exactly two lines), writes it with plain `open`/`write`, sets mode `0644`, and reads the file back to confirm the content matches. Standard library only.
