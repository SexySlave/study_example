import wikipedia

# Настройка языка Википедии
wikipedia.set_lang("ru")


def search_wikipedia():
    while True:
        # Спрашиваем первоначальный запрос у пользователя
        query = input("\nВведите запрос для поиска на Википедии (или 'выход' для завершения): ").strip()
        if query.lower() == "выход":
            print("Выход из программы.")
            break

        try:
            # Поиск страницы
            page = wikipedia.page(query)
            print(f"\nСтатья найдена: {page.title}\n")
            print("Что вы хотите сделать дальше?")
        except wikipedia.exceptions.DisambiguationError as e:
            print("\nЗапрос неоднозначен. Вот некоторые варианты:")
            for option in e.options[:5]:
                print(f"- {option}")
            continue
        except wikipedia.exceptions.PageError:
            print("\nСтатья не найдена. Попробуйте другой запрос.")
            continue

        while True:
            action = input(
                "\nВыберите действие:\n"
                "1 - Листать параграфы текущей статьи\n"
                "2 - Перейти на одну из связанных страниц\n"
                "3 - Выйти в главное меню\n"
                "Ваш выбор: "
            )

            if action == "1":
                paragraphs = page.content.split("\n\n")  # Делим текст на параграфы
                for i, paragraph in enumerate(paragraphs):
                    print(f"\nПараграф {i + 1}:\n{paragraph}\n")
                    next_action = input("Введите 'далее' для следующего параграфа или 'назад' для возврата: ").strip()
                    if next_action.lower() == "назад":
                        break
                continue

            elif action == "2":
                print("\nСвязанные страницы:")
                for i, link in enumerate(page.links[:10]):  # Ограничиваем до 10 связанных ссылок
                    print(f"{i + 1}. {link}")

                try:
                    link_choice = int(input("\nВведите номер статьи для перехода или '0' для отмены: "))
                    if link_choice == 0:
                        continue
                    new_query = page.links[link_choice - 1]
                    page = wikipedia.page(new_query)
                    print(f"\nПерешли на страницу: {page.title}\n")
                except (ValueError, IndexError):
                    print("Некорректный выбор. Возвращаемся в меню.")
                    continue

            elif action == "3":
                print("\nВозврат в главное меню.")
                break
            else:
                print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    print("Добро пожаловать в консольный поиск по Википедии!")
    search_wikipedia()
