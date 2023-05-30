OWASP Top 10

---

A regularly update list of the *most critical* security risks to web applications

---

Open Web Application Security Project (OWASP) is a community-led security project.

The team is made up of security experts from around the world.

---

# The 2021 Top 10

1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery

<div class="footnotes">

[OWASP Top Ten](https://owasp.org/www-project-top-ten/)

</div>

---

<!-- body-class:alt -->

Broken Access Control

---

Any situation where a user can access something that is outside their intended access

---

Manipulating URLs, cookies or tokens

---

Missing access controls on unexpected HTTP methods or routes

---

```
/api/getCustomerInformation?id=123129112
```

---

![](https://media.brntn.me/postie/0fac4c83.jpeg)

---

<!-- body-class:alt -->

Cryptographic Failures

---

Bad cryptography that can lead to unexpected data exposure

---

Weak SSL / TLS configurations that allow person in the middle attacks

<div class="footnote">
	Use Mozilla's <a href="https://ssl-config.mozilla.org/">SSL Config Generator</a> and Qualys' <a href="https://www.ssllabs.com/ssltest/">SSL Labs Server Test</a>.
</div>

---

Missing HTTP Strict Transport Security headers that allow HTTP downgrade attacks

<div class="footnote">
	<a href="https://securityheaders.io">SecurityHeaders.io</a> has tests for this and a bunch of others.
</div>

---

The use of default passwords or secrets in applications

---

![](https://media.brntn.me/postie/8c690dc2.png)

<!-- source: https://www.bleepingcomputer.com/news/security/hacker-steals-military-docs-because-someone-didn-t-change-a-default-ftp-password/ -->

---

Default credentials are really <a href="https://github.com/ihebski/DefaultCreds-cheat-sheet/blob/main/README.md">easy</a> <a href="https://github.com/ihebski/DefaultCreds-cheat-sheet/blob/main/README.md">to</a> <a href="https://github.com/danielmiessler/SecLists/tree/master/Passwords/Default-Credentials">come</a> <a href="https://github.com/ztgrace/changeme/blob/master/README.md">by...</a>

---

<!-- body-class:alt -->

Injection

---

Situations where user supplied data is directly injected into your code

---

Not just SQL!

LDAP, NoSQL, system commands, and ORMs are all targets.

---

![](https://media.brntn.me/postie/089015a8.png)

---

<!-- body-class:alt -->

Insecure Design

---

Design and architectural flaws in your system

---

Introduced to promote **secure by design** and ensure teams understand the security implications of changes

---

<!-- body-class:alt -->

Security Misconfiguration

---

Applications that are improperly secured because of a misconfiguration

---

Missing steps in go live or hardening documentation is a common cause

---

Applications deployed to production with development configurations

---

Features enabled that aren't being used that increase the attack surface area

---

<!-- body-class:alt -->

Vulnerable and Outdated Components

---

Applications using components with known security vulnerabilities

---

Both accidental vulnerabilities and malicious changes apply here

<div class="footnote">
	Malicious changes to dependencies have become known a <strong>supply chain attacks</strong>.
</div>

---

<!-- body-class:alt -->

Identification and Authentication Failures

---

Allowing the wrong user (malicious or not) to authenticate to a system

---

Commonly seen as account enumeration, expecially when weak and well-known passwords are used

---

Misconfiguration of authentication that allows MFA bypass, OAuth scope creep, unverified user registrations, etc..

---

<!-- body-class:alt -->

Software and Data Integrity Failures

---

Assuming that the build you just tested is the one that will be deployed

---

Using dependencies from third parties without verifying them

---

Allowing untrusted code into your ecosystem

---

<!-- body-class:alt -->

Security Logging and Monitoring Failures

---

Not having enough information to investigate an issue

---

Logging so much information that it becomes toxic waste

---

<!-- body-class:alt -->

Server-Side Request Forgery

---

Allowing your server to make requests to a resource provided by a user

---

`file:///`

---

Wrap Up

---

The OWASP Top 10 is a great guide, but is really only the first 10 of 100s of potential issues

---

Think about security early, during the planning and design phase of new work

---

Resource is you want to learn more

...

---

<style>
body {
  background-color: #ffd52e;
  color: #000;
}

p:not(:last-of-type) {
	margin-bottom: 1.4em;
}

body.alt {
	background-color: #020302;
	color: #fff;
}
</style>
