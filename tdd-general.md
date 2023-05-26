# Test Driven Development

---

- I'll introduce TDD and some of its guidelines
- We will run through a quick example together
- Complete a TDD Kata in pairs
- We'll have a quick chat about TDD

---

So, what is TDD?

---

> Test-Driven Development (TDD) is a technique for building software that guides software development by writing tests

_- Martin Fowler_

<div class="footnote">
  https://martinfowler.com/bliki/TestDrivenDevelopment.html
</div>

---

1. Write a failing test
2. Write code to make it pass
3. Refactor to ensure clean code

---

🔴💚🔁

---

Refactor both your code and tests

---

Rules, you say?

---

> ## The Three Laws of TDD

_- Robert Martin_

<div class="footnote">
  http://www.butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd
</div>

---

1. You are not allowed to write any production code unless it is to make a failing unit test pass.

---

2. You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.

---

3. You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

---

Generalisation

---

Avoid writing code for the "general" case when you don't have to

---

```javascript
describe('isPrime', () => {
  it('should be prime', () => {
    expect(isPrime(3)).toBe(true);
  });
});
```

---

```javascript
const isPrime = (n) => {
  return n == 3;
};
```

---

Triangulation

---

Use a second assertion to drive a safer creation of the generic version

<div class="footnote">
  https://dmitripavlutin.com/triangulation-test-driven-development/
</div>

---

![](https://media.brntn.me/postie/e3dbd8f4.png)

<div class="footnote">
  Image: CC-BY (Brenton Cleeland)
</div>

---

```javascript
describe('isPrime', () => {
  it('should return true when prime', () => {
    expect(isPrime(3)).toBe(true);
    expect(isPrime(7)).toBe(true);
  });
});
```

---

```javascript
const isPrime = (n) => {
  for (let i = 2; i <= n/2; i++) {
    if (n % i === 0) {
      return;
    }
  }
  return true;
};
```

---

Refactor

---

```javascript
const isPrime = (n) => {
  let max = Math.sqrt(n);
  for (let i = 2; i <= max; i++) {
    if (n % i === 0) {
      return;
    }
  }
  return true;
};
```

---

Once you're happy with the code, think about and test negative cases

---

```javascript
describe('isPrime', () => {
  it('should return false when not prime', () => {
    expect(isPrime(22)).toBe(false);
  });
});
```

---

```javascript
const isPrime = (n) => {
  let max = Math.sqrt(n);
  for (let i = 2; i <= max; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
};
```

---

Think about the edge cases

---

```javascript
describe('isPrime', () => {
  it('should return false when passed one', () => {
    expect(isPrime(1)).toBe(false);
  });
});
```

---

```javascript
const isPrime = (n) => {
  let max = Math.sqrt(n);
  for (let i = 2; i <= max; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return n > 1;
};
```

<div class="footnote">
  https://stackoverflow.com/a/40200710
</div>

---

Awesome-sauce 🍅

---

Let's recap

---

- Write a test
- Write code
- Refactor to make things 👍🏻

---

Only write the code required to make your test pass

---

Think about edge cases

---

TDD is a discipline and takes practice

---

Try using TDD on your next side project

---

Thank you 🙏🏻

<style>
body {
  background-color: #ffd52e;
  color: #000;
}
</style>
