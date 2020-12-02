import logging
import os


def get_logger(file_name, report_to_console=False):

    # create logger, set level and format
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s: lvl: %(levelname)s file: %(filename)s:%(lineno)d funct: %(funcName)s msg: %(message)s')

    # region Additional logging levels

    logging.TestStep = 25  # between WARNING and INFO
    logging.addLevelName(logging.TestStep, 'TestStep')
    setattr(logger, 'TestStep', lambda message, *args: logger._log(logging.TestStep, message, args))

    # add PrepStep level
    logging.PrepStep = 26  # between WARNING and INFO
    logging.addLevelName(logging.PrepStep, 'PrepStep')
    setattr(logger, 'PrepStep', lambda message, *args: logger._log(logging.PrepStep, message, args))

    # add PostStep level
    logging.PostStep = 27  # between WARNING and INFO
    logging.addLevelName(logging.PostStep, 'PostStep')
    setattr(logger, 'PostStep', lambda message, *args: logger._log(logging.PostStep, message, args))

    # endregion Additional logging levels

    # prepare full path for a "file_name".log file based on this module location / Logs/"file_name".log /
    root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    log_outputs_filename = root_path + os.sep + 'Logs' + os.sep + file_name + '.log'

    if not os.path.exists(root_path + os.sep + 'Logs'):
        # Create Log directory
        os.makedirs(root_path + os.sep + 'Logs')

    # report to file "file_name".log
    report_to_file = logging.FileHandler(log_outputs_filename, mode='a')
    report_to_file.setLevel(logging.DEBUG)
    report_to_file.setFormatter(formatter)
    logger.addHandler(report_to_file)

    # report to console if enabled
    if report_to_console:
        report_console = logging.StreamHandler()
        report_console.setLevel(logging.DEBUG)
        report_console.setFormatter(formatter)
        logger.addHandler(report_console)

    logger.debug("Logger initialized")
    return logger


def close_logger(_logger):

    for iterator in range(len(_logger.handlers)):
        _logger.removeHandler(_logger.handlers[0])

