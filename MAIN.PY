# a) Створює файл TF12_1 із символьних рядків різної довжини
def create_file_TF12_1():
    with open("TF12_1.txt", "w") as file:
        lines = [
            "First line of text.\n",
            "Another line.\n",
            "More data here.\n",
            "Random text to fill.\n",
            "Short one.\n"
        ]
        file.writelines(lines)

# б) Читає вміст TF12_1 і записує його у TF12_2 по певній кількості символів на рядок
def process_TF12_1_to_TF12_2():
    with open("TF12_1.txt", "r") as file:
        content = file.read()

    with open("TF12_2.txt", "w") as file:
        line_length = 1
        index = 0
        while index < len(content):
            file.write(content[index:index+line_length] + "\n")
            index += line_length
            line_length = (line_length % 10) + 1  # Щоб повторювався цикл довжин від 1 до 10

# в) Читає вміст TF12_2 і друкує його по рядках
def read_and_print_TF12_2():
    with open("TF12_2.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line, end="")  # end="" щоб уникнути подвійного переносу рядків

create_file_TF12_1()
process_TF12_1_to_TF12_2()
read_and_print_TF12_2()
