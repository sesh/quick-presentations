Build quick presentations from markdown files.

---

Usage:

```
pipenv run python bbig.py <markdown-file>
```

Build all markdown files with:

```
pipenv run python bbig.py *.md
```

---

Under the hood this really just combines a bunch of bigger utilities:

- [big](https://github.com/tmcw/big/) to power the presentation
- [mistune](https://mistune.lepture.com/en/latest/) for Markdown parsing
- [highlight.js](https://highlightjs.org/) for syntax highlighting
- [Twemoji](https://twemoji.twitter.com/) to ensure emoji are consistent and scalable
- [thttp](https://github.com/sesh/thttp) as a lightweight HTTP client

---

The Markdown files in this repository are presentations.

Processed examples:

- [This README](https://sesh.github.io/quick-presentations/README.html)
- [Lighting TDD Introduction](https://sesh.github.io/quick-presentations/tdd-general.html)
- [Estimation Challenge](https://sesh.github.io/quick-presentations/pragprog-challenges.html)

---

Licence

- Code: MIT
- Presentations: CC-BY-SA
