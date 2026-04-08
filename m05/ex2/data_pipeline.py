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


class ExportPlugin(typing.Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """"""
        pass


class ExportCSV(ExportPlugin):

    def process_output(self, data: List[Tuple[int, str]]) -> None:
        """Saves data in CSV format"""
        print("CSV Output:")
        info_csv = [value for _, value in data]
        final_csv = ",".join(info_csv)
        print(final_csv)


class ExportJSON(ExportPlugin):

    def process_output(self, data: List[Tuple[int, str]]) -> None:
        """Saves data in JSON format"""
        print("JSON Output:")
        info_json = [f'"item_{rank}": "{value}"' for rank, value in data]
        final_json = "{" + ", ".join(info_json) + "}"
        print(final_json)


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """
        Extracts a specified number of items from each processor
        and exports them via a plugin.
        """
        for proc in self.processors:
            pipeline = []
            for _ in range(nb):
                if proc.data_stored:
                    save_tuple = proc.output()
                    pipeline.append(save_tuple)
            if pipeline:
                plugin.process_output(pipeline)


def main():
    """main function"""
    print("=== Code Nexus - Data Stream ===\n")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    plug_csv = ExportCSV()
    plug_json = ExportJSON()
    data_stream = DataStream()
    first_batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil isconnected'}
            ],
        42,
        ['Hi', 'five']
        ]
    second_batch = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR',
             'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'}
            ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
        ]
    # no processors
    print("Initialize Data Stream...\n")
    # no data
    data_stream.print_processors_stats()
    print("\nRegistering Processors\n")
    data_stream.register_processor(numeric)
    data_stream.register_processor(text)
    data_stream.register_processor(log)
    print(f"Send first batch of data on stream: {first_batch}\n")
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()
    # send to csv plugin
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, plug_csv)
    print()
    # result after process
    data_stream.print_processors_stats()
    # second batch
    print(f"\nSend another batch of data on stream: {second_batch}")
    data_stream.process_stream(second_batch)
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, plug_json)
    # result after process
    print()
    data_stream.print_processors_stats()


main()
