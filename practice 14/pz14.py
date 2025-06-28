import re

def extract_1857_block(input_file, output_file):

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        pattern = re.compile(
            r'(1857\s*год?.*?)(?=(?:\n\d{4}\s*год|\Z))',
            re.DOTALL | re.IGNORECASE
        )

        match = pattern.search(content)

        if match:
            block_1857 = match.group(1).strip()


            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(block_1857)
            print(f"Блок за 1857 год успешно сохранен в файл {output_file}")
        else:
            print("Блок за 1857 год не найден в исходном файле.")

    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    input_filename = "Dostoevsky.txt"
    output_filename = "Dostoevsky_1857.txt"


    extract_1857_block(input_filename, output_filename)
