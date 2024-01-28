import os

cs_handler = "raw_response"
content_type = "image/jpeg"
pictures_path = os.path.join(cs_data_root, "courses", cs_course, "_photos")
try:
    role = cs_user_info["role"]
    assert role in {"LA", "UTA", "TA", "Instructor", "Admin"}
    fname = cs_form.get("username", "nopicture") + ".jpg"
    if not os.path.isfile(os.path.join(pictures_path, fname)):
        fname = "nopicture.jpg"
except:
    fname = "permissiondenied.jpg"

response = open(os.path.join(pictures_path, fname), "rb").read()
