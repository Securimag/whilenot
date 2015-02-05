import sys, time
import threading

nbTotalThread = 0


def recursive():
    global nbTotalThread
    nbTotalThread += 1
    print("NB of open thread: " + str(threading.activeCount()) + " for a total opened of: " + str(nbTotalThread))
    # Some instruction
    # ...
    # ...
    # Start it again
    thread = threading.Thread(target=recursive)
    thread.start()

    # Stop himself
    # Not necessary but cleaner
    sys.exit()
    # is stopped test
    print("Not Stopped")


if __name__ == "__main__":
    recursive()