from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from core.generatePassword import PasswordGeneratorSevice

import uvicorn

app = FastAPI()


class Pw(BaseModel):
    l: int | None = Field(default=8)
    upp: bool | None = Field(default=False)
    low: bool | None = Field(default=False)
    num: bool | None = Field(default=False)
    sym: bool | None = Field(default=False)


@app.get("/")
async def home():
    return "pipo"

@app.get("/gfr")
async def random_length_password_with_all_characters() -> str:
    return PasswordGeneratorSevice.generate_random_length_password_with_all_characters()

@app.post("/pw")
async def pw(pw: Pw = Body()) -> str:
    return PasswordGeneratorSevice.generate(pw.l,pw.upp,pw.low,pw.num,pw.sym)

@app.post("/rl")
async def pwrandomLength(pw: Pw = Body()) -> str:
    return PasswordGeneratorSevice.generate_random_length_password(pw.upp,pw.low,pw.num,pw.sym)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8008)