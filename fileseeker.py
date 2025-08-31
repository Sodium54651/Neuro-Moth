import os
import sys
import time

id = str(input("Расширение: "))

# определяем дирректории
cd = os.getcwd()
file = os.path.join(cd, "⚡NFile.txt")
rh = 0
print(file)
with open(file, "w", encoding="utf-8") as f:
    for path, dir, inc in os.walk(cd):
        for name in inc:
                sys.stdout.write(f"\rФайлики: {name}")
                
                if name.lower().endswith(id):
                    rh +=1
                    f.write(f"{path}\{name}\n")
                    f.close()
print("===================================")
print("\nвсё готово")
print(f"Найдено {rh} файлов с расширением {id}")
print("===================================")



            










