"""Local static preview with byte-range support for seeking in videos."""

import argparse
from email.utils import formatdate
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re


class PreviewHandler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def send_head(self):
        self.remaining = None
        path = Path(self.translate_path(self.path))
        if not path.is_file():
            return super().send_head()
        try:
            file = path.open("rb")
        except OSError:
            self.send_error(404, "File not found")
            return None
        stat = path.stat()
        size = stat.st_size
        start, end = 0, size - 1
        requested_range = self.headers.get("Range")
        # An If-Range validator requires a full response unless it matches.
        modified = formatdate(stat.st_mtime, usegmt=True)
        if self.headers.get("If-Range") not in (None, modified):
            requested_range = None
        if requested_range:
            match = re.fullmatch(r"bytes=(\d*)-(\d*)", requested_range.strip())
            valid = match is not None and any(match.groups()) and size > 0
            if valid:
                first, last = match.groups()
                if first:
                    start = int(first)
                    end = min(int(last), size - 1) if last else size - 1
                else:
                    suffix = int(last)
                    start = max(0, size - suffix)
                valid = 0 <= start <= end < size
            if not valid:
                file.close()
                self.send_response(416)
                self.send_header("Content-Range", f"bytes */{size}")
                self.send_header("Content-Length", "0")
                self.end_headers()
                return None
        self.send_response(206 if requested_range else 200)
        self.send_header("Content-Type", self.guess_type(str(path)))
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Length", str(end - start + 1))
        self.send_header("Last-Modified", modified)
        self.send_header("Cache-Control", "no-cache")
        if requested_range:
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.end_headers()
        file.seek(start)
        self.remaining = end - start + 1
        return file

    def copyfile(self, source, outputfile):
        try:
            if self.remaining is None:
                return super().copyfile(source, outputfile)
            while self.remaining > 0:
                chunk = source.read(min(256 * 1024, self.remaining))
                if not chunk:
                    break
                outputfile.write(chunk)
                self.remaining -= len(chunk)
        except (BrokenPipeError, ConnectionResetError):
            # Browsers cancel the previous stream when seeking elsewhere.
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()
    root = str(Path(__file__).resolve().parent)

    def handler(*args, **kwargs):
        return PreviewHandler(*args, directory=root, **kwargs)

    server = ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    print(f"主页预览：http://127.0.0.1:{args.port}（支持视频拖动跳转）", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
