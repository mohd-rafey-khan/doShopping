import decimal
import json
from datetime import datetime
from enum import Enum
from uuid import UUID


class CustomEncoder(json.JSONEncoder):
    """
    CustomEncoder for handling datetime, UUID and Decimal issues
    """
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, UUID):
            return str(o)
        if isinstance(o, decimal.Decimal):
            """Decimal to str"""
            return float(o)
        if isinstance(o, Enum):
            """Enum to str"""
            return o.name
        return json.JSONEncoder.default(self, o)


class JsonSerializable:

    @staticmethod
    def format(data) -> dict:
        """
        Format data to JSON serializable support
        @param data: list or dictionary
        @return:
        """
        return json.loads(
            json.dumps(data, cls=CustomEncoder)
        )

    @staticmethod
    def dumps(data) -> str:
        """
        Dump data to JSON string
        @param data:
        @return:
        """
        return json.dumps(data, cls=CustomEncoder)