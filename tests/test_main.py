import sys
from hangman import main
from threading import Thread
from Queue import Queue, Empty
from subprocess import Popen, PIPE
from time import sleep


class NBSR:

    def __init__(self, stream):
        '''
        stream: the stream to read from.
                Usually a process' stdout or stderr.
        '''

        self._s = stream
        self._q = Queue()

        def _populateQueue(stream, queue):
            '''
            Collect lines from 'stream' and put them in 'quque'.
            '''

            while True:
                line = stream.readline()
                if line:
                    queue.put(line)
                else:
                    raise UnexpectedEndOfStream

        self._t = Thread(target = _populateQueue,
                args = (self._s, self._q))
        self._t.daemon = True
        self._t.start() #start collecting lines from the stream

    def readline(self, timeout = None):
        try:
            return self._q.get(block = timeout is not None,
                    timeout = timeout)
        except Empty:
            return None

class UnexpectedEndOfStream(Exception): pass



def test_main():
    with open('dictionary.dat', 'w') as file_to_write:
        file_to_write.write('kakashka\n')
    p = Popen(['main'],
        stdin = PIPE, stdout = PIPE, stderr = PIPE, shell = False)
    nbsr = NBSR(p.stdout)
    output = nbsr.readline(0.1)
    assert output != None
    #with open('file.tmp', 'r') as file_output:
    #    data = file_output.read().split('\n')
    #assert data[0][-1] == '*'
    #assert data[1] == 'Guess a letter:'
