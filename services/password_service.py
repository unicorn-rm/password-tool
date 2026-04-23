import re

with open("data/common_passwords.txt", "r", encoding="utf-8") as f:
    COMMON_PASSWORDS = set(line.strip() for line in f)


def analyze_password(password: str):
    score = 0
    feedback = []
    is_common = False

    # 🔴 Dictionary check
    if password.lower() in COMMON_PASSWORDS:
        return {
            "score": 0,
            "level": "weak",
            "is_common": True,
            "feedback": ["This password is in a common password list. Do not use it."]
        }

    length = len(password)

    # Length
    if length >= 12:
        score += 25
    elif length >= 8:
        score += 15
    else:
        feedback.append("Increase password length (12+ recommended)")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 10
    else:
        feedback.append("Add lowercase letters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 10
    else:
        feedback.append("Add uppercase letters")

    # Numbers
    if re.search(r"\d", password):
        score += 15
    else:
        feedback.append("Add numbers")

    # Symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        feedback.append("Add special characters")

    # Variety bonus
    score += min(len(set(password)) * 2, 20)

    score = min(score, 100)

    if score < 40:
        level = "weak"
    elif score < 70:
        level = "medium"
    else:
        level = "strong"

    return {
        "score": score,
        "level": level,
        "is_common": is_common,
        "feedback": feedback
    }