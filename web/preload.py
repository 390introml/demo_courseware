# preload.py at each level defines special variables and/or functions to be
# inherited by pages farther down the tree.
import os
import re
import subprocess
import catsoop.loader as loader
from datetime import timedelta

SERVER_NAME = "introml"
IS_LOCAL = SERVER_NAME not in cs_url_root
PIAZZA_LINK = "https://piazza.com/mit/spring2024/63900/home"
SCHEDULE_LINK = ""

YEAR = "spring24"
YEAR_TITLE = "Spring 2024"

ADMIN = "Shen"
ADMIN_KERB = {"Shen": "shenshen", "Duane": "boning"}
ADMIN_EMAIL = {"Shen": "shenshen@mit.edu", "Duane": "boning@mtl.mit.edu"}

Piazza = "[Piazza](" + PIAZZA_LINK + ")"

LAB_FEEDBACK = "https://docs.google.com/document/d/1Y-PnBD1jlpAsxaLZpMYew31WZgrySeI_iTGOcl8XKTE/edit"
HW_FEEDBACK = "https://docs.google.com/document/d/1qDurusyFimRPrOXXgkKpC5pRUJhFZjOtAFnJV4KqUUU/edit"
EX_FEEDBACK = "https://docs.google.com/document/d/1xKNNtvpsdanOZ7dfoaS_nSQBL6rkEzvwW4v9sHs5WpY/edit"
REC_FEEDBACK = "https://docs.google.com/document/d/1bOKRlmKLX6DMyQePZO29rfYedGu6O1w_mlLdPfGpQAo/edit"

SWITCH_LINK = "https://canvas.mit.edu/courses/25370/external_tools/854"

if not IS_LOCAL:
    cs_scripts += """<style>
#cs_header {
  background: rgb(198,22,141);
  background: linear-gradient(90deg, rgba(198,22,141,1) 0%, rgba(102,45,145,1) 50%, rgba(0,161,199,1) 100%);
}
div.dropdown {
  -moz-transform: translateY(-1px);
}
.cs_top_menu_item {
  font-size: 0.88rem;
}
</style>
"""
cs_scripts += """<script src="https://hypothes.is/embed.js" async></script>
"""
STAGE = "regular"
# "pre_first_day", "pre_semester", "regular", "post_semester"
# LOOK AND FEEL
cs_base_font_color = "#ffffff"
cs_title = "6.390 | IntroML | " + str.capitalize(YEAR)
cs_header = "6.390"
cs_icon_url = "COURSE/logos/favicon.gif"
cs_content_header = "Introduction to Machine Learning"
cs_long_name = "Introduction to Machine Learning | " + YEAR_TITLE
cs_base_color = "#662D91"
cs_show_section_permalinks = True
cs_ui_config_flags["auto_show_explanation_with_answer"] = True

os.environ["OPENBLAS_NUM_THREADS"] = "1"  # Limit OpenBLAS to using a single thread
os.environ["OMP_NUM_THREADS"] = "1"  # for scikit learn

cs_markdown_ignore_tags = ("script", "svg", "textarea")
cs_breadcrumbs_skip_paths = {
    "recitations",
    "labs",
    "exercises",
    "homework",
    "info",
    "staffonly",
    "admin",
    #   "queue",
}
# cs_breadcrumbs_html = ""  # turn off header path display

cs_top_menu = [
    {"link": "COURSE/calendar", "text": "Calendar"},
    # {"link": "COURSE/progress", "text": "Progress"},
    {
        "text": "Info",
        "link": [
            # {"link": "COURSE/info", "text": "Basic Information"},
            # {"link": "COURSE/info/grading", "text": "Grading Policies"},
            {"link": "COURSE/info/collaboration", "text": "Collaboration Policy"},
            {"link": "COURSE/info/help", "text": "How to Get Help"},
            {"link": "COURSE/info/office_hours", "text": "Office Hours"},
            {"link": PIAZZA_LINK, "text": "Piazza"},
            {"link": "COURSE/info/staff", "text": "Staff List"},
            {"link": "COURSE/announcements", "text": "Previous Announcements"},
        ],
    },
]


def live_sessions():
    t = datetime.now()
    day = t.strftime("%A")
    hour = t.hour
    if (
        day == "Wednesday" or day == "Monday" or (t.month == 2 and t.day == 21)
    ) and 7 <= hour < 17:
        return True
    return False


# Q doesn't work locally anyway...(all dev/test have to happen on master branch on live site)
if STAGE == "regular":
    if live_sessions():
        cs_top_menu.append({"link": "COURSE/queue", "text": "Queue"})
    else:
        cs_top_menu.append({"link": "COURSE/queue/Office_Hours", "text": "Queue"})


