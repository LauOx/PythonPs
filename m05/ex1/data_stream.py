#!/usr/bin/env python3
# importar esto del futuro porque tengo python 8 y no permite typing.list[]
from __future__ import annotations
from abc import ABC, abstractmethod
import typing
from typing import Any, List, Tuple, Union, Dict


class DataProcessingError(Exception):
    """Exception for data processor error"""
    pass


class InvalidDataError(DataProcessingError):
    """Raises when invalid data enter a processor"""
    pass


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data_stored: List[str] = []
        self.rank = 0
        self.added = 0
        self.remaining = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validates data, returns True if data can be processed"""

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process data and save it to the list self.data_stored"""

    def output(self) -> Tuple[int, str]:
        """captures rank and data and returns them as tuple"""
        x = self.rank
        y = self.data_stored.pop(0)
        self.remaining -= 1
        self.rank += 1
        out = x, y
        return out


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        """Validates if data can be processed
        (int, float or list of int and/or float)"""
        value = False
        if isinstance(data, (int, float)):
            value = True
            return value
        elif isinstance(data, (list)):
            return all(isinstance(d, (int, float)) for d in data)
        return value

    def ingest(self, data: Union[int, float, list]) -> None:
        """Process data and save it to the list self.data_stored"""
        if not self.validate(data):
            raise InvalidDataError("Improper numeric data")
        if isinstance(data, (int, float)):
            data_to_add = str(data)
            self.data_stored.append(data_to_add)
            self.added += 1
            self.remaining += 1
        elif isinstance(data, list):
            for d in data:
                data_to_add = str(d)
                self.data_stored.append(data_to_add)
                self.added += 1
                self.remaining += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        """Validates if data can be processed(str or list of str)"""
        value = False
        if isinstance(data, (str)):
            value = True
            return value
        elif isinstance(data, (list)):
            return all(isinstance(d, (str)) for d in data)
        return value

    def ingest(self, data: Union[str, list]) -> None:
        """Process data and save it to the list self.data_stored"""
        if not self.validate(data):
            raise InvalidDataError("Improper string data")
        if isinstance(data, (str)):
            data_to_add = data
            self.data_stored.append(data_to_add)
            self.added += 1
            self.remaining += 1
        elif isinstance(data, list):
            for d in data:
                data_to_add = d
                self.data_stored.append(data_to_add)
                self.added += 1
                self.remaining += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        """"""
        super().__init__()

    def validate(self, data: Any) -> bool:
        """Validates if data can be processed (Dict or list of Dict)"""
        value = False
        if isinstance(data, (Dict)):
            value = True
            return value
        elif isinstance(data, (list)):
            return all(isinstance(d, (Dict)) for d in data)
        return value

    def ingest(self, data: Union[Dict, list]) -> None:
        """Process data and save it to the list self.data_stored"""
        if not self.validate(data):
            raise InvalidDataError("Improper log data")
        if isinstance(data, (Dict)):
            level = data['log_level']
            message = data["log_message"]
            data_to_add = f"{level}: {message}"
            self.data_stored.append(data_to_add)
            self.added += 1
            self.remaining += 1
        elif isinstance(data, list):
            for d in data:
                level = d['log_level']
                message = d["log_message"]
                data_to_add = f"{level}: {message}"
                self.data_stored.append(data_to_add)
                self.added += 1
                self.remaining += 1


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """Appends new processor to the list self.processors"""
        if proc not in self.processors:
            self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        """Recieves data and finds the correct DataProcessor to process it"""
        for d in stream:
            accepted = False
            for proc in self.processors:
                if proc.validate(d):
                    proc.ingest(d)
                    accepted = True
                    break
            if not accepted:
                print("DataStreamError - "
                      f"Can't process element in stream: {d}")

    def print_processors_stats(self) -> None:
        """Shows information about DataProcessors status in DataStream"""
        print("== DataStream statistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data")
            return
        else:
            for proc in self.processors:
                name = type(proc).__name__.replace("Processor", " Processor")
                total = proc.added
                remaining = proc.remaining
                print(f"{name}: total {total} items processed, "
                      f"remaining {remaining} on processor")


def main():
    """main function"""
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
    print("\nConsume some elements from the data processors:"
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output()
    data_stream.print_processors_stats()


main()
