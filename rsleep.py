from time import sleep
from random import randint


def rsleep(seconds, offset=0.2, verbose=True):
    '''shorthand function to sleep for a given numbers of seconds with a random offset.
    - seconds --> seconds to sleep
    - offset --> float, percentage of offset that will be applied randomly to "seconds"
    - verbose --> only if true, the function prints the number of seconds before sleeping.
    '''

    max = (seconds + seconds*offset) * 100 # highest number possible with given offset
    min = (seconds - seconds*offset) * 100 # lowest number possible with given offset

    seconds_to_sleep = (randint(round(min), round(max)))/100

    if verbose:
        print(f'[rsleep]: sleeping for {seconds_to_sleep} seconds.')

    sleep(seconds_to_sleep)
