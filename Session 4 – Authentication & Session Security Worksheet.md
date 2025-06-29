# 🛡️ Secure Coding Worksheet - Session 4: Authentication, Authorization & Session Security

**Duration**: 20-25 minutes  
**Format**: Small group or pair-based review  
**Objective**: Identify vulnerabilities in real-world authentication and session handling code and suggest secure alternatives.

---

## 🔍 Instructions

1. Review each code snippet carefully.
2. Discuss with your group:
   - What's wrong with the code?
   - How could an attacker exploit it?
   - How would you fix it?
3. Write your secure version of the code.
4. Bonus: Identify which security principles are violated (e.g., Least Privilege, Secure Session Management, MFA).

---

## ❌ Example 1: Plain-Text Password Storage (PHP)

```php
$password = $_POST['password'];
file_put_contents("users.txt", $password);
```

**🛠️ Task**:  
- What's the risk here?
- Rewrite the code to use secure password hashing (e.g., bcrypt).

---

## ❌ Example 2: JWT with Insecure Algorithm (alg: none)

```json
{
  "header": {
    "alg": "none"
  },
  "payload": {
    "user": "admin"
  },
  "signature": ""
}
```

**🛠️ Task**:  
- What does `alg: none` mean?
- What is the correct way to use JWTs securely?

---

## ❌ Example 3: Session Token in URL

```
https://example.com/dashboard?sessionid=abc123
```

**🛠️ Task**:  
- What's the issue with putting session tokens in URLs?
- How should sessions be handled securely?

---

## ❌ Example 4: No RBAC Enforcement (Flask)

```python
@app.route('/admin')
def admin_panel():
    return "Welcome, Admin!"
```

**🛠️ Task**:  
- How could unauthorized users access this?
- Add a proper role check using Flask-Login or Flask-Security.

---

## ❌ Example 5: Login Endpoint with No Rate Limiting (Flask)

```python
@app.route('/login', methods=['POST'])
def login():
    ...
```

**🛠️ Task**:  
- What type of attack is this vulnerable to?
- Add basic rate-limiting to protect the login endpoint.

---

## ✅ Bonus Challenge:

Write down:
- 3 signs of a **secure authentication** system.
- 3 common **session handling mistakes** you've seen or made.

---
