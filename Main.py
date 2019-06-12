import random
import logging

def roll():
    x = random.randrange(1, 6)
    y = random.randrange(1, 6)
    print("your dice rolled the numbers: ", x, y)
    return x, y


print("Rolling........")
roll()
input1 = input("Click Y if you want to roll again!!!Else click N [Y/N]: ")

if input1 == 'Y':
    roll()

else:
    print("Happy coding!!!")

# will add logs in example.log
logging.basicConfig(filename="example.log", level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %('
                                                                        'message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# 'application' codex
logging.debug('saving logs for debugging')
logging.info('time when the logs were captured')
logging.warning('Dice have been rolled again!')
logging.error('No error found')
logging.critical('critical message')