lalinks = {
    "text": "Staff",
    "link": [
        {
            "link": "COURSE/staffonly/section_override",
            "text": "Section Override",
        },
        {
            "link": "COURSE/staffonly/how_to_be_an_la",
            "text": "How to Be an LA",
        },
        {"text": "Staff Schedule", "link": SCHEDULE_LINK},
        {
            "link": "COURSE/staffonly/local_copy",
            "text": "Set Up Local Copy",
        },
    ],
}

stafflinks = {
    "text": "Staff",
    "link": [
        {
            "link": "COURSE/staffonly/section_override",
            "text": "Section Override",
        },
        {
            "link": "COURSE/staffonly/attendance_override",
            "text": "Attendance Override",
        },
        {
            "link": "COURSE/staffonly/section_roster",
            "text": "Section Roster",
        },
        {
            "link": "COURSE/staffonly/whdw",
            "text": "Who Has Done What",
        },
        {
            "link": "COURSE/staffonly/whfw",
            "text": "Who Has Felt What",
        },
        "divider",
        {
            "link": "COURSE/staffonly",
            "text": "Staff Links",
        },
    ],
}

## AUTHENTICATION -- moved to ~/.config/catsoop/config.py
# cs_auth_type="openid_connect"
# cs_openid_server = "https://shimmer.mit.edu"
# cs_openid_client_id = "catsoop-s4"
# cs_openid_client_secret = "7sQP3tNE3lm6i40RJ3qYl2bKtl3NjPiO"


def cs_openid_email_generator(idtoken, userinfo):
    if "email" in userinfo:
        return userinfo["email"]
    elif "preferred_username" in userinfo:
        return "%s@mit.edu" % userinfo["preferred_username"]
    else:
        return "NO EMAIL"


# PYTHON SANDBOX
csq_python_sandbox_type = "bwrap"
csq_python_sandbox_interpreter = "/home/catsoop/python3_sandbox/bin/python3.9"
csq_bwrap_extra_ro_binds = [
    ("/home/catsoop/python3_sandbox", "/home/catsoop/python3_sandbox")
]
# csq_sandbox_options = {'CLOCKTIME': 5}
csq_sandbox_options = {
    "MEMORY": 1e12,
    "NPROC": 10,
}  # this may be necessary for numpy
csq_python3 = True
csq_syntax = "python"

## LOCAL
if IS_LOCAL:
    # Local sandbox
    csq_python_sandbox_type = "python"
    csq_python_sandbox_interpreter = "python3"
    csq_sandbox_options = {"MEMORY": 1e9, "do_rlimits": False}

    # Local looks.  we'll just add some flavor to make it easy to
    # tell at a glance that we're running locally.
    cs_base_color = "#A31F34"
    cs_header += " Local"


# PERMISSIONS
cs_default_role = "Guest"
cs_permissions = {
    "Admin": [
        "view_all",
        "submit_all",
        "impersonate",
        "admin",
        "staff_queue",
        "whdw",
        "email",
        "checkoff",
        "grade",
    ],
    "Instructor": [
        "view_all",
        "submit_all",
        "impersonate",
        "admin",
        "staff_queue",
        "whdw",
        "email",
        "checkoff",
        "grade",
    ],
    "TA": [
        "view_all",
        "submit_all",
        "impersonate",
        "staff_queue",
        "whdw",
        "email",
        "checkoff",
        "grade",
    ],
    "UTA": [
        "view_all",
        "submit_all",
        "impersonate",
        "staff_queue",
        "whdw",
        "checkoff",
        "grade",
    ],
    "LA": ["view_all", "submit_all", "staff_queue", "checkoff", "grade"],
    "Student": ["view", "submit"],
    "Guest": ["view"],
}

# TIMING

cs_first_monday = "2024-02-05:00:00"  # necessary for relative times to work

# shensquared: I'm running out of **time** to do the following with style... pls don't look at it...

