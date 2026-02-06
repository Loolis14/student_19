#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria."""
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        pass


class SensorStream(stream_id):
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria."""
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        pass


class TransactionStream(stream_id):

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria."""
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        pass


class EventStream(stream_id):

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria."""
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        pass


class StreamProcessor():
    pass
