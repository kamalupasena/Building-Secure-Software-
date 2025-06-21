import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("CREATE TABLE users (username TEXT, password TEXT)")
c.execute("INSERT INTO users VALUES ('admin', 'admin123')")

# Vulnerable login
username = input("Username: ")
password = input("Password: ")

# Vulnerable to SQL injection
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"




print("Query:", query)

c.execute(query)
# SQL injection safe Query
# c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

result = c.fetchone()

if result:
    print("✅ Logged in!")
else:
    print("❌ Access denied.")