
"""
Application Logger
"""

__license__ = "GPL"
__author__ = "Sylvain Meignier"
__copyright__ = "Copyright 2023 Sylvain Meignier, Le Mans Université, LIUM (https://lium.univ-lemans.fr/)"


import logging
import sys
import panel as pn
import numpy as np

#pn.extension(notifications=True)

class NotificationStream():
    """
    A class that represents a notification stream.

    This class is responsible for writing log messages to the notification system.
    It provides methods to send different types of notifications based on the log message level.

    Args:
        duration (int, optional): The duration of the notifications in milliseconds. Defaults to 5000.
    """

    def __init__(self, duration=5000):
        self.duration = duration

    def _extracte_message(self, msg):
        """
        Extracts the relevant part of the log message.

        Args:
            msg (str): The log message.

        Returns:
            str: The extracted log message.
        """
        index = np.max(np.array([msg.find("DEBUG"), msg.find("WARNING"), msg.find("INFO"),
            msg.find("ERROR"), msg.find("CRITICAL")]))
        if index > -1:
            msg = msg[index:]
        if len(msg) > 103:
            msg = msg[:50]+ '...'+msg[-50:]
        return msg
 
    def write(self, msg):
        """
        Writes a log message to the notification system.

        This method processes the log message and sends the appropriate notification based on the log message level.

        Args:
            msg (str): The log message to be sent as a notification.
        """
        if pn.config.notifications and (pn.state.notifications is not None):
            msg = self._extracte_message(msg)
            if msg.find('DEBUG') >= 0:
                pn.state.notifications.send(msg, background='hotpink', icon='<i class="fas fa-bug"></i>')
            elif msg.find('WARNING') >= 0:
                if msg.find('Dropping a patch') >= 0: #can't remove Bokeh message !!!
                    return
                pn.state.notifications.warning(msg, self.duration*2)
            elif msg.find('INFO') >= 0:
                pn.state.notifications.info(msg, self.duration)
            elif msg.find('ERROR') >= 0:
                pn.state.notifications.error(msg, 0)
            elif msg.find('CRITICAL') >= 0:
                pn.state.notifications.send(msg, background='black', icon='<i class="fas fa-burn"></i>')
            else:
                pn.state.notifications.send(msg, background='gray', icon='<i class="fas fa-bolt"></i>')

def add_stream(logger_object, level=logging.INFO, stream=sys.stdout):
    """
    Add a stream handler to the logger object.

    Args:
        logger_object (logging.Logger): The logger object to which the stream handler will be added.
        level (int, optional): The logging level for the stream handler. Defaults to logging.INFO.
        stream (io.TextIOBase, optional): The stream to which the log messages will be written. Defaults to sys.stdout.

    Returns:
        logging.StreamHandler: The added stream handler.

    """
    stream_handler = logging.StreamHandler(stream)
    stream_handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter) # add formatter to ch
    logger_object.addHandler(stream_handler) # add ch to logger
    return stream_handler

GENERAL_LEVEL = logging.INFO
NOTIFICATION_LEVEL = logging.INFO

FORMAT = '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
logging.basicConfig(format=FORMAT, level=GENERAL_LEVEL, force=True)
logger = logging.getLogger()

notification_stream = NotificationStream()
notification_stream_handler = add_stream(logger, level=NOTIFICATION_LEVEL, stream=notification_stream)

