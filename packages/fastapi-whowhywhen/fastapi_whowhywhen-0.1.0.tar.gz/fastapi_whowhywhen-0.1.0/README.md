# fastapi-whowhywhen

WhoWhyWhen middleware for FastAPI. Create a WhoWhyWhen account at https://whowhywhen.com/ and get your API key.

## Installation

```bash
pip install fastapi-whowhywhen
```

## Usage
```python
from fastapi import FastAPI
from fastapi_whowhywhen import WhoWhyWhenMiddleware

app = FastAPI()

app.add_middleware(
    WhoWhyWhenMiddleware,
    api_key="YOUR_API_KEY"
)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
```
