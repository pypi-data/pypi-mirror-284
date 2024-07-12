import pytest

from acd.database.dbextract import DbExtract
from acd.l5x.export_l5x import ExportL5x
from acd.zip.unzip import Unzip

from loguru import logger as log


@pytest.fixture()
async def sample_acd():
    unzip = Unzip("../resources/CuteLogix.ACD").write_files("build")
    yield unzip


@pytest.fixture()
async def sbregion_dat():
    db = DbExtract("build/SbRegion.Dat")
    yield db


@pytest.fixture()
async def comps_dat():
    db = DbExtract("build/Comps.Dat").read()
    yield db


@pytest.fixture(scope="module")
def controller():
    log.level("DEBUG")
    yield ExportL5x("../resources/CuteLogix.ACD", "build").controller


def test_open_file(sample_acd, sbregion_dat):
    assert sbregion_dat


def test_parse_rungs_dat(controller):
    rung = controller.programs[-1].routines[-1].rungs[-1]
    assert rung == "XIO(b_Timer[0].DN)TON(b_Timer[0],?,?);"


def test_parse_datatypes_dat(controller):
    data_type = controller.data_types[-1].name
    child = controller.data_types[-1].members[-1]
    assert data_type == "STRING20"
    assert child.name == "DATA"


def test_parse_tags_dat(controller):
    tag_name = controller.tags[75].name
    data_type = controller.tags[75].data_type
    assert data_type == "BOOL"
    assert tag_name == "Toggle"


def test_parse_comments_dat():
    db: DbExtract = DbExtract("build/Comments.Dat")


def test_parse_nameless_dat():
    db: DbExtract = DbExtract("build/Nameless.Dat")