section_times = {
    "default": {
        "wks": "M:09:00",
        "release_hw": "M:09:00",
        "rec_attendance_start": "M:09:30",
        "rec_attendance_end": "M:16:00",
        "labe": "M:23:00",
        "labs": "W:09:30",
        "lab_attendance_start": "W:09:30",
        "lab_attendance_end": "W:16:00",
        "release_ex": "W:17:00",
        "release_lab": "W:09:00",
        "hw_due": "W:23:00",
        "wke": "W:23:00",
        "wke_1": "M:09:00",
        "recitation": "M:09:00",
        # no use for below but keep-safe
        "staffmtg": "M:16:00",
    },
    0: {
        "rec_attendance_start": "M:09:30",
        "rec_attendance_end": "M:16:00",
        "lab_attendance_start": "W:09:30",
        "lab_attendance_end": "W:16:00",
    },
    1: {
        "recitation": "M:09:30",
        "rec_attendance_start": "M:09:30",
        "rec_attendance_end": "M:09:50",
        "recitation_e": "M:11:00",
        "labs": "W:09:30",
        "lab_attendance_start": "W:09:30",
        "lab_attendance_end": "W:09:50",
        # "lab_attendance_end": "W:11:00",  # first lab only
    },
    3: {
        "recitation": "M:11:00",
        "rec_attendance_start": "M:11:00",
        "rec_attendance_end": "M:11:20",
        "recitation_e": "M:12:30",
        "labs": "W:11:00",
        "lab_attendance_start": "W:11:00",
        "lab_attendance_end": "W:11:20",
        # "lab_attendance_end": "W:12:30",  # first lab only
    },
    5: {
        "recitation": "M:13:00",
        "rec_attendance_start": "M:13:00",
        "rec_attendance_end": "M:13:20",
        "recitation_e": "M:14:30",
        "labs": "W:13:00",
        "lab_attendance_start": "W:13:00",
        "lab_attendance_end": "W:13:20",
        # "lab_attendance_end": "W:14:30",  # first lab only
    },
    7: {
        "recitation": "M:14:30",
        "rec_attendance_start": "M:14:30",
        "rec_attendance_end": "M:14:50",
        "recitation_e": "M:16:00",
        "labs": "W:14:30",
        "lab_attendance_start": "W:14:30",
        "lab_attendance_end": "W:14:50",
        # "lab_attendance_end": "W:16:00",  # first lab only
    },
}
# shensquared ... at least i could do this...
section_times[2] = section_times[1]
section_times[4] = section_times[3]
section_times[6] = section_times[5]
# section_times[8] = section_times[7]

# global date overrides (for e.g. holidays)
# lab05 is due on T, its M is a holiday:
# section_times["default"]["labe:6"] = "T:23:00"

sections = {
    "1": ("9:30am-11am", "", "34-501"),
    "2": ("9:30am-11am", "", "32-044"),
    "3": ("11am-12:30pm", "", "34-501"),
    "4": ("11am-12:30pm", "", "32-044"),
    "5": ("1pm-2:30pm", "", "34-501"),
    "6": ("1pm-2:30pm", "", "32-044"),
    "7": ("2:30pm-4pm", "", "34-501"),
    # "8": ("2:30pm-4pm", "", "32-044"),
}

office_hours = [
    ("Sunday", "5-7pm", "Virtual"),
    ("Sunday", "7-9pm", "Virtual"),
    ("Monday", "7-9pm", "32-044"),
    ("Monday", "9-11pm", "Virtual"),
    ("Tuesday", "3-5pm", "32-044"),  # instead of 4-6pm
    ("Tuesday", "7-9pm", "32-044"),
    ("Wednesday", "4-6pm", "32-044"),  # NOTE: does not match Tuesday
    ("Wednesday", "7-9pm", "32-044"),
    ("Wednesday", "9-11pm", "Virtual"),
    ("Thursday", "1-3pm", "32-044"),
]
cs_show_due = False


def cs_due_date_message(duedate):
    return ""


assignment_types = [
    "recitations",
    "labs",
    "homework",
    "exercises",
]

wall = assignment_types + [
    "calendar",
    "queue",
    "progress",
    "admin",
    "midterm",
    "final",
    "staffonly",
]


def cs_realize_time(meta, rel, force_section=None):
    """
    Make due date by converting relative time specification, like "labe:2" to a datetime
    Returns a datetime

    meta: (dict) context, or globals(), with cs_user_info
    rel: (str) relative time spec, e.g. "labe:2" -- lab end for section 2
    force_section: (None or int) section to use for the time computation -- use for debugging and output to staff
    """
    from datetime import datetime

    if isinstance(rel, datetime):  # needed, e.g. for nq activation code
        return rel

    uinfo = meta.get("cs_user_info", {})

    # try:
    #     if uinfo.get("username") in {"shenshen"} and uinfo.get("role") == "Student":
    #         meta["cs_first_monday"] = "2023-01-23:00:00"
    # except:
    #     pass

    try:
        section = uinfo.get(
            "section", 0
        )  # lab due date uses 'section' in user_info (see cs_handle_section_override)
    except:
        section = 0

    if force_section:
        section = int(force_section)  # should already be an int, but just make sure

    default = section_times.get("default", {})
    special = section_times.get(section, {})
    real = dict(default)
    # shensquared [question]
    # seems to be checking user.py field, harmless at the moment. but need to understand it later.
    for key, when in uinfo.get("times_override", []):
        special[key] = when

    real.update(special)
    try:
        start, end = rel.split(":")
        # see if labe:5 is in the dict, otherwise default to labe
        rel = real.get(rel, real[start])
        meta["cs_week_number"] = int(end)
    except:
        pass
    try:
        rt = csm_time.realize_time(meta, rel)
    except Exception as err:
        print(
            "[6.390.preload.cs_realize_time] failure in csm_time.realize_time, with meta=%s, rel=%s, err=%s"
            % (str(meta)[:100], str(rel)[:100], err)
        )
        raise
    # print(f"path is {cs_path_info[1:]}, rel is {rel}, and time is {rt}")
    return rt


