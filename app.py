from datetime import datetime

print("Python artifact demo")

with open("result.txt", "w") as file:
    file.write("I love you Prajakta\n")
    file.write("Lavkar firayala jau.\n")
    file.write(f"Udya ya time la: {datetime.now()}\n")

print("result.txt file is created successfully")
