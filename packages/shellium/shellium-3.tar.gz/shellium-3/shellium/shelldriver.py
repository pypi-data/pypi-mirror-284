import time
from pathlib import Path
from shutil import rmtree
from subprocess import Popen, PIPE

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

from .service import Service
from .options import Options
from .exceptions import *


class ShellElement(WebElement):
    """
    RU: Класс ShellElement - это обертка над WebElement, которая добавляет дополнительные функции для удобства работы.
    EN: The ShellElement class is a wrapper over WebElement that adds additional functions for convenience.
    """

    def __init__(self, parent, _id):
        """
        RU: Инициализирует объект ShellElement.
        EN: Initializes the ShellElement object.
        """
        super().__init__(parent, _id)

    def find_element(self, by=By.ID, value=None) -> 'ShellElement':
        """
        RU: Находит элемент на странице и возвращает его как объект ShellElement.
        EN: Finds an element on the page and returns it as a ShellElement object.
        """
        item = super().find_element(by, value)
        return ShellElement(item.parent, item.id)

    def find_elements(self, by=By.ID, value=None) -> list['ShellElement']:
        """
        RU: Находит элементы на странице и возвращает их как список объектов ShellElement.
        EN: Finds elements on the page and returns them as a list of ShellElement objects.
        """
        items = super().find_elements(by, value)
        return [ShellElement(item.parent, item.id) for item in items]

    def click(self, timeout=0.0, interval=0.1, ignore_errors=False):
        """
        RU: Кликает по элементу, повторяя попытку в течение заданного времени, если произошла ошибка WebDriverException.
        EN: Clicks on the element, retrying for a given time if a WebDriverException error occurs.
        """
        start = time.time()
        current_exception = WebDriverException
        while time.time() - start <= timeout:
            try:
                return super().click()
            except WebDriverException as exception:
                current_exception = exception
                time.sleep(interval)
        if ignore_errors:
            return None
        raise current_exception

    def check_element(self, by=By.ID, value=None, interval=0.1, timeout=0.0):
        """
        RU: Проверяет наличие элемента на странице в течение заданного времени.
        EN: Checks for the presence of an element on the page for a given time.
        """
        start = time.time()
        while time.time() - start <= timeout:
            try:
                return self.find_element(by, value)
            except WebDriverException:
                time.sleep(interval)
        return None

    def check_elements(self, by=By.ID, value=None, interval=0.1, timeout=0.0):
        """
        RU: Проверяет наличие элементов на странице в течение заданного времени.
        EN: Checks for the presence of elements on the page for a given time.
        """
        start_time = time.time()
        while time.time() - start_time <= timeout:
            items = self.find_elements(by, value)
            if items:
                return items
            time.sleep(interval)
        return None

    def send_keys(self, values, timeout=0.25):
        """
        RU: Отправляет последовательность клавиш элементу, делая паузу между каждым символом.
        EN: Sends a sequence of keys to the element, pausing between each character.
        """
        interval = timeout / len(values)
        for value in values:
            super().send_keys(value)
            time.sleep(interval)

    def is_exists(self):
        """
        RU: Проверяет, существует ли элемент на странице.
        EN: Checks if the element exists on the page.
        """
        try:
            return self.is_displayed()
        except WebDriverException:
            return False