def show_checkoff_grade():
    chk = csm_cslog.most_recent(cs_username, cs_path_info, "checkoff", None)
    if chk is None:
        return '<div class="response"><i>You have not yet received this checkoff.</i></div>'
    out = '<div class="response">\n\n**You have received this checkoff!**'
    if chk["comments"]:
        out += (
            '<p style="margin-top:1em"><b>Comments from Grader:</b><br/>%s</p>'
            % csm_language.source_transform_string(
                globals(), chk["comments"].replace("<", "&lt;").replace(">", "&gt;")
            )
        )
    return out + "</div>"


#
def cs_post_load(context):
    if "cs_loader_states" in context:
        elements = [context["cs_title"]]
        to_skip = context.get("cs_breadcrumbs_skip_paths", [])
        for ix, elt in enumerate(context["cs_loader_states"]):
            if ix == 0:
                continue
            if "/".join(context["cs_path_info"][1 : ix + 1]) in to_skip:
                continue
            if context.get("cs_breadcrumbs_skip", False):
                continue
            elements.append(elt.get("cs_long_name", context["cs_path_info"][ix]))
        context["cs_title"] = " | ".join(
            re.sub(r":[^\s:]*:", "", i) for i in elements[::-1]
        )
    if len(cs_path_info) == 1:
        context[
            "cs_content_header"
        ] = "<img src='COURSE/logos/eecslogo.svg' height=115px/>&emsp; <img src='COURSE/logos/390.png' height=120px/><br><img src='COURSE/logos/txt.png' height=30px/><br>Introduction to Machine Learning <br/>(Spring 2024)"
    cui = context.get("cs_user_info", {})
    uname = cui.get("username", "None")
    _role = cui.get("role", None)
    is_staff = _role in {"LA", "TA", "UTA", "Admin", "Instructor"}
    is_authorized = _role == "Student" or is_staff

    if _role in ("TA", "UTA", "Instructor", "Admin"):
        stafflinks["link"].insert(
            3,
            {"text": "Staff Schedule", "link": SCHEDULE_LINK},
        )

    if (is_staff and _role != "LA") or uname == "shenshen":
        context["cs_top_menu"].insert(-1, stafflinks)
    if _role == "LA":
        context["cs_top_menu"].insert(-1, lalinks)
    if str(context["cs_username"]) != "None":
        try:
            del context["cs_top_menu"][-1]["link"][0]  # remove user 'settings'
        except:
            pass
    # needs to be called before due dates are
    try:
        cs_handle_section_override(cui)
    except:
        pass

    if _role in {"Admin", "Instructor"} or uname in {
        "tvbraun",
        "shenshen",
        "boning",
        "tlp",
        "hartz",
    }:
        stafflinks["link"].insert(
            0,
            {"text": "Exceptions", "link": "COURSE/staffonly/exceptions"},
        ),
        stafflinks["link"].insert(
            -1,
            {
                "text": "Notes Overleaf",
                "link": "https://www.overleaf.com/9971114968rjykqmkhtmbp#c16c2a",
            },
        )

    def pre_semester():
        if not is_authorized and len(cs_path_info) > 1 and cs_path_info[-1] != "staff":
            context[
                "cs_content"
            ] = '<div class="impsolution">This page is currently accessible to 6.390 course staff members only.</div>'
        # if not is_staff:
        #     context["cs_top_menu"] = [context["cs_top_menu"][-1]]
        pre_first_day()

    def pre_first_day():
        if len(cs_path_info) > 1:
            context[
                "cs_content"
            ] = f'<div class="impsolution">You are viewing a draft version of the 6.390 web site. Please note that information on this page may change between now and the start of the semester. \n\n</div>{context["cs_content"]}'

    if STAGE == "pre_semester":
        pre_semester()
    elif STAGE == "pre_first_day":
        pre_first_day()
    elif STAGE == "regular":
        pass
    elif STAGE == "post_semester":
        pass

    if (
        not is_authorized
        and len(cs_path_info) > 1
        and cs_path_info[1] in wall
        and cs_path_info[-1] != "hw01"
        and cs_path_info[-1] != "lab01"
    ):
        # if we allow for viewing but not submitting
        context[
            "cs_content"
        ] = '<div class="impsolution">You will need an account on the 6.390 web site in order to view this page. Please contact us at <code>6.390-website@mit.edu</code> to obtain an account.  Note that you also need to have satisfied the prerequisite to submit assignments for 6.390.</div>'
    if _role == "Disallowed":
        context["cs_content"] = (
            '<div class="impsolution">According to our records, you have not completed the prerequisite for 6.390.  As such, you will not be allowed to submit to assignments in 6.390.  If you believe you are receiving this message in error, please fill out <a href="COURSE/prereq">this form</a> describing your situation.</div>\n\n%s'
            % context["cs_content"]
        )
    # if this is an assignment, inject due date:
    if (
        len(cs_path_info) == 3
        and cs_path_info[1] in assignment_types
        and "cs_due_date" in context
    ):
        date_format = "%A, %B %d, %Y at %I:%M %p"
        due = cs_realize_time(context, context["cs_due_date"])
        deadline = due.strftime(date_format)
        try:
            days = cs_get_extension(cs_path_info[1], int(cs_path_info[2][-2:]))
            if days != 0:
                extended = (due + timedelta(days=days)).strftime(date_format)
                msg = f"<p><b>Extended due date:</b> {extended}<br/>(Original due date: {deadline})</p>"
            else:
                msg = f"<p><b>Due:</b> {deadline}</p>"
        except:
            msg = f"<p><b>Due:</b> {deadline}</p>"
        # add it under the first h1, and if it doesn't exist, just add it to the top
        new_content, num_subs = re.subn(
            r"((<h1>([^<>]*)</h1>)|(^# .*$))",
            "\\1\n" + msg,
            context["cs_content"],
            count=1,
            flags=re.M,
        )
        if num_subs:
            context["cs_content"] = new_content
        else:
            context["cs_content"] = msg + new_content
    base_url = "/".join([context["cs_url_root"]] + context["cs_path_info"])

    if (cui.get("section", 0)) and cs_top_menu:
        cs_top_menu[-1].update(
            {
                "text": cs_top_menu[-1]["text"]
                + " (Section: "
                + str(cui.get("section", 0))
                + ")"
            }
        )
    if uname in ("boning", "tlp", "shenshen"):
        if context["cs_form"].get("as_role", None):
            context["cs_top_menu"].insert(
                0, {"text": "(To) Staff View", "link": "%s" % base_url}
            )
        else:
            context["cs_top_menu"].insert(
                0,
                {"text": "(To) Student View", "link": "%s?as_role=Student" % base_url},
            )
    # show_sha(context)


