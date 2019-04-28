import time

class Stopwatch(object):

    def __init__(self):
        """Initialize a new Stopwatch, but do not start timing."""
        self.start_time = None
        self.elapsed_time = 0

    def start(self):
        """Start timing."""
        self.start_time = time.time()*1000

    def stop(self):
        """Stop timing."""
        if not (self.start_time):
            return
        stop_time = time.time()*1000
        self.elapsed_time += int(round(stop_time - self.start_time))
        self.start_time = None

    def time_elapsed(self):
        if (self.start_time):
            self.stop()
       
        return self.elapsed_time

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0