class ShellDriver(webdriver.Chrome):
    """
    RU: Класс ShellDriver - это обертка над webdriver.Chrome, которая добавляет
дополнительные функции для удобства работы.
    EN: The ShellDriver class is a wrapper over webdriver.Chrome that adds additional functions for convenience.
    """

    def __init__(self, options: Options = None, service: Service = None):
        """
        RU: Инициализирует объект ShellDriver.
        EN: Initializes the ShellDriver object.
        """
        super().__init__(options=options, service=service)

    def _wrap_value(self, value):
        """
        RU: Оборачивает значение в словарь, если оно является экземпляром ShellElement.
        EN: Wraps the value in a dictionary if it is an instance of ShellElement.
        """
        if isinstance(value, ShellElement):
            return {"element-6066-11e4-a52e-4f735466cecf": value.id}
        return super()._wrap_value(value)

    def _unwrap_value(self, value):
        """
        RU: Распаковывает значение из словаря, если оно является экземпляром ShellElement.
        EN: Unwraps the value from a dictionary if it is an instance of ShellElement.
        """
        if isinstance(value, dict) and "element-6066-11e4-a52e-4f735466cecf" in value:
            return ShellElement(self, (value["element-6066-11e4-a52e-4f735466cecf"]))
        return super()._unwrap_value(value)

    def find_element(self, by=By.ID, value=None) -> ShellElement:
        """
        RU: Находит элемент на странице и возвращает его как объект ShellElement.
        EN: Finds an element on the page and returns it as a ShellElement object.
        """
        item = super().find_element(by, value)
        return ShellElement(item.parent, item.id)

    def find_elements(self, by=By.ID, value=None) -> list[ShellElement]:
        """
        RU: Находит элементы на странице и возвращает их как список объектов ShellElement.
        EN: Finds elements on the page and returns them as a list of ShellElement objects.
        """
        items = super().find_elements(by, value)
        return [ShellElement(item.parent, item.id) for item in items]

    def check_element(self, by=By.ID, value=None, interval=0.1, timeout=0.0):
        """
        RU: Проверяет наличие элемента на странице в течение заданного времени.
        EN: Checks for the presence of an element on the page for a given time.
        """
        start = time.time()
        while time.time() - start <= timeout:
            try:
                return self.find_element(by, value)
            except WebDriverException:
                time.sleep(interval)
        return None

    def check_elements(self, by=By.ID, value=None, interval=0.1, timeout=0.0):
        """
        RU: Проверяет наличие элементов на странице в течение заданного времени.
        EN: Checks for the presence of elements on the page for a given time.
        """
        start_time = time.time()
        while time.time() - start_time <= timeout:
            items = self.find_elements(by, value)
            if items:
                return items
            time.sleep(interval)
        return None

    def scroll_into_view(self, item):
        """
        RU: Прокручивает страницу до элемента.
        EN: Scrolls the page to the element.
        """
        if not isinstance(item, ShellElement):
            raise TypeError('Item Must be a ShellElement.')
        script = 'arguments[0].scrollIntoView({block: "center"});'
        return self.execute_script(script, item)


class Shellium:
    """
    RU: Класс Shellium предназначен для управления драйвером ShellDriver и его настройками.
    EN: The Shellium class is designed to manage the ShellDriver and its settings.
    """

    def __init__(self, executable_path=None, user_data_dir=None, binary_location=None):
        """
        RU: Инициализирует объект Shellium.
        EN: Initializes the Shellium object.
        """
        # Setup options and service
        self._driver: ShellDriver | None = None
        self._options = Options()
        self._service = Service()

        # Setup paths
        if user_data_dir:
            self.options.user_data_dir = user_data_dir
        if binary_location:
            self.options.binary_location = binary_location
        if executable_path:
            self.service.path = executable_path

    @property
    def driver(self):
        """
        RU: Возвращает текущий экземпляр драйвера.
        EN: Returns the current driver instance.
        """
        return self._driver

    @property
    def options(self):
        """
        RU: Возвращает текущие настройки драйвера.
        EN: Returns the current driver settings.
        """
        return self._options

    @property
    def service(self):
        """
        RU: Возвращает текущий сервис драйвера.
        EN: Returns the current driver service.
        """
        return self._service

    def run(self) -> ShellDriver:
        """
        RU: Запускает драйвер, если он еще не запущен.
        EN: Runs the driver if it is not already running.
        """
        if self.driver:
            raise ShellDriverAlreadyRunningError(f'The ShellDriver is already running: {self.driver}.')
        self._driver = ShellDriver(self.options, self.service)
        cmd = "Page.addScriptToEvaluateOnNewDocument"
        args = {'source': "delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;"
                          "delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;"
                          "delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;"
                          "const newProto = navigator.__proto__;"
                          "delete newProto.webdriver;"
                          "navigator.__proto__ = newProto;"}
        self.driver.execute_cdp_cmd(cmd, args)
        return self.driver

    def terminate(self):
        """
        RU: Завершает работу драйвера, если он запущен.
        EN: Terminates the driver if it is running.
        """
        if not self.driver:
            return None
        self.driver.quit()
        self._driver = None

    def build(self):
        """
        RU: Создает новый каталог пользовательских данных, если он еще не существует.
        EN: Creates a new user data directory if it does not already exist.
        """
        if Path(self.options.user_data_dir).exists():
            raise UserDataDirExistsError(f'{self.options.user_data_dir} already exists.')

        process = Popen([self.options.binary_location, '--no-startup-window',
                         f'--user-data-dir={self.options.user_data_dir}'], stdout=PIPE)
        _, error = process.communicate()
        if process.returncode != 0:
            raise UserDataBuildError('Failed to build a User Data Dir.')

    def destroy(self):
        """
        RU: Удаляет каталог пользовательских данных и завершает работу драйвера.
        EN: Deletes the user data directory and terminates the driver.
        """
        self.terminate()
        rmtree(self.options.user_data_dir, ignore_errors=True)
