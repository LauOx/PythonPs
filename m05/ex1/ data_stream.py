#!/usr/bin/env python3
# importar esto del futuro porque tengo python 8 y no permite typing.list[]
from __future__ import annotations
from abc import ABC, abstractmethod
import typing

class DataProcessor(ABC):
    pass

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        """"""

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        """"""

    def output(self) -> typing.Tuple[int, str]:
        """"""
        x = self.rank
        i = 0
        while i < len(self.data_stored) and self.data_stored[i] != ",":
            i += 1
        y = self.data_stored[:i]
        self.data_stored = self.data_stored[i + 2:]
        self.remaining -= 1
        self.rank += 1
        out = x, y
        return out


class NumericProcessor(DataProcessor):
    def __init__(self): 
        """"""
        self.data_stored = ""
        self.rank = 0
        self.added = 0
        self.remaining = 0

    def validate(self, data: typing.Any) -> bool:
        """"""
        value = False
        if isinstance(data, (int, float)):
            value = True
            return value
        elif isinstance(data, (list)):
            return all(isinstance(d, (int, float)) for d in data)
        return value

    def ingest(self, data: typing.Union[int, float, list]) -> None:
        """"""
        try:
            if self.validate(data):
                if isinstance(data, (int, float)):
                    self.data_stored += str(data)
                    self.added += 1
                    self.remaining += 1
                elif isinstance(data, list):
                    for d in data:
                        if not self.data_stored:
                            self.data_stored += str(d)
                            self.added += 1
                            self.remaining += 1
                        else:
                            self.data_stored += ", " + str(d)
                            self.added += 1
                            self.remaining += 1
            else:
                raise ValueError("Improper numeric data")
        except ValueError as e:
            print(f" Got exception: {e}")


class TextProcessor(DataProcessor):
    def __init__(self): 
        """"""
        self.data_stored = ""
        self.rank = 0
        self.remaining = 0
        self.added = 0

    def validate(self, data: typing.Any) -> bool:
        """"""
        value = False
        if isinstance(data, (str)):
            value = True
            return value
        elif isinstance(data, (list)):
            return all(isinstance(d, (str)) for d in data)
        return value
    
    def ingest(self, data: typing.Union[str, list]) -> None:
        """"""
        try:
            if self.validate(data):
                if isinstance(data, (str)):
                    self.data_stored += data
                    self.added += 1
                    self.remaining += 1
                elif isinstance(data, list):
                    for d in data:
                        if not self.data_stored:
                            self.data_stored += d
                            self.added += 1
                            self.remaining += 1
                        else:
                            self.data_stored += ", " + d
                            self.added += 1
                            self.remaining += 1
            else:
                raise ValueError("Improper string data")
        except ValueError as e:
            print(f" Got exception: {e}")


class LogProcessor(DataProcessor):
    def __init__(self):
        """"""
        self.data_stored = ""
        self.rank = 0
        self.remaining = 0
        self.added = 0

    def validate(self, data: typing.Any) -> bool:
        """"""
        value = False
        if isinstance(data, (typing.Dict)):
            value = True
            return value
        elif isinstance(data, (list)):
            return all(isinstance(d, (typing.Dict)) for d in data)
        return value
    
    def ingest(self, data: typing.Union[typing.Dict, list]) -> None:
        """"""
        try:
            if self.validate(data):
                if isinstance(data, (typing.Dict)):
                    level = data['log_level']
                    message = data["log_message"]
                    self.data_stored += f"{level}: {message}"
                    self.added += 1
                    self.remaining += 1
                elif isinstance(data, list):
                    i = 0
                    for d in data:
                        if not self.data_stored:
                            level = data[i]['log_level']
                            message = data[i]["log_message"]
                            self.data_stored += f"{level}: {message}"
                            self.added += 1
                            self.remaining += 1
                        else:
                            level = data[i]['log_level']
                            message = data[i]["log_message"]
                            self.data_stored += f", {level}: {message}"
                            self.added += 1
                            self.remaining += 1
                        i += 1
            else:
                raise ValueError("Improper log data")
        except ValueError as e:
            print(f" Got exception: {e}")


class DataStream:
    def __init__(self) -> None:
        self.processors = []


    def register_processor(self, proc: DataProcessor) -> None:
        """"""
        if proc not in self.processors:
            self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        """"""
        for d in stream:
            accepted = False
            for proc in self.processors:
                if proc.validate(d):
                    proc.ingest(d)
                    accepted = True
            if not accepted:
                print("DataStreamError - "
                      f"Can't process element in stream: {d}")
            


    def print_processors_stats(self) -> None:
        """"""
        print("== DataStream statistics ==")
        if len(self.processors) == 0:
                print("No processor found, no data")
                return
        else:
            for proc in self.processors:
                name = type(proc).__name__.replace("Processor", " Processor")
                total = proc.added
                remaining = proc.remaining
                print(f"{name}: total {total} items processed, remaining {remaining} on processor")



def main():
    """"""
    print("=== Code Nexus - Data Stream ===\n")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    first_batch = [
        'Hello world', [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil isconnected'}
            ],
        42,
        ['Hi', 'five']
        ]
    data_stream = DataStream()
    # no processors
    print("Initialize Data Stream...")
    # no data
    data_stream.print_processors_stats()
    # Register 1 processor
    print("\nRegistering Numeric Processor\n")
    data_stream.register_processor(numeric)
    # test with only numeric processor
    print(f"Send first batch of data on stream: {first_batch}")
    data_stream.process_stream(first_batch)
    # stats
    data_stream.print_processors_stats()
    # register other processors
    print("\nRegistering other data processors")
    data_stream.register_processor(text)
    data_stream.register_processor(log)
    print("Send the same batch again")
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()
    # consume data
    print("\nConsume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output()
    data_stream.print_processors_stats()

    


main()


# tengo que hacer al cuenta de remaining cuando se añaden los datos que si no no se suma
