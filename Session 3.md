# Secure Coding Fix-It Exercise

## 👥 Activity Title: Fix the Bug! - Secure Coding in Your Language

### 🕒 Duration: 25-30 minutes

### 🎯 Goal: Identify and fix insecure code snippets in a language you're comfortable with.

## Instructions

1. Form pairs or small groups.
2. Choose one or more of the code examples below based on your preferred language.
3. Identify what's insecure about each snippet.
4. Write a secure version of the code.
5. Prepare a 1-minute explanation of your fix.

## Example 1: PHP - SQL Injection

```php
$unsafe_email = $_POST['email']; $sql = "SELECT * FROM users WHERE email = '$unsafe_email'"; $result = mysqli_query($conn, $sql);
```

### 🛠️ Task: Rewrite this code using prepared statements.

## Example 2: JavaScript - DOM-Based XSS

```js
const comment = location.hash.substring(1);
document.getElementById("output").innerHTML = comment;
```

### 🛠️ Task: Prevent script injection from the URL fragment.

## Example 3: Python (Flask) - Missing Input Validation

```python
@app.route('/user/<username>')
    def profile(username):
        return f"Welcome, {username}"
```

### 🛠️ Task: Properly escape or validate the username before displaying.

## Example 4: Java - Insecure Role Check

```java
if (request.getParameter("role").equals("admin")) {
        giveAdminAccess();
}
```

### 🛠️ Task: Use Spring Security role checks instead of trusting parameters.

## ✅ Bonus Challenge: For each example, list the secure coding principle violated (e.g., input validation, least privilege, output encoding).
