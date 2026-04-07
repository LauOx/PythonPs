#!/usr/bin/env python3
from abc import ABC, abstractmethod
import typing

class ExportPlugin(typing.Protocol):
    pass

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """"""
        pass

class ExportCSV(ExportPlugin):
    pass

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """"""
        print("CSV Output:")
        info_csv = [value for rank, value in data]
        final_csv = ",".join(info_csv)
        print(final_csv)

class ExportJSON(ExportPlugin):
    pass

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """"""
        print("JSON Output:")
        info_json = [f'"item_{rank}": "{value}"' for rank, value in data] 
        final_json = "[" + ", ".join(info_json) + "]"
        print(final_json)


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
                    if not self.data_stored:
                        self.data_stored += str(data)
                        self.added += 1
                        self.remaining += 1
                    else:
                        self.data_stored += ", " + str(data)
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
                    if not self.data_stored:
                        self.data_stored += data
                        self.added += 1
                        self.remaining += 1
                    else:
                        self.data_stored += ", " + data
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
                    if not self.data_stored:
                        level = data['log_level']
                        message = data["log_message"]
                        self.data_stored += f"{level}: {message}"
                        self.added += 1
                        self.remaining += 1
                    else:
                        level = data['log_level']
                        message = data["log_message"]
                        self.data_stored += f", {level}: {message}"
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
                print(f"{name}: total {total} items processed, "
                      f"remaining {remaining} on processor")
    
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """"""
        for proc in self.processors:
            pipeline = []
            count = 0
            while count < nb and proc.data_stored != "":
                save_tuple = proc.output()
                pipeline.append(save_tuple)
                count += 1
            if pipeline:
                plugin.process_output(pipeline)



def main():
    """"""
    print("=== Code Nexus - Data Stream ===\n")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    plug_csv = ExportCSV()
    plug_json = ExportJSON()
    data_stream = DataStream()
    first_batch = [
        'Hello world', [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil isconnected'}
            ],
        42,
        ['Hi', 'five']
        ]
    second_batch = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}
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
