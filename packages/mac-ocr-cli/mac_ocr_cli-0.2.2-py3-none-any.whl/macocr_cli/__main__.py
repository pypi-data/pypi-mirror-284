import base64
import io

import typer
import uvicorn
from PIL import Image
from fastapi import FastAPI, HTTPException, Depends, Request
from ocrmac import ocrmac
from pydantic import BaseModel
from rich.panel import Panel
from fastapi.responses import JSONResponse

from utils import merge_text_by_line, beautify_ocr_result, console

app = FastAPI()
cli = typer.Typer()

# 全局变量用于存储 token
AUTH_TOKEN = None


# 修改验证函数以使用全局 token
def verify_token(request: Request):
    if AUTH_TOKEN is None:
        # 如果没有设置 token，则跳过验证
        return None
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(
            status_code=401,
            detail="Authorization header missing",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = auth_header
    if token != AUTH_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"code": 500, "message": str(exc), "data": None},
    )


# 定义HTTPException处理器
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.status_code, "message": exc.detail, "data": None},
    )


class ImageBase64(BaseModel):
    image: str


@app.post("/ocr")
async def perform_ocr(image_data: ImageBase64, token: str = Depends(verify_token)):
    image_bytes = base64.b64decode(image_data.image)
    image = Image.open(io.BytesIO(image_bytes))

    annotations = ocrmac.OCR(image, language_preference=["zh-Hans"]).recognize()
    result = merge_text_by_line(annotations)
    beautify_ocr_result(result)
    return {"code": 200, "message": "success", "data": {
        "annotations": annotations,
        "fullText": result
    }}


@cli.command("server")
def start_server(
        port: int = typer.Option(8000, "--port", "-p", help="服务器运行的端口"),
        host: str = typer.Option("0.0.0.0", "--host", "-h", help="服务器运行的主机地址"),
        log_level: str = typer.Option("info", "--log-level", "-l", help="日志级别"),
        token: str = typer.Option(None, "--token", "-t", help="用于认证的 token")
):
    """
    启动具有指定配置的 OCR 服务器。
    """
    global AUTH_TOKEN
    AUTH_TOKEN = token

    start_message = f"正在启动 OCR 服务器，地址：[bold cyan]{host}[/bold cyan]，端口：[bold green]{port}[/bold green]"
    console.print(Panel(start_message, title="mac ocr", expand=False, border_style="bold magenta"))

    uvicorn.run(app, host=host, port=port, log_level=log_level)


if __name__ == '__main__':
    cli()
