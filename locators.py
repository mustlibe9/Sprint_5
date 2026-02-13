from selenium.webdriver.common.by import By

# Кнопка "Войти в аккаунт" на главной странице
LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

# Гиперссылка перехода на форму регистрации
REGISTER_LINK = (By.XPATH, "//a[@href='/register']")

# Поле "Имя" на форме регистрации
NAME_INPUT_REGISTER = (By.XPATH, "//label[text()='Имя']/..//input")

# Поле "Email" на форме регистрации
EMAIL_INPUT_REGISTER = (By.XPATH, "//label[text()='Email']/..//input")

# Поле "Пароль" на форме регистрации
PASSWORD_INPUT_REGISTER = (By.XPATH, "//label[text()='Пароль']/..//input")

# Ошибка некорректного пароля на форме регистрации
PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")

# Кнопка "Зарегистрироваться" на форме регистрации
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

# Поле "Email" на форме входа
EMAIL_INPUT_LOGIN = (By.XPATH, "//label[text()='Email']/..//input")

# Поле "Пароль" на форме входа
PASSWORD_INPUT_LOGIN = (By.XPATH, "//label[text()='Пароль']/..//input")

# Кнопка "Войти" на форме входа
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Гиперссылка перехода в личный кабинет
ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")

# Гиперссылка перехода на форму восстановления пароля
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")

# Гиперссылка перехода на форму входа
LOGIN_LINK = (By.XPATH, "//a[@href='/login']")

# Гиперссылка перехода на форму конструктора по клику на «Конструктор»
CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/parent::a")

# Гиперссылка перехода на форму конструктора по клику на логотип Stellar Burgers
LOGO_LINK = (By.XPATH, "//div[contains(@class,'logo')]//a")

# Кнопка "Выход" в личном кабинете
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

# Кнопка "Оформить заказ" на главной странице после входа в аккаунт
MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

# Гиперссылка перехода на профиль в личном кабинете
ACCOUNT_PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile']")

# Заголовок конструктора
CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")

# Гиперссылка перехода на профиль в личном кабинете
ACCOUNT_PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile']")

# Скролл таб "Булки" в конструкторе
BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")

# Скролл таб "Соусы" в конструкторе
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")

# Скролл таб "Начинки" в конструкторе
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")

# Хедер вариантов булок в конструкторе
BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")

# Хедер вариантов соусов в конструкторе
SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")

# Хедер вариантов начинок в конструкторе
FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")
