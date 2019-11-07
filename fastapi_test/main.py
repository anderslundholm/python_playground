from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    test1 = 'value1'
    test2 = 'value2'
    test3 = 'value3'


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}


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
