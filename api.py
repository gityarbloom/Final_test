from fastapi import FastAPI, HTTPException, Request, UploadFile, File
from pydantic import BaseModel
import sqlite3
import os
from datetime import datetime
import uvicorn
import csv
from oop_objects import *
import io
import pandas as pd


app = FastAPI(title="Soldier deployment", version="1.0.0")

@app.post("/assignWithCsv")
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()
    decoded_contents = contents.decode("utf-8")
    csv_reader = csv.DictReader(io.StringIO(decoded_contents))
    data = list(csv_reader)
    for obj in data:
        obj = Soldier(obj.id, obj.first_name, obj.last_name, obj.gender, obj.state, obj.distans)


