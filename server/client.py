import base64
import requests

from io import BytesIO

def make_request(source_file="sparkfish.svg", from_="svg", to="pdf", to_file="document.pdf"):

    print(f"Converting {source_file} from {from_} to {to}")

    with open(source_file, "rb") as f:
        data = f.read()

    # TODO: Make the URI configurable
    r = requests.put(f"http://localhost:8000?to={to}&from={from_}", data=data)
    print(r.request.headers)
    print(r.headers)

    maybe_converted = r.content

    if maybe_converted and r.status_code < 400:
        with open(to_file, "wb") as f:
            f.write(maybe_converted)
            print(f"Converting {source_file} from {from_} to {to} succeeded: file written to {to_file}")
    else:
        print(f"Converting {source_file} from {from_} to {to} failed with status code {r.status_code} and message: '{r.text}'")


if __name__ == '__main__':
    import timeit
    import statistics
    timer = timeit.Timer(
        'make_request("sparkfish.svg", from_="svg", to="pdf", to_file="testfile-svg.pdf")',
        globals={"make_request": make_request})
    timed = timer.repeat(repeat=10, number=1)
    message = f"""
average: {statistics.mean(timed)}
shortest: {min(timed)}
longest: {max(timed)}
"""
    print(message)

    #from glyphcast.converters import Converter

    #x = Converter()
    
