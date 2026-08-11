# The Nature of Code — pygame Examples

Every example from Daniel Shiffman's [*The Nature of Code*](https://natureofcode.com/),
ported to Python 3.12+ and [pygame-ce](https://github.com/pygame-community/pygame-ce).

<!-- TODO: replace with a colage GIF that shows a few seconds the most exciting programms. -->
![GIF](gif-path.gif)

---

## Why this exists

The book's examples are written in p5.js and Processing. To make it possible for developers more familiar with python, I have translated the examples to [`pygame-ce`](https://github.com/pygame-community/pygame-ce). A community fork of the pygame game engine.

The port uses pygames ecosystem, and solves the problems in a [`pythonic`](https://en.wikipedia.org/wiki/Zen_of_Python#Being_Pythonic) way.


## Quick start

You need Python 3.12+ and `pygame-ce`. The easiest setup uses
[uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
git clone https://github.com/Hohnik/noc-examples-pygame.git
cd noc-examples-pygame
uv sync
```

Then run any example **from the repo root**:

```bash
uv run chapter5/Example_5_11_Flocking/main.py
```

<details>
<summary>Without uv (plain pip)</summary>

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install pygame-ce noise
python chapter5/Example_5_11_Flocking/main.py
```
</details>


## Finding the p5.js original

To compare an example against the book's code, click the example's image or the **pink book** icon beneath it on [natureofcode.com/examples](https://natureofcode.com/examples), then choose *Open in Web Editor*.

The original Processing examples are [here](https://github.com/shiffman/The-Nature-of-Code-Examples), along with [ports to other languages](https://natureofcode.com/resources/#ports-of-code-examples-to-other-languages).


## License

Code is MIT licensed — see [LICENSE](LICENSE).

This is a derivative work of
[The Nature of Code Examples](https://github.com/shiffman/The-Nature-of-Code-Examples)
(MIT, © 2014 Daniel Shiffman). The book's text and illustrations are separately
licensed (CC BY-NC) and are **not** included here.

## Credits

All of the ideas, and the structure of every example, come from Daniel Shiffman's
*The Nature of Code*. If this repo is useful to you,
[buy the book](https://natureofcode.com/) and watch
[The Coding Train](https://www.youtube.com/@TheCodingTrain).
