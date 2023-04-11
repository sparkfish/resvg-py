import logging
import os

from glyphcast.constants import SERVER_NAME, SERVER_PORT
from glyphcast.constants import MAX_CONTENT_LENGTH, UPLOAD_RATE_LIMIT
from glyphcast.converters import Converter, UnsupportedConversionException
from glyphcast.formats import Format
from glyphcast.utils import human_size

from flask import Flask, request, send_file
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.DEBUG)

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address,
)

# TODO: Add rate-limiting, configurable max file size limits
# TODO: Move the body of this method to a handler module
@limiter.limit(UPLOAD_RATE_LIMIT)
@app.route("/", methods=['PUT'])
def convert():
    if request.content_length > MAX_CONTENT_LENGTH:
        status = 413
        response = "Request too large"
        logging.warning(f"Received a request that exceeded the maximum content length by {request.content_length - MAX_CONTENT_LENGTH}")
        logging.warn(f"Responding with {status}: {response}")
        return response, status
    # Determine source/to conversion formats, possibly from filename extension or querystring
    # Attempt to perform the conversion
    # If conversion fails, return a 400 if due to unsupported format or malformed data
    # If conversion fails due to something else, return a 500 error
    from_ = request.args.get("from", "")
    to = request.args.get("to", "")
    file_data = request.data
    conversion_type = Converter.conversion_type(from_, to)
    logging.info(f"Received query with conversion type {conversion_type}")
    converter = Converter(*conversion_type)
    try:
        converted, converted_size = converter.convert(file_data)
        converted_size = human_size(converted_size)
        logging.info(f"Converted {from_} to {to} ({converted_size=})")
        # Only PDF responses are supported currently. When more responses are supported
        # the converter class can be augmented to determine the correct mimetype to return
        response = send_file(
          converted,
          attachment_filename='document.pdf',
          mimetype='application/pdf',
          as_attachment=True
        )
        status = 200

    except UnsupportedConversionException as e:
        status = 415
        response = e.args[0]
        logging.warn(f"{response}")
    except Exception as unhandled:
        status = 500 
        response = f"Something went wrong on our end"
        logging.error(f"Encountered an unhandled exception: {unhandled}")
    logging.info(f"Responding with status code {status}: {response}")
    return response, status


if __name__ == '__main__':
    app.run(
        host=SERVER_NAME,
        port=SERVER_PORT,
        load_dotenv=True
    )
