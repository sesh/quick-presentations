OWASP Top 10

---

A regularly updated list of the *most critical* security risks to web applications

<div class="footnote">
	https://owasp.org/www-project-top-ten/
</div>

---

Open Worldwide Application Security Project (OWASP) is a community-led security project.

The team is made up of security experts from around the world.

<div class="footnote">
	https://owasp.org/
</div>

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

---

<!-- body-class:alt -->

Broken Access Control

---

Any situation where a user can access something that is outside their intended permissions

---

Manipulating URLs, cookies or tokens

---

Missing access controls on unexpected HTTP methods or routes

---

```
/api/getCustomerInformation?id=123129112
```

---

<div data-body-style="background-color: #f8f9fa;">
	<img src="https://media.brntn.me/postie/c1ed47c2.png" alt="Optus logo" />
</div>

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

<div class="footnote">
	Default credentials are really <a href="https://github.com/ihebski/DefaultCreds-cheat-sheet/blob/main/README.md">easy</a> <a href="https://github.com/ihebski/DefaultCreds-cheat-sheet/blob/main/README.md">to</a> <a href="https://github.com/danielmiessler/SecLists/tree/master/Passwords/Default-Credentials">come</a> <a href="https://github.com/ztgrace/changeme/blob/master/README.md">by...</a>
</div>

---

Keys using weak algorithms or low entropy

Accidental key exposure

---

<div data-body-style="background-color: #22272e;">
	<img src="https://media.brntn.me/postie/d03d1497.png" />
</div>


---

<!-- body-class:alt -->

Injection

---

Situations where user supplied data is directly injected into your code

---

Not just SQL!

LDAP, NoSQL, system commands, and ORMs are all targets.

---

<div>
	<img src="https://imgs.xkcd.com/comics/exploits_of_a_mom.png">
</div>

---

<!-- body-class:alt -->

Insecure Design

---

Design and architectural flaws in your system

---

Promotes secure by design and ensures teams understand the security implications of changes

---

<div>
	<img src="https://media.brntn.me/postie/fee937f4.png" />
</div>

---

<!-- body-class:alt -->

Security Misconfiguration

---

Applications that are improperly secured because of a misconfiguration

---

Missed steps in go live or hardening documentation

---

Applications deployed to production with development configurations

---

Features enabled that aren't being used increasing the attack surface area

---

<div>
	<img src="https://media.brntn.me/postie/5f897134.png">
</div>

---

<!-- body-class:alt -->

Vulnerable and Outdated Components

---

Applications using components with known security vulnerabilities

---

Both accidental vulnerabilities and malicious changes apply here

---

Supply chain attacks

---

<div data-body-style="background-color:#fff;">
	<img src="https://media.brntn.me/postie/aa4b3202.png" />
</div>

---

<!-- body-class:alt -->

Identification and Authentication Failures

---

Allowing the wrong user (malicious or not) to authenticate to a system

---

Account enumeration, especially when weak and previously leaked passwords are allowed

---

Misconfiguration of authentication that allows MFA bypass, OAuth scope creep, unverified user registrations, etc..

---

<div>
	<img src="https://media.brntn.me/postie/c52fbfb0.png" />
</div>

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

<div data-body-style="background-color:#fff;">
	<img src="https://media.brntn.me/postie/0891c86a.png" />
</div>

---

<!-- body-class:alt -->

Security Logging and Monitoring Failures

---

Not having enough information to investigate an issue

---

Logging so much information that it becomes toxic waste

<div class="footnote">
	<a href="https://idlewords.com/talks/haunted_by_data.htm">Haunted By Data</a> at Idle Words, <a href="https://www.schneier.com/blog/archives/2016/03/data_is_a_toxic.html">Data is a Toxic Asset</a> by Bruce Schneier.
</div>

---

<div data-body-style="background-color:#fff;">
	<img src="https://media.brntn.me/postie/ea9c46fb.png">
</div>

---


<!-- body-class:alt -->

Server-Side Request Forgery

---

Allowing your server to make requests to a resource provided by a user

---

Making requests that reveal metadata about the service

---

Tricking servers into mining cryptocurrencies

---

```bash
http://google.com:80+&@127.88.23.245:22/#+@google.com:80/
```

<div class="footnote">
	Source: <a href="https://github.com/cujanovic/SSRF-Testing">SSRF-Testing</a> on Github
</div>
---

```bash
http://0/
```

---

<div data-body-style="background-color:#fff;">
	<img src="https://media.brntn.me/postie/82787881.png">
</div>

---

Wrap Up

---

The OWASP Top 10 is a great guide, but is really only the first 10 of 100s of potential issues

---

Think about security early, during the planning and design phase of new work

---

Resources if you want to learn more

- [OWASP](https://owasp.org/) ([Top 10](https://owasp.org/www-project-top-ten/), [Cheat Sheet Series](https://cheatsheetseries.owasp.org/), [Testing Guide](https://owasp.org/www-project-web-security-testing-guide/stable/))
- [Pentester Labs Bootcamp](https://www.pentesterlab.com/bootcamp)
- [PicoCTF](https://www.picoctf.org/)
- [Risky Business](https://risky.biz/)

---

Exposure links

- [Optus breach details](https://verse.systems/blog/post/2022-09-25-optus-breach/)
- [Github RSA key leak](https://github.blog/2023-03-23-we-updated-our-rsa-ssh-host-key/)
- [Exploits of a Mom](https://xkcd.com/327/)
- [Lastpass Security Incidents](https://en.wikipedia.org/wiki/LastPass#Security_incidents)
- [Salesforce public sites](https://krebsonsecurity.com/2023/04/many-public-salesforce-sites-are-leaking-private-data/)
- [node-ipc updated to support Ukraine](https://www.theregister.com/2022/03/18/protestware_javascript_node_ipc/)
- [Have I Been Pwned?](https://haveibeenpwned.com)
- [Solarwinds](https://www.wired.com/story/russia-solarwinds-hack-roundup/) ([non-paywalled link](https://archive.md/3RizK))
- [Latitude breach just got much worse](https://ia.acs.org.au/article/2023/latitude-breach-just-got-much-worse.html)
- [Github SSRF Exploit Chain](http://blog.orange.tw/2017/07/how-i-chained-4-vulnerabilities-on.html)

---

🙏🏻 Thanks!

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
