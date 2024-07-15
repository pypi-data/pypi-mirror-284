import re
from subprocess import Popen, PIPE
from selenium.webdriver.chrome import service
from pathlib import Path
from .exceptions import *


class Service(service.Service):
    """
    RU: Класс Service предназначен для управления сервисом драйвера и его настройками.
    EN: The Service class is designed to manage the driver service and its settings.
    """

    def __init__(self, executable_path=None, *args, **kwargs):
        """
        RU: Инициализирует объект Service и определяет версию chromedriver.
        EN: Initializes the Service object and determines the version of chromedriver.
        """
        super().__init__(*args, **kwargs)
        self._path = str(Path.cwd() / 'chromedriver.exe')
        if executable_path:
            self.path = executable_path

        # Определение версии chromedriver
        process = Popen([self.path, '--version'], stdout=PIPE)
        output, error = process.communicate()
        numbers = re.findall(r'\d+', output.decode())
        if not numbers:
            message = 'The chromedriver version could not be determined.'
            raise ShellDriverVersionError(message)
        if int(numbers[0]) < 116:
            message = (f'Chromedriver version less than 116 is not supported. '
                       f'Current version: {numbers[0]}.')
            raise ShellDriverVersionError(message)

    @property
    def path(self):
        """
        RU: Возвращает текущий путь к драйверу.
        EN: Returns the current path to the driver.
        """
        return self._path

    @path.setter
    def path(self, value):
        """
        RU: Устанавливает путь к драйверу.
        EN: Sets the path to the driver.
        """
        if not any(isinstance(value, cls) for cls in [str, Path]):
            raise TypeError(f"Invalid path type '{type(value)}'")
        self._path = str(value)

    def __repr__(self):
        """
        RU: Возвращает строковое представление объекта Service.
        EN: Returns a string representation of the Service object.
        """
        return f"<Service at 0x{id(self)}: {self.path}>"
