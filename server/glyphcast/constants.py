"""
The constants module initializes configuration parameters and sets defaults if parameters are unset
"""

import logging
import os

from dotenv import load_dotenv
load_dotenv()

SERVER_NAME = os.environ.get('SERVER_NAME', 'localhost')
SERVER_PORT = os.environ.get('SERVER_PORT', 5000)

MAX_CONTENT_LENGTH = os.environ.get('MAX_CONTENT_LENGTH', None)
UPLOAD_RATE_LIMIT = os.environ.get('UPLOAD_RATE_LIMIT', "25 per minute")

if not MAX_CONTENT_LENGTH:
    logging.warning("MAX_CONTENT_LENGTH is unset, so there will be no limits on file upload size")
else:
    MAX_CONTENT_LENGTH = int(MAX_CONTENT_LENGTH)

UNOCONV_PATH = os.environ.get('UNOCONV_PATH', '/usr/bin/unoconv')
UNOCONV_PYTHON_PATH = os.environ.get('UNOCONV_PYTHON_PATH', '/usr/bin/python3')

# Hardcode WeasyPrint since we install it as a dependency
WEASYPRINT_PATH = "weasyprint"
