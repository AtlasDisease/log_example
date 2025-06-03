# --- Imports --- #

import logging as logger
from pathlib import Path


# --- Logging Setup --- #

path = Path(".").resolve()
logger.basicConfig(filename=f"{path.name}.log",
                filemode="w",
                datefmt="%Y-%m-%d %H:%M:%S",
                format='[%(asctime)s %(name)s] (%(filename)s) - %(levelname)s: %(message)s',
                level=logger.DEBUG)
log = logger.getLogger(__name__)

log.debug("Finish logging setup.",)

# --- Main Def --- #

def main():
    log.info("Hello World!")
    log.warning("TestWarning")
    log.error("TestError")
    log.critical("TestCritical")


# --- Main --- #

if __name__ == "__main__":
    main()
