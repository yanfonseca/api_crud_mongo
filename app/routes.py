from sanic import Blueprint
from sanic.request import Request
from sanic.response import json, HTTPResponse
from api.app import helpers
from api.app.schemas import Add, Delete, Update

database_bp = Blueprint('database', "/database")

@database_bp.route('/add', methods=["POST"])
async def add(request: Request) -> json:
    json_schema = Add().load(request.json)
    # _id = request.json.get("id")
    print(json_schema)
    await helpers.add(json_schema)
    return json("added")

@database_bp.route('/search', methods=["GET"])
async def search(request: Request) -> json:
    ret = await helpers.search(request.json)
    return json(ret)


@database_bp.route('/delete', methods=["DELETE"])
async def delete(request: Request) -> json:
    json_schema = Delete().load(request.json)
    await helpers.delete(json_schema.get("id"))
    return json("deleted")

@database_bp.route('/delete/<id:int>', methods=["DELETE"])
async def delete(request: Request, id) -> json:
    await helpers.delete(id)
    return json("deleted")


@database_bp.route('/update', methods=["POST"])
async def delete(request: Request) -> json:
    json_schema = Update().load(request.json)
    ret = await helpers.update(json_schema.get("query"), json_schema.get("changes"))
    return json(ret)

@database_bp.route('/', methods=["GET"])
async def add(request: Request) -> json:
    return HTTPResponse(body="<div>OI</div>")