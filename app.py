from datetime import datetime

 

print("Python artifact demo")

 

with open("result.txt","w") as file:

  file.write("Hello from GitHub\n")

  file.write("This file is created in Git\n")

  file.write(f"Genaretd Time: {datetime.now()}\n")

  

print ("result.txt file is created successfully")
