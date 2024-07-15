from selenium.webdriver.chrome import options
from pathlib import Path


class Options(options.Options):
    """
    RU: Класс Options предназначен для управления настройками драйвера.
    EN: The Options class is designed to manage the driver settings.
    """
    USER_DATA_DIR_ERROR = "User Data Dir Must be a String or a Path"
    BINARY_LOCATION_ERROR = "Binary Location Must be a String or a Path"

    def __init__(self):
        """
        RU: Инициализирует объект Options и устанавливает общие настройки драйвера.
        EN: Initializes the Options object and sets common driver settings.
        """
        super().__init__()
        # Setup path to chrome.exe
        self._binary_location = Path('C:/Program Files/Google/Chrome/Application/chrome.exe')
        self._user_data_dir = Path.home() / 'AppData/Local/Google/Chrome/User Data'
        self.add_argument(f"--user-data-dir={self.user_data_dir}")

        # Common options
        self.add_argument("--start-maximized")
        self.add_argument("–-disable-translate")
        self.add_argument("-–disable-plugins")

        # Setup undetected options
        self.add_argument("--disable-blink-features=AutomationControlled")
        self.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.add_experimental_option('useAutomationExtension', False)

    def remove_argument(self, argument: str):
        if not isinstance(argument, str):
            raise TypeError('Argument Must be a str.')
        self._arguments = [i for i in self.arguments if argument not in i]

    @property
    def user_data_dir(self) -> str:
        """
        RU: Возвращает текущий каталог пользовательских данных.
        EN: Returns the current user data directory.
        """
        return str(self._user_data_dir)

    @property
    def binary_location(self):
        """
        RU: Возвращает текущее местоположение бинарного файла.
        EN: Returns the current binary location.
        """
        return str(self._binary_location)

    @property
    def headless(self):
        """
        RU: Возвращает значение, указывающее, работает ли драйвер в режиме без головы.
        EN: Returns a value indicating whether the driver is running in headless mode.
        """
        return '--headless=new' in self.arguments

    @binary_location.setter
    def binary_location(self, value):
        """
        RU: Устанавливает местоположение бинарного файла.
        EN: Sets the binary location.
        """
        if not isinstance(value, (str, Path)):
            raise TypeError(self.BINARY_LOCATION_ERROR)
        self._binary_location = Path(value).resolve()

    @user_data_dir.setter
    def user_data_dir(self, value):
        """
        RU: Устанавливает каталог пользовательских данных.
        EN: Sets the user data directory.
        """
        if not isinstance(value, (str, Path)):
            raise TypeError(self.USER_DATA_DIR_ERROR)
        self._user_data_dir = Path(value).resolve()
        self.remove_argument('user-data-dir')
        self.add_argument(f"--user-data-dir={self.user_data_dir}")

    @headless.setter
    def headless(self, value):
        """
        RU: Устанавливает значение, указывающее, должен ли драйвер работать в режиме без головы.
        EN: Sets a value indicating whether the driver should run in headless mode.
        """
        if not isinstance(value, bool):
            raise TypeError('Headless Must be a bool.')
        if value and not self.headless:
            self.add_argument('--headless=new')
        if self.headless and not value:
            self.remove_argument('headless')

    def __repr__(self):
        """
        RU: Возвращает строковое представление объекта Options.
        EN: Returns a string representation of the Options object.
        """
        return f"<Options at 0x{id(self)}: {self.arguments}>"
