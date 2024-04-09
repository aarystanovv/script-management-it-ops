import subprocess
import sys
#Этот скрипт выполняет обновление программного обеспечения на компьютерах в производственной среде

def update_software():
    try:
        print("Проверка обновлений ПО...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        print("ПО успешно обновлено.")
    except subprocess.CalledProcessError as e:
        print("Ошибка при обновлении ПО:", e)
        sys.exit(1)

if __name__ == "__main__":
    update_software()
