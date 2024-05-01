class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.log_file = open("log.txt", "a")

    def log(self, message):
        self.log_file.write(message + "\n")
        self.log_file.flush()

    def close(self):
        self.log_file.close()


class LoggerFactory:
    def create_logger(self):
        return Logger()


# Usage
if __name__ == "__main__":
    logger_factory = LoggerFactory()

    logger1 = logger_factory.create_logger()
    logger2 = logger_factory.create_logger()

    print(logger1)
    print(logger2)

    logger1.log("This is a log message from logger1")
    logger2.log("This is a log message from logger2")

    logger1.close()
    logger2.close()
