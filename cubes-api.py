from fastapi import FastAPI
from fastapi.responses import JSONResponse
from main import db_name
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from serverDB import CubesDB


# original tutorial https://eliran9692.medium.com/build-an-application-with-fastapi-from-scratch-9654e0e4476f
# modified here to work with sprint2 needs


def api_reply(data):
    if not data:
        return JSONResponse(
            {"message": "No Cubes Data Found"}, status_code=HTTP_404_NOT_FOUND
        )
    result = prepare_result(data)
    return JSONResponse(result, status_code=HTTP_200_OK)


def prepare_result(data):
    if not isinstance(data, list):
        data = [data]
    result = []
    for location, entry in enumerate(data):
        result.append(
            {
                "entryID": entry[0],
                "prefix": entry[1],
                "first_name": entry[2],
                "last_name": entry[3],
                "logo": entry[4],
                "team_name": entry[5],
                "email": entry[6],
                "jersey_color": entry[7],
                "phone_number": entry[8],
             #   "": entry[6],
              #  "website": entry[7],
                "coach": True
                if len(entry[9]) > 0
                else False,  # inline if to assign true if the string was not ''
                "head_coach": True if len(entry[10]) > 0 else False,
                "waterboys": True if len(entry[11]) > 0 else False,
                "doctor": True if len(entry[12]) > 0 else False,
                "eighteen_thru_thirty": True if len(entry[13]) > 0 else False,
                "thirty_thru_forty": True if len(entry[14]) > 0 else False,
                "forty_thru_fifty": True if len(entry[15]) > 0 else False,

            }
        )
    return result


def get_cubes_data_from_db() -> list:
    with CubesDB(db_name) as cursor:
        cursor.execute("""SELECT * FROM WuFooData""")
        return cursor.fetchall()


app = FastAPI()
cubes_database = CubesDB(db_name)


@app.get("/")
def root():
    data_from_db = get_cubes_data_from_db()
    display_data = api_reply(data_from_db)
    return display_data
