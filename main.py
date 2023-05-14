from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def get_icd_codes():
    icd1 = {
        "code": "A01.4",
        "diagnosis": "Paratyphoid",
        "billable":
        "(effective 10/1/2015)"
    }
    icd2 = {
        "code": "A02.9",
        "diagnosis": "typhimurium",
        "billable":
        "(effective 10/1/2015)"
    }
    return {"icd1": icd1, "icd2": icd2}

