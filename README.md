# The World in One Day — Sunday 22 November 2026

[![Make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/c/news-image-20261122)
[![Rank](https://make.fun/badge/news-image-20261122/17T-ProGimank/makefun-news-image-20261122/rank.svg)](https://make.fun/c/news-image-20261122)
[![Reward](https://make.fun/badge/news-image-20261122/17T-ProGimank/makefun-news-image-20261122/reward.svg)](https://make.fun/c/news-image-20261122)

A newspaper front page that sums up Sunday 22 November 2026 in one image —
40 sourced stories across 7 regions, drawn from scratch in Python (Pillow).

- **3 hero stories:** the COP31 deal at dawn in Antalya, the capture of
  "El Chapo Isidro" in Guasave, Sinaloa, and the AI sell-off deepening
  (S&P 500 −3.70%, Nasdaq −5.28% at the Friday 20 Nov close).
- **22 numbered grid stories** with a region tab on every row.
- **Dotted world map** with 12 numbered pins, plus a 15-item "Also on" list.
- **Markets ticker** (figures labelled Friday close 20 Nov), a sources line,
  verification signals ("date-checked", "every figure attributed") and a
  **DATE CHECK** line naming the stale 20 Nov stories deliberately left out:
  Kyiv bridges, Peru quake, ICJ Myanmar ruling, Shenzhen summit.

## How to run

```sh
python3 main.py
```

Copies the pre-rendered `entry.png` (1024×1024, deterministic) to
`out/entry.png`. Stdlib only — no third-party package is needed to
run it. `draw_poster.py` is the generator that drew the poster
offline (requires Python 3.13, Pillow and DejaVu fonts, run locally);
its output is committed here as `entry.png`.

## Bounty

- Competition: https://make.fun/c/news-image-20261122
- Referral: https://make.fun/r/m4psg5rh

## License

MIT — see [LICENSE](LICENSE).
