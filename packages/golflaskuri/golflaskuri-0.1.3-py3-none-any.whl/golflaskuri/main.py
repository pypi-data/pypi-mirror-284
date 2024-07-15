from dataclasses import dataclass
from importlib.abc import Traversable
import json
from typing import Optional, List
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import jinja2
from pathlib import Path
import pkgutil
from importlib import resources
from . import clubs  # type: ignore


@dataclass
class Player:
    name: str
    hcp: float


@dataclass
class Tee:
    id: str
    name: str
    length: int
    rating_men: float
    slope_men: int


@dataclass
class Course:
    name: str
    tees: List[Tee]
    par: int


def parse_courses(club_name: str, club_data: dict) -> List[Course]:
    courses = []
    for course in club_data:
        tees = [
            Tee(
                t["id"],
                t["name"],
                t["length"],
                t["rating_men"],
                t["slope_men"],
            )
            for t in course["tees"]
        ]
        par = sum([t["hole_par"] for t in course["holes"]])
        name = f"{club_name} - {course['name']}" if course["name"] else club_name
        courses.append(Course(name, tees, par))
        print(f"Added course {name}")
    return courses


def read_courses_from_files(path: Traversable) -> List[Course]:

    courses = []
    for file in path.iterdir():
        with file.open("r") as f:
            course_data = json.load(f)
        courses.extend(parse_courses(file.name.removesuffix(".json"), course_data))
    return courses


def calculate_game_hcps(hcp: float, course: Course) -> List[dict]:
    game_hcps = []
    for tee in course.tees:
        game_hcps.append(
            {
                "tee": tee.name,
                "id": tee.id,
                "length": tee.length,
                "hcp": (((tee.slope_men * hcp) / 113) + tee.rating_men - course.par),
            }
        )
    return sorted(game_hcps, key=lambda t: t["length"])


clubs_dir = resources.files(clubs)
TEMPLATES = Jinja2Templates(
    env=jinja2.Environment(loader=jinja2.PackageLoader(__name__))
)
COURSES = read_courses_from_files(clubs_dir)

DEFAULT_HCPS = {
    "max": 15.8,
    "jesse": 29.4,
    "panu": 29.7,
    "tele": 52.3,
}

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root(
    request: Request,
    max_hcp: Optional[float] = None,
    jesse_hcp: Optional[float] = None,
    panu_hcp: Optional[float] = None,
    tele_hcp: Optional[float] = None,
    course_name: Optional[str] = None,
):
    hcp_query = f"max_hcp={max_hcp or DEFAULT_HCPS['max']}&jesse_hcp={jesse_hcp or DEFAULT_HCPS['jesse']}&panu_hcp={panu_hcp or DEFAULT_HCPS['panu']}&tele_hcp={tele_hcp or DEFAULT_HCPS['tele']}"
    if None in {max_hcp, jesse_hcp, panu_hcp, tele_hcp}:
        return RedirectResponse(url=f"/?{hcp_query}")
    assert (
        max_hcp is not None
        and jesse_hcp is not None
        and panu_hcp is not None
        and tele_hcp is not None
    )
    if course_name is None:
        return TEMPLATES.TemplateResponse(
            request=request,
            name="course_select.html",
            context={
                "courses": COURSES,
            },
        )

    course = next((c for c in COURSES if c.name == course_name), None)
    if course is None:
        return RedirectResponse(url="/?{hcp_query}")
    player_datas = [
        {
            "name": "Max",
            "hcp": max_hcp,
            "game_hcps": calculate_game_hcps(max_hcp, course),
        },
        {
            "name": "Jesse",
            "hcp": jesse_hcp,
            "game_hcps": calculate_game_hcps(jesse_hcp, course),
        },
        {
            "name": "Panu",
            "hcp": panu_hcp,
            "game_hcps": calculate_game_hcps(panu_hcp, course),
        },
        {
            "name": "Tele",
            "hcp": tele_hcp,
            "game_hcps": calculate_game_hcps(tele_hcp, course),
        },
    ]

    return TEMPLATES.TemplateResponse(
        request=request,
        name="handicaps.html",
        context={
            "course": course,
            "players": player_datas,
        },
    )
