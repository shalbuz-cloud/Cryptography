from cryptography.fernet import Fernet

KEY_FILENAME = 'crypto.key'


# Создаем ключ и сохраняем его в файл
def write_key():
    key = Fernet.generate_key()
    with open(KEY_FILENAME, 'wb') as key_file:
        key_file.write(key)


# Загружаем ключ из файла
def load_key():
    return open(KEY_FILENAME, 'rb').read()


# Зашифруем и запишем файл
def encrypt(filename, key):
    f = Fernet(key)
    # Прочитать все данные файла
    with open(filename, 'rb') as file:
        file_data = file.read()
    # Зашифровать данные
    encrypt_data = f.encrypt(file_data)
    # Запистаь зашифрованный файл
    with open(filename, 'wb') as file:
        file.write(encrypt_data)


# Расшифрока и запись файла
def decrypt(filename, key):
    f = Fernet(key)
    # Считываем зашифрованные данные
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    # Расшифровываем данные
    decrypted_data = f.decrypt(encrypted_data)
    # Записываем оригинальный файл
    with open(filename, 'wb') as file:
        file.write(decrypted_data)


def main():
    write_key()
    key = load_key()
    file = 'path_to_file'
    encrypt(file, key)
    # decrypt(file, key)


if __name__ == '__main__':
    main()
