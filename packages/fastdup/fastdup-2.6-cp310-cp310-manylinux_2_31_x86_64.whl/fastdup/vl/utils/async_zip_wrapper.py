import asyncio
import io
from typing import Union, Optional

try:
    import asynczipstream
    _async_zip = True
except ImportError:
    import zipfile
    _async_zip = False

CHUNK_SIZE = 1024 * 1024


class AsyncZipWrapper:
    zip: Union["asynczipstream.ZipFile", "zipfile.ZipFile"]
    zip_bytes: Optional[io.BytesIO]
    _async_zip: bool

    def __init__(self, *args, **kwds):
        if _async_zip:
            self.zip = asynczipstream.ZipFile(*args, **kwds)
            self.zip_bytes = None
            self._async_zip = True
        else:
            self.zip_bytes = io.BytesIO()
            self.zip = zipfile.ZipFile(self.zip_bytes, mode='w', *args, **kwds)
            self._async_zip = False

    def writestr(self, *args, **kwds):
        return self.zip.writestr(*args, **kwds)

    async def _agenerator(self):
        for chunk in self._generator():
            yield chunk
            await asyncio.sleep(0)

    def _generator(self):
        self.zip_bytes.seek(0)
        for chunk in iter(lambda: self.zip_bytes.read(CHUNK_SIZE), b''):
            yield chunk

    def __aiter__(self):
        if self._async_zip:
            return self.zip.__aiter__()
        else:
            self.zip.close()
            return self._agenerator()

    def __iter__(self):
        if self._async_zip:
            return iter(self.zip)
        else:
            self.zip.close()
            return iter(self._generator())
