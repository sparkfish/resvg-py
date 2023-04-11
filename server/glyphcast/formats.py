"""
The glyphcast.formats module contains the Format enum class which is used to signal the various
file formats that Glyphcast supports, or UNKNOWN if the format is unsupported
"""

from enum import Enum

class Format(Enum):
    PDF = 0
    SVG = 1
    DOCX = 2
    HTML = 3
    UNKNOWN = 4

