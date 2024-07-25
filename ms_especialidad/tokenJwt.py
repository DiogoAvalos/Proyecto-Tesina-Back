import requests
from typing import Callable
from fastapi.routing import APIRoute
from fastapi import Request, Response,HTTPException

class Validacion(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()
        async def custom_route_handler(request: Request) -> Response:
            response: Response = await original_route_handler(request)
            header = request.headers.get('Authorization',None)       
            queryPath = f"?token={header}" if header is not None else ''
            result = requests.get(f"http://seguridad/validacionToken/{queryPath}")
            if result.status_code != 200:
                raise HTTPException(status_code=result.status_code,detail=result.json()['detail'])
            return response
        return custom_route_handler