def show_sha(context):
    try:
        loc = os.path.abspath(
            os.path.join(context["cs_data_root"], "courses", *context["cs_path_info"])
        )
        git_info = subprocess.check_output(
            [
                "git",
                "log",
                "--pretty=format:%h %ct %an",
                "-n1",
                "--",
                "content.md",
                "content.xml",
                "content.py",
                "content.catsoop",
            ],
            cwd=loc,
        ).decode("utf-8")
        h, t, a = git_info.split(" ", 2)
        t = (
            context["csm_time"]
            .long_timestamp(datetime.fromtimestamp(float(t)))
            .replace(";", " at")
        )
        context["cs_footer"] = (
            "This page was last updated on %s (revision <code>%s</code>).<br/>&nbsp;<br/>"
            % (t, h)
        )
    except:
        pass


def cs_handle_section_override(cui):
    """
    Override section assignment if appropriate unexpired record exists in the section_override cslog db.
    """
    username = cui["username"]

    # Handles split rec/lab section
    if username == "echang25":
        t = datetime.now()
        day = t.strftime("%A")
        if day == "Wednesday":
            cui["section"] = 4

    db_name = "section_override"
    data = csm_cslog.most_recent(db_name, [], username, {})
    if data and "expiration" in data:
        # print(
        # "[cs_handle_section_override] got section override for %s: %s"
        # % (username, data)
        # )
        if data["expiration"] > datetime.now():
            # print(
            # "[cs_handle_section_override] changing section for %s from %s to %s"
            # % (username, cui["section"], data["secnum"])
            # )
            cui["section"] = data["secnum"]
        # else:
        #     print(
        #         "[cs_handle_section_override] override for %s expired, leaving unchanged"
        #         % username
        #     )


# CHECKERS
# ----------------------------------------
# Common 6.036 checkers
# Use in exercises, hw, labs, nqs, etc.
# ----------------------------------------

import numpy as np

# ----------------------------------------
# pythonic and other checkers
# ----------------------------------------

csq_allow_save = False
check_equal = csm_check.equal()
check_equal_set = lambda sub, soln: isinstance(sub, (list, tuple)) and set(sub) == set(
    soln
)
check_equal_dict = csm_check.dict_all()
check_nocase_str_equal = lambda sub, soln: str(sub).casefold() == str(soln).casefold()


def check_none(sub, soln):
    if soln == "None" or soln == "none":
        soln = None
    if sub == "None" or sub == "none":
        sub = None
    return sub == soln


