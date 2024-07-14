# @author Akash Pallath
# This code is licensed under the MIT license (see LICENSE.txt for details).
"""
Definitions of all Exceptions raised by paperfetcher.
"""


class QueryError(Exception):
    """Exception raised when query fails."""
    pass


class SearchError(Exception):
    """Exception raised when search fails."""
    pass


class ContentNegotiationError(Exception):
    """Exception raised when content negotiation fails."""
    pass


class RISParsingError(Exception):
    """Exception raised when RIS parsing fails."""
    pass


class DatasetError(Exception):
    """Exception raised when an incorrect operation is performed on a dataset."""
    pass
