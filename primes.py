import sys
sys.path[:] = [path for path in sys.path if path.find('pymultinode') == -1]
sys.path.append('.')
from pymultinode import JobProcessor
import time
def isprime(number):
    for value in xrange(2, number):
        if number % value == 0:
            return False
    return True
def main():
    processor = JobProcessor( 'tweak', 'dd06.ecs.baylor.edu' )
    for number, result in enumerate( processor.imap(isprime, xrange(2, 10000) ) ):
        if result:
            print number+2
if __name__ == '__main__':
    main()
    

