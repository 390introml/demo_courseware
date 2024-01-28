cs_content_header = ""
cs_long_name = "Course Staff"

_instructors = [
    ("Priya Donti", "donti"),
    ("Kyle Keane ", "kkeane"),
    ("Manolis Kellis", "manoli"),
    ("Alexandre Megretski", "ameg"),
    ("Vince Monardo", "monardo"),
    ("Chris Tanner", "cwt"),
    ("Shen Shen", "shenshen"),
    # ("Robert Yang", "yanggr"),
]


_tas = [
    ("George Bian", "gbian"),
    ("Linh Nguyen", "linhnk"),
    ("Andrew Hutchison", "aphutch"),
    ("Emily Liu", "emizfliu"),
    ("Emily Jiang", "emji"),
    ("Haley Nakamura", "halnak"),
    ("Elisa Xia", "elisaxia"),
    ("Yogi Sragow", "ysragow"),
    ("Abhay Basireddy", "abthebee"),
    ("Shaunticlair Ruiz", "swr"),
    ("Kevin Bunn", "bunn"),
    ("Shaden Alshammari", "shaden"),
    ("Claire Lu", "luclaire"),
    ("Andi Spiride", "spiridea"),
    ("Lucian Covarrubias", "lucianc"),
]


def do_photo(name, kerb, role=None):
    if os.path.isfile(
        os.path.join(
            cs_data_root, "courses", cs_course, "__STATIC__", "staffpics", f"{kerb}.png"
        )
    ):
        imkerb = kerb + ".png"
    elif os.path.isfile(
        os.path.join(
            cs_data_root, "courses", cs_course, "__STATIC__", "staffpics", f"{kerb}.jpg"
        )
    ):
        imkerb = kerb + ".jpg"
    elif os.path.isfile(
        os.path.join(
            cs_data_root,
            "courses",
            cs_course,
            "__STATIC__",
            "staffpics",
            f"{kerb}.jpeg",
        )
    ):
        imkerb = kerb + ".jpeg"
    else:
        imkerb = "widetim.png"

    # imrole = role.lower() if role not in {"Lectures", "Recitations"} else "instructor"
    print(f'<div class="staffmember {role.lower()}">')
    print(f'<img src="COURSE/staffpics/{imkerb}" width="100%"/>')
    print(f'<div class="desc"><b>{name}</b></div>')
    print("</div>")
