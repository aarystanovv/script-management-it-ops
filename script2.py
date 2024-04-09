import psutil
import datetime

#Мониторит использование ресурсов системы в производственной среде и записывает данные в лог-файл для последующего анализа.
def monitor_system():
    try:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent
        log_entry = f"{current_time}: CPU использование - {cpu_percent}%, Память использование - {memory_percent}%\n"
        with open("system_monitor.txt", "a") as log_file:
            log_file.write(log_entry)

        print("Данные успешно записаны в лог-файл.")
    except Exception as e:
        print("Ошибка при мониторинге системы:", e)


if __name__ == "__main__":
    monitor_system()
