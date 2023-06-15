from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)




if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, 
                log_level='info', reload=True)
    




"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjg3NDM4NTEzLCJpYXQiOjE2ODY4MzM3MTMsInN1YiI6IjIifQ.epGQrxmueox00N6Zo2XHovSNQKBMxUH-1eA2i2r4JJw
Tipo: bearer

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjg3NDQwMDEzLCJpYXQiOjE2ODY4MzUyMTMsInN1YiI6IjMifQ.NEJwG1sYdzP-OB_Ka8U4AS_uMHrTSk4qNqJFpOX_KgQ
"""