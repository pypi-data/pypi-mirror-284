import pytest
import json
from pytest import skip

_pcode1 = "PYTESTCUSTOMOUTPUTSCODE5567PCU_"
_pcode2 = "_PYTESTCUSTOMOUTPUTSCODE5568PCU_"
_pcode3 = "_PYTESTCUSTOMOUTPUTSCODE5569PCU"
_attrcode = "_PCOCODE5568PCU_"
_status = _attrcode+"status"
_message = _attrcode+"message"

msg = ""

def attach(message):
    if type(message) != str:raise TypeError("message must be string")
    global msg
    msg = message

def c_assert(status, message=""):
    if type(status) != str or type(message) != str:raise TypeError("status and message must both be strings")
    global msg
    msg = message
    skip(_pcode1+status+_pcode2)

def pytest_addoption(parser):
    group = parser.getgroup('custom_outputs')
    group.addoption(
        '--custom_output',
        action='store',
        dest='custom_output_loc',
        default='pytest_custom_outputs.json',
        help='Select the custom output file to use.'
    )

def pytest_sessionstart(session):
    global exception_dict
    session.config.custom_output_valid = True
    col = session.config.getoption('custom_output_loc')
    try:
        f = open(col)
        data = json.load(f)
    except:
        session.config.custom_output_valid = False
    if session.config.custom_output_valid:
        jfile = data["custom_outputs"]
        for name in jfile:
            if jfile[name]["desc"] == "failed":
                jfile[name]["desc"] = "_failed"
            if jfile[name]["desc"] == "passed":
                jfile[name]["desc"] = "_passed"
        session.config.custom_output = jfile

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    report = (yield).get_result()
    global msg
    message = msg
    setattr(item, _status, "")
    setattr(item, _message, message)
    msg = ""
    if report.passed:
        setattr(item, _status, "passed")
    if report.failed:
        setattr(item, _status, "failed")
        try:fmsg = call.excinfo.value.args[0].split("\n")[0]
        except:fmsg = msg
        setattr(item, _message, fmsg)
    if report.skipped and call.excinfo.typename != "AssertionError":
        if _pcode1 in str(call.excinfo):
            if item.config.custom_output_valid:
                data = item.config.custom_output
                status = str(call.excinfo).split(_pcode1)[1].split(_pcode2)[0]
                isFound = False
                for name in data:
                    if name == status:
                        setattr(report, _attrcode+name, True)
                        setattr(item, _status, name)
                        isFound = True
                if not isFound:
                    setattr(report, _attrcode+"unknown", True)
                    setattr(item, _status, "unknown")
                    setattr(item, _message, "Unknown output ("+status+")")
            else:
                setattr(report, _attrcode+"unknown", True)
                setattr(item, _status, "unknown")
                setattr(item, _message, "Cannot find the pytest_custom_outputs.json to load")
        else:
            setattr(item, _status, "skipped")

def get_results(request):
    item = request.node
    return {"status":getattr(item, _status, ""),"message":getattr(item, _message, "")}

def pytest_report_teststatus(report, config):
    if config.custom_output_valid:
        data = config.custom_output
        for name in data:
            if getattr(report, _attrcode+name, False):
                return data[name]["desc"],data[name]["code"],(data[name]["tag"], {data[name]["color"]: True})
    if getattr(report, _attrcode+"unknown", False):
        return "unknown","?",("UNKNOWN", {"purple": True})

