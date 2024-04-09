import os

#Этот скрипт будет сканировать определенную директорию и создавать отчет о всех файлах и поддиректориях в ней.
def generate_directory_report(directory_path, report_file):
    try:
        with open(report_file, 'w') as report:
            report.write(f"Отчет о содержимом директории: {directory_path}\n\n")
            for root, dirs, files in os.walk(directory_path):
                if dirs:
                    report.write("Поддиректории:\n")
                    for d in dirs:
                        report.write(f"- {d}\n")
                    report.write("\n")

                if files:
                    report.write("Файлы:\n")
                    for f in files:
                        report.write(f"- {f}\n")
                    report.write("\n")
        print(f"Отчет успешно создан: {report_file}")
    except Exception as e:
        print("Ошибка при создании отчета:", e)


if __name__ == "__main__":
    directory_to_scan = "C:\\xampp\\htdocs\\easyCRM"
    report_file_path = "directory_report.txt"

    generate_directory_report(directory_to_scan, report_file_path)


