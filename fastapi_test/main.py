from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    test1 = 'value1'
    test2 = 'value2'
    test3 = 'value3'


app = FastAPI()

fake_items_db = [{"item_name": "Foo"},
                 {"item_name": "Bar"},
                 {"item_name": "Baz"}]


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    """ Return slice of list with args:
    http://127.0.0.1:8000/items/?skip=1&limit=2
    """
    return fake_items_db[skip:skip + limit]


@app.get('/items/{item_id}')
async def read_item_id(item_id: int, q: str = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long "
             "description"}
        )
    return item


@app.get('/model/{model_name}')
async def get_mode(model_name: ModelName):
    if model_name == ModelName.test1:
        return {'model_name': model_name,
                'message': 'First!'}
    if model_name.value == 'value2':
        return {'model_name': model_name,
                'message': 'The second value.'}
    return {'model_name': model_name,
            'message': 'The leftovers.'}


@app.get('/file/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long "
             "description"}
        )
    return item


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    """ Required parameters:
    http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
    """
    item = {"item_id": item_id, "needy": needy}
    return item
