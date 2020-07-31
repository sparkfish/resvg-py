import logging
import os

MAX_CONTENT_LENGTH = os.environ.get('MAX_CONTENT_LENGTH', None)
UPLOAD_RATE_LIMIT = os.environ.get('UPLOAD_RATE_LIMIT', "25 per minute")

if not MAX_CONTENT_LENGTH:
    logging.warn("MAX_CONTENT_LENGTH is unset, so there will be no limits on file upload size")
else:
    MAX_CONTENT_LENGTH = int(MAX_CONTENT_LENGTH)

