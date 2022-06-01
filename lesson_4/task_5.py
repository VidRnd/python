import sys
import utils

if __name__ == "__main__":
    args = sys.argv[1:]
    print ( utils.currency_rates ( args[0] ) )