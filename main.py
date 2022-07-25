from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000,
                log_level='info', reload=True)


"""
TOKEN: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjU5MTQ3NTIyLCJpYXQiOjE2NTg1NDI3MjIsInN1YiI6IjEifQ.ElPKogf33x6440VeGeUAJDnkO5-AbVAjQ7vdGyzhgf4
TIPO: BEARER
"""
