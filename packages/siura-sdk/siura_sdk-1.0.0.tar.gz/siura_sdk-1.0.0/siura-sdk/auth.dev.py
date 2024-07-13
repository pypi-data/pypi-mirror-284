import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from auth import Auth, ISignIn, ISignUp

sdk = Auth("http://localhost:8000")

token = os.getenv("TOKEN", "")

instance = ISignUp(
    email="njavilas2015@gmail.com",
    password="Abc123%1",
    phone="5492615450939",
    username="njavilas"
)

async def save(token: str):
    output = Path("/home/sarys/projects/siura/package/sdk/.env")
    data = f"TOKEN={token}"
    output.write_text(data, encoding='utf-8')

async def sign_in(method: ISignIn['method']):
    payload = await sdk.sign_in({
        "value": getattr(instance, method),
        "method": method,
        "password": instance.password
    })
    await save(payload)

async def sign_up():
    payload = await sdk.sign_up(instance)
    await save(payload)

async def active_account():
    sdk.set_token(token)
    await sdk.verify_email({"code": "683084"})
    await sdk.verify_phone({"code": "961352"})
    payload = await sdk.active_account({})
    print(payload)

async def main(step: str):
    try:
        if step == 'sign_in':
            await sign_in('username')
        elif step == 'sign_up':
            await sign_up()
        elif step == 'active_account':
            await active_account()
    except Exception as error:
        print({"error": str(error)})

if __name__ == "__main__":
    import asyncio
    asyncio.run(main('sign_in'))
