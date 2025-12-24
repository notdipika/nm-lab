# import pdb

# aList = [1,2,3,4,5]

# pdb.set_trace()

# while(True):
#     aList.pop()
#     print(aList)


# def fact(n):
#     f = 1
#     for i in range (1,n+1):
#         f=f*i
#     return f

# pdb.set_trace()

# fact (5)

# Logging

import logging

logging.basicConfig(level=logging.WARNING,
                    format = "%(asctime)s %(levelname)s %(message)s",
                    filename = "Day5.log",
                    filemode = "a"
                    )

logging.debug("THIS IS A DEBUG VALUE")
logging.info("THIS IS A INFO")
logging.warning("THIS IS A WARNING")
logging.error("THIS IS A ERROR")
logging.critical("THIS IS CRITICAL")