<!-- ===================== -->
<!-- 💜 UNICORN PENTEST UI -->
<!-- ===================== -->

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff00cc,100:6a00ff&height=200&section=header&text=VULNERABLE%20LOGIN%20LAB&fontSize=38&fontColor=ffffff&animation=fadeIn" width="100%"/>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?color=ff00cc&size=18&center=true&vCenter=true&width=600&lines=unicorn-rm+pentest+lab;SQL+Injection+Demo;Web+Security+Practice;Think+like+an+attacker" />
</p>

---

```bash
[ SYSTEM ] unicornOS pentest module v1.0
[ INIT   ] Booting vulnerable environment...
[ LOAD   ] modules: flask, sqlite, auth
[ STATUS ] READY
```
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff00cc,100:333399&height=3"/>
> unicorn-rm

$ role --current
> Cybersecurity Student

$ lab --start
> vulnerable login system loaded
```bash
⚙️ RUN PROJECT
pip install -r requirements.txt
python app.py
> open http://127.0.0.1:5000
> waiting for input...

📸 DEMO
🔐 Login Page
✔ Normal Login
💀 SQL Injection Attack
```
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff00cc,100:333399&height=3"/>

```bash
🧪 ATTACK WALKTHROUGH
[ STEP 1 ] normal login
username: admin
password: admin
> ✔ ACCESS GRANTED
[ STEP 2 ] wrong password
username: admin
password: 123
> ❌ ACCESS DENIED
[ STEP 3 ] SQL injection 💀
username: admin
password: ' OR '1'='1
```
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff00cc,100:333399&height=3"/>

```bash
📜 ATTACK LOG
[LOG] admin/admin        → SUCCESS
[LOG] admin/123          → FAIL
[LOG] admin/' OR '1'='1  → SUCCESS 💀

🛡️ FIX (SECURE MODE)
cursor.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (user, password)
)
[ STATUS ] injection blocked ✔
```
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff00cc,100:333399&height=3"/>


```bash
🧬 SKILLS USED
> SQL Injection
> Flask
> SQLite
> Web Security
> Vulnerability Analysis
> Secure Coding
```

## 🎬 Live Demo ATTACK

### 1️⃣ Login Page
<p align="center">
  <img src="screenshots/login.png" width="600"/>
</p>

---

### 2️⃣ Injection Attack
<p align="center">
  <img src="screenshots/hack.png" width="600"/>
</p>

---

### 3️⃣ Access Granted
<p align="center">
  <img src="screenshots/success.png" width="600"/>
</p>
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff00cc,100:333399&height=3"/>

## 🎬 Live Demo Secure

### 1️⃣ Login Page
<p align="center">
  <img src="screenshots/loginsecure.png" width="600"/>
</p>

---

### 2️⃣ Secure
<p align="center">
  <img src="screenshots/succsec-secure.png" width="600"/>
</p>

---

### 3️⃣ Attack
<p align="center">
  <img src="screenshots/attack.png" width="600"/>
</p>

---

### 3️⃣ SQL Secure
<p align="center">
  <img src="screenshots/failsql.png" width="600"/>
</p>

📦 Installation

```bash
git clone https://github.com/unicorn-rm/vuln-login.git
cd vuln-login

python3 -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate    # Windows

pip install -r requirements.txt
▶️ Run application
python3 app.py
🌐 Default access
http://127.0.0.1:5000

```bash
========================================
[ SYSTEM BREAK ]
========================================
```
---

## 🙌 Thank you for your attention

Thanks for checking out this project!

If you have any feedback, ideas, or suggestions — feel free to reach out or open an issue.

---

👤 Author: unicorn  
🐙 GitHub: https://github.com/unicorn-rm  
🧠 Pseudonym used across projects: unicorn  

---
