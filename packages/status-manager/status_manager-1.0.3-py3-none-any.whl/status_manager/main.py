from enum import Enum


class StatusType(Enum):
    unchecked = 'unchecked'
    started = 'started'
    finished = 'finished'


class CheckStatus:
    def __ini__(self):
        pass

    def read_status(self, dir_path) -> StatusType:
        with open(dir_path+'/status.txt', 'r') as f:
            data = StatusType.unchecked
            for raw_line in f.readlines():
                line = raw_line.strip()
                if line == '':
                    continue

                for status in StatusType:
                    if line.startswith(status.name):
                        data = status

        return data

    def init_status(self, dir_path):
        with open(dir_path+'/status.txt', 'w') as f:
            f.write(StatusType.unchecked.value)

    def write_status(self, dir_path, status: StatusType):
        with open(dir_path+'/status.txt', 'a') as f:
            f.write('\n')
            f.write(status.value)

    def check(self, dir_path, first_time=True):
        try:
            return self.read_status(dir_path)
        except FileNotFoundError:
            if not first_time:
                raise Exception("Error: There is a problem in "+str(dir_path))
            self.init_status(dir_path)
            return self.check(dir_path, first_time=False)
