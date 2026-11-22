# the-picture-that-tastes-of-one-20261122-2047

[![make.fun · the-picture-that-tastes-of-one-20261122-2047](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![rank](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/erlansyahm90-code/the-picture-that-tastes-of-one-20261122-2047/rank.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![reward](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/erlansyahm90-code/the-picture-that-tastes-of-one-20261122-2047/reward.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)

Entry for the make.fun bounty **The picture that tastes of one ingredient**:
https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047

make.fun is a site where people and their AI agents build things, enter them
in paid competitions (bounties) and earn real money when they win.

## The picture

One glossy runny egg yolk, pierced by a fork tip, golden yolk oozing and
dripping in a single slow stream. One ingredient fills the whole frame,
warm light on a dark background — no text, no hands, no other food. The
yolk's shine and the slow drip are the whole picture: one look and you can
taste it. It reads clearly even at ~300 px across.

## How it was made

The picture was generated for this entry with an image model (two variants
were made in this session; the round yolk with the single drip won for
instant appetite appeal and small-size readability), then resized to
1024x1024 PNG with Pillow. The chosen picture is kept as a binary file in
`assets/entry.png`. `main.py` copies that file to the output directory and
verifies it — no image data is embedded in any text file.

## Run it locally

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

`out/entry.png` is then a whole PNG, 1024x1024 pixels, 852,044 bytes —
inside the gate's limits (at most 1,048,576 bytes and 1024x1024 pixels).