def check_count(sub, soln):
    credit_per_correct = 1 / sum(soln)
    correct = sum(i == j == True for i, j in zip(sub, soln)) * credit_per_correct
    incorrect = (
        sum(i == True and j == False for i, j in zip(sub, soln)) * credit_per_correct
    )
    return max(0, correct - incorrect)


check_close = csm_check.number_close(absolute_threshold=1.0e-6)

# list checkers
check_close_list_unordered = csm_check.list_all_unordered(check_close)


def make_check_close_list(tol=1.0e-6):
    return csm_check.list_all(csm_check.number_close(tol))


check_close_list = make_check_close_list()


def make_check_close_list_of_list(tol=1.0e-6):
    return csm_check.list_all(csm_check.list_all(csm_check.number_close(tol)))


check_close_list_of_list = make_check_close_list_of_list()


def check_list_partial_credit(sub, soln):
    if not isinstance(sub, (list, tuple)) or len(sub) != len(soln):
        return (
            0,
            "<font color='red'>Answer should be a list with %d elements.</font>"
            % len(soln),
        )
    same = [sub[i] == soln[i] for i in range(len(soln))]
    return sum(same) / len(same)


# vector and array checkers
def make_check_close_array(tol=1.0e-6):
    def _checker(sub, soln):
        # sub, soln as created by ans=<np.array>.tolist()
        sub_a = np.array(sub)
        sol_a = np.array(soln)
        return sub_a.shape == sol_a.shape and np.all(np.isclose(sub_a, sol_a, atol=tol))

    return _checker


check_close_array = make_check_close_array()


def check_array_shape(sub, soln):
    return np.array(sub).shape == np.array(soln).shape


def vector_normalize(col_v):
    return col_v / np.sum(col_v * col_v) ** 0.5


def check_scaled_vector(sub, soln):
    return (
        np.max(
            np.abs(vector_normalize(np.array(sub)) - vector_normalize(np.array(soln)))
        )
        < 1.0e-6
    )


def make_array_type_checker(allowed_types):
    def _checker(sub, soln):
        sub_a = np.array(sub["result"])
        return sub_a.dtype in allowed_types

    return _checker


# ----------------------------------------
# pythoncode checkers
# ----------------------------------------

# sub and soln in pythoncode questions types are
# dictionaries, with keys 'results' and other elements. Here
# we wrap the pythonic checker with check_result to use
# corresponding 'results' rather than dictionaries.

pycode_equal = csm_check.check_result(check_equal)
pycode_equal_set = csm_check.check_result(check_equal_set)
pycode_equal_dict = csm_check.check_result(check_equal_dict)

pycode_close = csm_check.check_result(check_close)
pycode_close_list = csm_check.check_result(check_close_list)
pycode_close_list_unordered = csm_check.check_result(check_close_list_unordered)
pycode_close_list_of_list = csm_check.check_result(
    csm_check.list_all(csm_check.list_all(check_close))
)


def make_pycode_close_array(tol=1e-6):
    return csm_check.check_result(make_check_close_array(tol))


pycode_close_array = make_pycode_close_array()
pycode_array_shape = csm_check.check_result(check_array_shape)
pycode_scaled_vector = csm_check.check_result(check_scaled_vector)


def make_pycode_close_array_list(tol=1e-6):
    return csm_check.check_result(csm_check.list_all(make_check_close_array(tol)))


pycode_close_array_list = make_pycode_close_array_list()

# ----------------------------------------
# source code checkers
# ----------------------------------------


import ast


def ast_search(node, check_func):
    return [i for i in ast.walk(node) if check_func(i)]


def loop_count(node):
    return len(
        ast_search(
            node,
            lambda x: isinstance(
                x,
                (
                    ast.For,
                    ast.While,
                    ast.ListComp,
                    ast.DictComp,
                    ast.SetComp,
                    ast.GeneratorExp,
                ),
            ),
        )
    )


def no_loops(source):
    # node = ast.parse(source)
    try:
        node = ast.parse(source)
    except:
        return None  # say that there are no issues so that the question itself can report the issue
    if loop_count(node):
        return "Your code should not use any explicit loops"


def at_most_one_loop(source):
    try:
        node = ast.parse(source)
    except:
        return None  # say that there are no issues so that the question itself can report the issue
    if loop_count(node) > 1:
        return "Your code may use at most one explicit loop"


def is_norm_call(n):
    return isinstance(n, ast.Attribute) and n.attr == "norm"


def no_loops_or_norm(code):
    no_loop_report = no_loops(code)
    if no_loop_report:
        return no_loop_report
    try:
        t = ast.parse(code.strip().replace("\r\n", "\n"))
        prepare_ast(t)
        calls = downward_search(t, is_norm_call)
    except:
        return None  # let Python handle syntax errors
    if len(calls) > 0:
        return "Your code should not call `np.linalg.norm` function."


