import argparse
import shutil
import time
from pathlib import Path


def parse_argv():
    parser = argparse.ArgumentParser(description="Копіює файли в папку")
    parser.add_argument("-s", "--source", type=Path, required=True, help="Папка з файлами")
    parser.add_argument("-o", "--output", type=Path, default=Path("output"), help="Папка для копіювання")
    return parser.parse_args()


def recursive_copy(source: Path, output: Path):
    try:
        print("Програма сортує........")
        for element in source.iterdir():
            if element.is_dir():
                print(f"Створення папки для директорії: {element}")
                recursive_copy(element, output)
            else:
                file_extension = element.suffix[1:]
                folder = output / file_extension if file_extension else output / "others"
                folder.mkdir(exist_ok=True, parents=True)
                shutil.copy(element, folder / element.name)
    except Exception as e:
        print(f"Помилка при копіюванні файлу {element}: {e}")


def main():
    print("Привіт!")
    args = parse_argv()

    print(f"Початок роботи. Копіювання файлів з {args.source} в {args.output}")

    start_time = time.time()

    args.output.mkdir(exist_ok=True, parents=True)
    recursive_copy(args.source, args.output)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Копіювання завершено за {elapsed_time:.2f} секунд. Дякую за використання програми!")


if __name__ == "__main__":
    main()
