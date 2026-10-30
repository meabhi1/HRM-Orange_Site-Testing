import logging
import os


class Loggen:

    def logger():

        os.makedirs("..\\Logs",exist_ok=True)

        logging.basicConfig(
            filename=".\\Logs\\automtionLogs.log",
            format='%(asctime)s : %(levelname)s : %(message)s',   # Fixed format specifiers
            datefmt='%Y-%m-%d %H:%M:%S',                           # Optional: Standardized time layout
                                       # Sets baseline logging visibility
            force=True                                             # Overwrites any prior basicConfig initializations

        )

        logg=logging.getLogger()
        logg.setLevel(logging.INFO)

        return logg