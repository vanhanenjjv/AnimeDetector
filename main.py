import logging
from os import getenv
from time import perf_counter

from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn

from anime import detect_anime_from, UnsupportedFormatError


app = FastAPI()


@app.post('/')
async def detect_anime(file: UploadFile = File(...)):
    try:
        begin = perf_counter()
        result = await detect_anime_from(file)
        end = perf_counter()
    except UnsupportedFormatError:
        logging.info(f'Unsupported content-type: "{file.content_type}"')
        raise HTTPException(status_code=415)

    return {
        'is_anime': result,
        'time_elapsed': end - begin
    }


if __name__ == '__main__':
    uvicorn.run(
        app,
        host=getenv('HOST') or 'localhost',
        port=int(getenv('PORT') or 8080)
    )
