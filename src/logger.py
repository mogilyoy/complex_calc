import os
import datetime
import traceback



class SingletonBase(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBase, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonBase):

    def __init__(self, dir_path:str=os.path.abspath(os.curdir)):
        """
        dir_path - путь к файлу или папке.
        Пример: logs = Logger('./cfg/logs/')
        Путь по умолчанию - текущая директория.
        """
        self._path = dir_path
        self._year = self._current_date().strftime('%Y')
        self._day = self._current_date().strftime('%d')
        self._month = self._current_date().strftime('%m')
        self.latest_message = ''
        
        try:
            assert self._path != '', f'Неверный путь к файлу в инициализации path="{self._path}"'
            assert isinstance(self._path, str), 'Неверный формат пути к директории'
            if not f'log_{self._day}.{self._month}.{self._year[2:]}' in os.listdir(path=self._path):
                with open(self._current_file(), 'w') as f:
                    f.write('')
        except FileNotFoundError:
            os.makedirs(self._path, exist_ok=True)
            with open(self._current_file(), 'w') as f:
                f.write('')

        except AssertionError as e:
            print(traceback.format_exc())
            self._path = os.path.abspath(os.curdir)


    def __str__(self):
        with open(self._current_file(), 'r') as f:
            lines = f.read()
        return lines
    

    def write_log(self, message):
        try:
            assert isinstance(message, str), f'Неверный формат сообщения в логе "{message}": {type(message)}'
        except AssertionError as e:
            print(traceback.format_exc())
            return

        message = f'[{self._current_time()}] {message}\n'
        self.latest_message = message
        with open(self._current_file(), 'a') as f:
            f.write(message)


    def clear_log(self):
        with open(self._current_file(), 'w') as f:
            f.write('')

        
    def get_logs(self) -> list:
        with open(self._current_file(), 'r') as f:
            lines = f.readlines()
            res = []
            for i in lines:
                i = i.replace('\n', '')
                a = i.split(' ')
                res.append((a[0],  ' '.join(a[1:])))
            return res
    

    def get_last_event(self) -> str:
        try:
            assert self.latest_message != '', 'Ещё ничего не было записано'
        except AssertionError as e:
            print(traceback.format_exc())
            return
        return self.latest_message
    

    def get_all_logs(self) -> list:
        dirr = os.listdir(path=self._path)
        try:
            assert dirr, 'Ещё не создано файлов лога'
            dirr.remove('logger.py')
        except AssertionError as e:
            print(traceback.format_exc())
            return
        except ValueError as e:
            pass
        return dirr


    def _change_day(self):
        day = int(self._day)
        self._day = str(day+1)

    
    def _current_file(self):
        return f'{self._path}/log_{self._day}.{self._month}.{self._year[2:]}'


    @staticmethod
    def _current_date():
        return datetime.datetime.now()


    @staticmethod
    def _current_time():
        TIME_FORMAT = '%H:%M:%S'
        return datetime.datetime.now().strftime(TIME_FORMAT)



if __name__ == '__main__':
    log = Logger('./cfg/logs/')
    log.write_log('Отправил запрос github.com')
    log.write_log('<Request 200>, Все гуд')
    log.write_log('KeyError a[i:10] no such key')
    log.write_log('Restarting...')
    print(log)