def prepare_ast(tree, parent=None):
    tree._hz_parent = parent
    tree._hz_children = list(ast.iter_child_nodes(tree))
    for i in tree._hz_children:
        prepare_ast(i, tree)


def downward_search(node, testfunc):
    out = []
    if testfunc(node):
        out.append(node)
    for i in node._hz_children:
        out.extend(downward_search(i, testfunc))
    return out


def check_types_and_value(allowed_types, tol=1.0e-6):
    def _checker(sub, soln):
        types_checker = make_array_type_checker(allowed_types)
        values_checker = make_pycode_close_array(tol)
        return types_checker(sub, soln) and values_checker(sub, soln)

    return _checker


def make_check_is_one_of(choices):
    def _checker(sub, soln):
        sub = np.array(sub).tolist()
        return sub in choices

    return _checker


def make_pycode_is_one_of(choices):
    return csm_check.check_result(make_check_is_one_of(choices))


def make_check_is_almost_one_of(choices):
    def _checker(sub, soln):
        sub = np.array(sub).tolist()
        response = [False] * len(sub)
        for choice in choices:
            for i, value in enumerate(sub):
                if value == choice[i]:
                    response[i] = True
        return sum(response) / len(response)

    return _checker


def make_pycode_is_almost_one_of(choices):
    return csm_check.check_result(make_check_is_almost_one_of(choices))


######### CALLOUTS


def callout(note, header, style):
    return """<div class="callout callout-%s"><h5>%s</h5>%s</div>""" % (
        style,
        header,
        csm_language._md_format_string(globals(), note),
    )


# def note(x, title="Note"):
#     return callout(x, title, "info")

# def becareful(x, title="Be Careful!"):
#     return callout(x, title, "danger")

# def trynow(x):
#     return callout(x, "Try Now", "warning")

# def aside(x):
#     return callout(x, "Aside", "warning")


def environment_matcher(tag):
    return re.compile(
        """<%s>(?P<body>.*?)</%s>""" % (tag, tag), re.MULTILINE | re.DOTALL
    )


def cs_course_handle_custom_tags(text):
    def handle_todo(m):
        if (
            cs_user_info.get("role", None) in {"UTA", "TA", "Instructor", "Admin"}
            or cs_user_info.get("username", None) == "shenshen"
        ):
            return callout(m.groupdict()["body"], "TODO", "error")
        return ""

    todo_regex = re.compile(r"<todo>(?P<body>.*?)</todo>", re.MULTILINE | re.DOTALL)
    text = re.sub(todo_regex, handle_todo, text)

    def handle_staffnote(m):
        if (
            cs_user_info.get("role", None) in {"UTA", "TA", "Instructor", "Admin", "LA"}
            or cs_user_info.get("username", None) == "shenshen"
        ):
            return callout(m.groupdict()["body"], "Staff Note", "note")
        return ""

    staffnote_regex = re.compile(
        r"<staffnote>(?P<body>.*?)</staffnote>", re.MULTILINE | re.DOTALL
    )
    text = re.sub(staffnote_regex, handle_staffnote, text)

    # CHECKOFFS AND CHECK YOURSELFS
    checkoffs = [0]

    def docheckoff(match):
        d = match.groupdict()
        checkoffs[0] += 1
        return (
            '<div class="checkoff"><b>Checkoff %d:</b><p>%s</p><p><span id="queue_checkoff_%d"></span></p></div>'
            % (checkoffs[0], d["body"], checkoffs[0])
        )

    text = re.sub(environment_matcher("checkoff"), docheckoff, text)

    # GOALS
    text = re.sub(
        environment_matcher("goals"),
        lambda m: '<div class="question"><b>Goals:</b>%s</div>' % m.groupdict()["body"],
        text,
    )

    # PAGE BREAKS
    text = re.sub("<page(.*?)>", '<div class="pagebreak"></div>', text)

    # FRAMED TEXT
    text = re.sub(
        environment_matcher("framedtext"),
        lambda x: '<div class="question">%s</div>' % x.groups()[0],
        text,
    )

    return text


def q_room(context):
    room = "Office_Hours"
    # shensquared still hard coding, needs a better way
    # adding Monday recitation just in case
    if live_sessions():
        section = context.get("cs_user_info", {}).get("section", 0)
        if section in [2, 4, 6, 8]:
            room = "32-044"
        else:
            room = "34-501"
    context["queue_room"] = room


def assignment_path_end(type, num):
    if type == "exercises":
        return "ex%02d" % num
    elif type == "labs":
        return "lab%02d" % num
    elif type == "homework":
        return "hw%02d" % num
    elif type == "recitations":
        return "rec%02d" % num
    return None


def cs_get_extension(type, num, uname):
    path = [cs_course, type, assignment_path_end(type, num)]
    try:
        entry = csm_cslog.most_recent(uname, path, "extensions", {})
    except:
        entry = {}
    # print(entry)
    return entry.get("days", 0)


