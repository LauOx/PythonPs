#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Union, Dict

class DataProcessor(ABC):
    pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """"""

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """"""

    def output(self) -> Tuple[int, str]:
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

    def validate(self, data: Any) -> bool:
        """"""
        value = False
        if isinstance(data, (int, float)):
            value = True
            return value
        elif isinstance(data, (list)):
            return all(isinstance(d, (int, float)) for d in data)
        return value

    def ingest(self, data: Union[int, float, list]) -> None:
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

    def validate(self, data: Any) -> bool:
        """"""
        value = False
        if isinstance(data, (str)):
            value = True
            return value
        elif isinstance(data, (list)):
            return all(isinstance(d, (str)) for d in data)
        return value
    
    def ingest(self, data: Union[str, list]) -> None:
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

    def validate(self, data: Any) -> bool:
        """"""
        value = False
        if isinstance(data, (Dict)):
            value = True
            return value
        elif isinstance(data, (list)):
            return all(isinstance(d, (Dict)) for d in data)
        return value
    
    def ingest(self, data: Union[Dict, list]) -> None:
        """"""
        try:
            if self.validate(data):
                if isinstance(data, (Dict)):
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


def main():
    """"""
    print("=== Code Nexus - Data Processor ===\n")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    bad_tester = [42, "Hello"]
    n_good_tester = [1, 2, 3, 4, 5]
    foo = "foo"
    t_tester = ['Hello', 'Nexus', 'World']
    l_tester = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    # numeric processor
    print("Testing Numeric Processor...")
    for d in bad_tester:
        print(f" Trying to validate '{d}':", numeric.validate(d))
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest(foo)
    except ValueError as e:
        print(e)
    print(f" Processing data: {n_good_tester}")
    print(" Extracting 3 values...")
    numeric.ingest(n_good_tester)
    for _ in range(3):
        n_out_x, n_out_y = numeric.output()
        print(f" Numeric value {n_out_x}: {n_out_y}")
    # text processor
    print("\nTesting Text Processor...")
    print(f" Trying to validate '42':", text.validate(bad_tester[0]))
    print(f" Processing data: {t_tester}")
    text.ingest(t_tester)
    print(" Extracting 1 value...")
    text.output
    t_out_x, t_out_y = text.output()
    print(f" Text value {t_out_x}: {t_out_y}")
    # log processor
    print("\nTesting Log Processor...")
    print(f" Trying to validate 'Hello':", log.validate(bad_tester[1]))
    print(f" Processing data: {l_tester}")
    log.ingest(l_tester)
    print(" Extracting 2 values...")
    for _ in range(2):
        l_out_x, l_out_y = log.output()
        print(f" Log entry: {l_out_x}: {l_out_y}")


main()
