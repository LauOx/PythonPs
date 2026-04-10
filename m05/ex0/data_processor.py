!#/usr/bin/env python3
from abc import ABC, abstractmethod
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


def main():
    """main function"""
    print("=== Code Nexus - Data Processor ===\n")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    bad_tester = [42, "Hello"]
    n_tester = [1, 2, 3, 4, 5]
    foo = "foo"
    t_tester = ['Hello', 'Nexus', 'World']
    l_tester = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    # numeric processor
    print("Testing Numeric Processor...")
    # validate data
    for d in bad_tester:
        print(f" Trying to validate input '{d}':", numeric.validate(d))
    # ingest not validated data
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest(foo)
    except InvalidDataError as e:
        print(f" Got exception: {e}")
    # processing (ingest and output) validated data
    print(f" Processing data: {n_tester}")
    print(" Extracting 3 values...")
    numeric.ingest(n_tester)
    for _ in range(3):
        n_out_x, n_out_y = numeric.output()
        print(f" Numeric value {n_out_x}: {n_out_y}")
    # text processor
    print("\nTesting Text Processor...")
    print(" Trying to validate input '42':", text.validate(bad_tester[0]))
    print(f" Processing data: {t_tester}")
    try:
        text.ingest(t_tester)
    except InvalidDataError as e:
        print(f"Got exception: {e}")
    print(" Extracting 1 value...")
    text.output
    t_out_x, t_out_y = text.output()
    print(f" Text value {t_out_x}: {t_out_y}")
    # log processor
    print("\nTesting Log Processor...")
    print(" Trying to validate input 'Hello':", log.validate(bad_tester[1]))
    print(f" Processing data: {l_tester}")
    try:
        log.ingest(l_tester)
    except InvalidDataError as e:
        print(f"Got exception: {e}")
    print(" Extracting 2 values...")
    for _ in range(2):
        l_out_x, l_out_y = log.output()
        print(f" Log entry: {l_out_x}: {l_out_y}")


main()