def release_due(type, num):
    name = assignment_path_end(type, num)
    path = [cs_course, type, name]
    ctx = loader.generate_context(path)
    release = cs_realize_time(ctx, ctx.get("cs_release_date", "NEVER"))
    due = cs_realize_time(ctx, ctx.get("cs_due_date", "NEVER"))
    # try:
    # due = ctx["cs_realize_time"](ctx, ctx["cs_due_date"])
    return release, due


def cs_pre_handle(context):
    from collections import defaultdict

    textsections = [None, 0, 0, 0]
    tags = [
        "chapter",
        "section",
        "subsection",
        "subsubsection",
    ]

    counts = {
        "checkoff": 0,
        "checkyourself": 0,
        None: 0,
    }
    texts = defaultdict(
        lambda: "Tutor Question {count} in Section {section}",
        {
            "checkoff": "Checkoff {count}",
            "checkyourself": "Check Yourself {count}",
        },
    )

    for problem in context.get("cs_problem_spec", []):
        try:
            if type(problem) is str:
                section_re = re.compile(
                    r"""
                <
                \s*
                (?P<name>chapter|(sub){0,2}section)
                .*?
                (num\s*(?P<quote>['"])=\s*(?P<num>\d+)(?P=quote))?
                \s*
                >
                """,
                    re.VERBOSE,
                )
                for match in section_re.finditer(problem):
                    name = match.group("name")
                    index = tags.index(name)

                    if match.group("num") is not None:
                        num = int(match.group("num") or "0")
                        textsections[index] = num
                    else:
                        if textsections[index] is None:
                            textsections[index] = 0
                        textsections[index] += 1

                    textsections[index + 1 :] = [0] * (len(textsections) - (index + 1))
                    # checkoff and checkyourself are counted per-page,
                    # but everything else is per-section
                    counts = {
                        "checkoff": counts["checkoff"],
                        "checkyourself": counts["checkyourself"],
                        None: 0,
                    }
            else:
                qtype, qinfo = problem

                if qtype["qtype"] in counts:
                    counts[qtype["qtype"]] += 1
                    count = counts[qtype["qtype"]]
                else:
                    counts[None] += 1
                    count = counts[None]

                text = texts[qtype["qtype"]]

                if "csq_display_name" not in qinfo:
                    qinfo["csq_display_name"] = text.format(
                        count=count,
                        section=".".join(str(n) for n in textsections if n),
                    )
                else:
                    if qtype["qtype"] == "checkyourself":
                        qinfo["csq_display_name"] = "Check Yourself {}: {}".format(
                            counts[qtype["qtype"]],
                            qinfo["csq_display_name"],
                        )
                qinfo["csq_display_count"] = count
        except:
            pass


########## midterm exam room ##########


def get_room_headcount(db, role="Student"):
    roster = csm_user.all_users_info(
        globals(), cs_course, lambda u: u.get("role", None) == role
    )
    # print(f"[get_room_headcount] {db=}")
    # print(f"[get_room_headcount] {roster=}")
    out = {}
    for i in roster:
        sec = cslog.most_recent(i, [cs_course], db, None)
        if sec:
            out.setdefault(sec, set()).add(i)
    return out


midterm_rooms = {
    # Regular ones
    "0": ("50-340 (Walker)", "Wed, 20 Wed, 7:30pm-9:30pm", 250),
    "1": ("26-100", "Wed, 20 Wed, 7:30pm-9:30pm", 220),
    "2": ("45-230", "Wed, 20 Wed, 7:30pm-9:30pm", 318),
    # accomodations
    "3": ("32-123", "Wed, 20 Wed, 7pm-10pm", 150),
    "4": ("54-100", "Wed, 20 Wed, 7pm-10pm", 150),
    #
    "5": ("32-123", "Wed, 20 Wed, 7:30pm-9:30pm", 318),
    "6": ("2-190", "Thur, 26 Oct, 8am-10am (conflict)", 67),
    "7": ("24-307", "Thur, 26 Oct, 10am-noon (extra conflict)", 5),
    "8": ("35-225", "Wed, 20 Wed, 7pm-10pm (accommodation)", 45),
    # reweight
    "9": ("None", "Excused from midterm; reweight final", 5),
}

rooms_allowed_to_change = {"0", "1"}  # where people can self-change intro

accommodations = {"2": "conflict exam", "3": "time and a half", "4": "double time"}


def get_midterm_room(kerb, db="midterm_room"):
    room_id = csm_cslog.most_recent(kerb, [cs_course], db, None)
    if room_id and room_id in midterm_rooms:
        room_name, room_time, _ = midterm_rooms[room_id]
        return room_id, room_name, room_time
    return None, None, None
