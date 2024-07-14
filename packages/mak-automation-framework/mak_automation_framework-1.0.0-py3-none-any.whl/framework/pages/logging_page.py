import logging
from logging.handlers import RotatingFileHandler


class Logger:
    LOG_LEVELS = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    def __init__(self, log_level="INFO", log_file=None,
                 log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', max_bytes=10485760, backup_count=3):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self._get_log_level(log_level))
        formatter = logging.Formatter(log_format)

        # Ensure no duplicate handlers
        if not self.logger.hasHandlers():
            self._add_stream_handler(log_level, formatter)
            if log_file:
                self._add_file_handler(log_level, formatter, log_file, max_bytes, backup_count)

    def _get_log_level(self, level):
        return self.LOG_LEVELS.get(level.upper(), logging.INFO)

    def _add_stream_handler(self, log_level, formatter):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(self._get_log_level(log_level))
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def _add_file_handler(self, log_level, formatter, log_file, max_bytes, backup_count):
        file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        file_handler.setLevel(self._get_log_level(log_level))
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def set_log_level(self, log_level):
        self.logger.setLevel(self._get_log_level(log_level))
        for handler in self.logger.handlers:
            handler.setLevel(self._get_log_level(log_level))

    def log_info(self, message):
        self.logger.info(message)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_critical(self, message):
        self.logger.critical(message)
