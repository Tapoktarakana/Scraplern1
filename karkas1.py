# Импортируем необходимые модули
from selenium import webdriver  # Для управления браузером
from selenium.webdriver.common.by import By  # Для поиска элементов на странице

# --- ШАГ 1. Настройка браузера ---
# Указываем путь к веб-драйверу (например, ChromeDriver)
# Замените 'path_to_chromedriver' на путь к вашему драйверу
# Сейчас уже вроде этого не требуется поэтому просто пропиши: driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

# --- ШАГ 2. Вставляем API-ключ, если он нужен ---
# Если для доступа к странице или API нужно указать ключ,
# его можно вставить в заголовки или параметры URL.
api_key = "ВАШ_API_КЛЮЧ"  # Сюда вставляем ваш API-ключ

# Например, если API-ключ передается через URL, формируем URL:
url = f"https://example.com/page?api_key={api_key}"

# Если API-ключ нужен для заголовков, вот пример:
headers = {
    "Authorization": f"Bearer {api_key}"  # Стандартный формат передачи ключа
}

# --- ШАГ 3. Открываем нужную страницу ---
# В данном примере просто открываем URL с API-ключом в параметрах
driver.get(url)

# --- ШАГ 4. Поиск элемента h1 ---
try:
    # Ищем первый элемент h1 на странице
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    # Выводим текст элемента
    print("Найден элемент h1 с текстом:", h1_element.text)
except Exception as e:
    # Обрабатываем ошибку, если элемент не найден
    print("Элемент h1 не найден:", e)

# --- ШАГ 5. Завершаем работу браузера ---
driver.quit()
