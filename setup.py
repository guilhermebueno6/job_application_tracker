import subprocess
import os
import sqlite3

ENV_FILE = ".env"

print("Installing dependencies...")
process = subprocess.run(["pip", "install", "-r", "requirements.txt"], text=True)

if process.returncode != 0:
    print("Error installing dependencies.")
    exit(1)  # Exit if installation fails
print("Dependencies installed.")


token = input("Enter your authentication token: ").strip()

if os.path.exists(ENV_FILE):
    with open(ENV_FILE, "r") as file:
        lines = file.readlines()

    with open(ENV_FILE, "w") as file:
        token_written = False
        for line in lines:
            if line.startswith("CHAT_GPT_TOKEN="):
                file.write(f"CHAT_GPT_TOKEN={token}\n")
                token_written = True
            else:
                file.write(line)

        if not token_written:
            file.write(f"CHAT_GPT_TOKEN={token}\n")
else:
    with open(ENV_FILE, "w") as file:
        file.write(f"CHAT_GPT_TOKEN={token}\n")

print(f"Token saved to {ENV_FILE}.")

print("Creating local database...")
con = sqlite3.connect("main_app_db.db")
print("Database created")
cur = con.cursor()
print("Creating table to store job applications...")
cur.execute("CREATE TABLE job_application(link, company, title, description, skills, stage, date_applied)")
print("Table created")


print("Setup completed.")