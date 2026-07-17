from abc import ABC, abstractmethod


class BaseCollector(ABC):
    """Base class for all collectors."""

    @abstractmethod
    def fetch(self):
        """Fetch raw data from the source."""
        pass

    @abstractmethod
    def parse(self, raw_data):
        """Convert raw data into a standard format."""
        pass