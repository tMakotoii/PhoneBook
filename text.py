main_menu = ['Главное меню',
             'Открыть тел. справ.',
             'Сохранить тел. справ.',
             'Показать контакты',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход',]

choice_main_menu = f'Выберите пункт меню ({1}-{len(main_menu)-1}):'

choice_main_menu_error = 'Нет такого варианта'

phone_book_opened_successful = 'Телефонная книга успешно открыта'
phone_book_saved_successful = 'Телефонная книга успешно сохранена'

empty_phone_book_error = 'Телефонная книга пуста или не открыта'

input_new_contact = ['Введите имя контакта: ',
                     'Введите номер контакта: ',
                     'Введите комментарий контакта: ',]

input_search_word = 'Введите слово для поиска: '
input_search_word_for_edit = 'Введите слово для поиска, который хотите изменить: '
input_search_word_for_delete = 'Введите слово для поиска, который хотите удалить: '
input_id_for_edit = 'Введите ID контакты, который хотите изменить: '
input_id_for_delete = 'Введите ID контакты, который хотите удалить: '

no_changes = 'Или ENTER, чтобы оставить без изменений'

edit_contact = [f'Введите новое имя ({no_changes}): ',
                f'Введите новый телефон ({no_changes}): ',
                f'Введите новый комментарий ({no_changes}): ']

def new_contact_added_successful(name: str) -> str:
    return f'Контакт "{name}" успешно добавлен!'

def find_contact_no_result(word: str) -> str:
    return f'контакты содержащие "{word}" не найдены!'

def edit_contact_successful(name) -> str:
    return f'Контакт "{name}" успешно изменён!'

def delete_contact_successful(name) -> str:
    return f'Контакт "{name}" успешно удалён!'