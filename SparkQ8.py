def sanitize_email(raw_input: str) -> str:
    cleaned = raw_input.strip().lower()
    return cleaned if cleaned and cleaned.count("@") == 1 else "Invalid Email"
email = input("Enter email: ")
print(f'"{sanitize_email(email)}"')
