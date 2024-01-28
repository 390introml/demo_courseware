<todo>
- need to rewrite basic info page. remember to add back. the same for the grading page.
- need to test queue and progress. and remember to add the tabs back.
</todo>

## Pre-semester Information

👋 Hi there! Welcome to 6.390 -- we're very much looking forward to
working with you all this spring!

<catsoop-section>Course Overview
</catsoop-section>
6.390 introduces the principles and algorithms of machine learning from an optimization perspective. Topics include linear and non-linear models for supervised, unsupervised, and reinforcement learning, with a focus on gradient-based methods and neural-network architectures. Enrollment may be limited.

<catsoop-section>
Prerequisites
</catsoop-section>
Concretely, things we expect you to know (we use these constantly, but
don’t teach them explicitly):

<catsoop-subsection>
Programming
</catsoop-subsection>

- Intermediate Python, including the notion of classes.
- Exposure to algorithms – ability to understand & discuss
  pseudo-code, and implement in Python.

<catsoop-subsection>
Linear Algebra
</catsoop-subsection>

- Fundamental matrix concepts and manipulations, e.g., rank, multiplication, 
  and inverse.
- Points and planes in high-dimensional space.
- Basic matrix calculus, e.g., gradients.

[6.1010](https://py.mit.edu/fall23/calendar) or [6.1210](https://learning-modules.mit.edu/materials/index.html?uuid=/course/6/sp20/6.006#materials) can serve as the programming prerequisite.

[18.06](https://github.com/mitmath/1806), [18.C06](https://canvas.mit.edu/courses/16629), [18.03](https://math.mit.edu/~dyatlov/18.03/), or [18.700](https://math.mit.edu/~dav/700.html) can serve as the linear algebra prerequisite.

(For each of these courses above, a link points to a representative syllabus from some past semesters, for reference.)
<comment>
<catsoop-section>
Useful Background
</catsoop-section>

Things it helps to have prior exposure to, but we don’t expect (we use
these in 6.390, but will discuss as we go):

- `numpy` (Python package for matrix/linear algebra).
- `pytorch` (Python package for neural networks).
- Basic discrete probability, e.g., random variables, conditioning, and expectation.
</comment>
<catsoop-section>
Class Meeting and Sections
</catsoop-section>
We will be meeting on Mondays (Recitations), Wednesdays (Labs), and Fridays (Lectures). 

<catsoop-subsection>
Recitation and Lab sections
</catsoop-subsection>

Monday recitations focus on discussing examples and working through pen-paper problems. Wednesday labs engage students with each other in small teams (typically two to three students per team) and with staff, to explore fundamental concepts.

Recitations and Labs will be held in small sections. As of now, we have seven sections planned.
<ul>
 <python>
    print("<center>")
    import pandas as pd
    from pretty_html_table import build_table

    timetable = []
    for num, info in sections.items():
      timetable.append([num, "Mon & Wed, " + info[0], info[2], info[1]])
    # table_header = ["Section", "Time", "Room", "Instructor"]
    table_header = ["Section", "Time", "Room", ""]
    df = pd.DataFrame(data=timetable, columns=table_header).convert_dtypes()
    print(build_table(df, "blue_light"))
    print("</center>")

  </python>
</ul>

Our first class meeting will be a Recitation on Monday, Feb. 5. Each student will be assigned into one section. Section assignments and a self-switch mechanism will be detailed here as we near the semester start. 


<comment>
If you
pre-registered for 6.390, the Registrar will likely schedule you into
a section during the registration week. Towards the end of that week,
we'll provide info here on where to see your assigned section and
what-to-do if you don't have one.

If at all possible, **please attend the section you are scheduled into
by the Registrar for this first session**. Subsequently, we'll have a
mechanism through which you can make changes in your scheduled
section. Self-switching will be first-come-first-served and subject to
section capacity constraints; the process will be detailed here.
</comment>

<catsoop-subsection>
Friday Lectures
</catsoop-subsection>
Friday lectures focus to anchor the upcoming week's discussion, overview the technical contents, and tie together the high-level motivations, concepts, and stories. Along with lecture notes, they prepare students for the upcoming Monday recitations and Wednesday labs.

Lectures will be held class-wide, in Room 10-250, Fridays 11am-12pm. Recordings will be made available shortly after live sessions. Our first lecture will be on Friday, Feb. 9. 

<comment>
You can see your assigned section under "Section Signup" on the
[Canvas site for 6.390](@{SWITCH_LINK}). If you
registered later and don't have a section, please choose one using
"Section Signup". In addition, if you need to change your permanent
section assignment, you can **self-switch** into another section with
"Section Signup", .

If at all possible, **please attend the section shown on Canvas.**
</comment>

<!-- <catsoop-section>
Course Components
</catsoop-section> -->

<catsoop-section>Cross-registration
</catsoop-section>

- This site is our course site and it uses MIT Kerberos for
  authentication. Cross-registered students will receive their
  Kerberos once the registration goes through; however, the process
  can take a while. We therefore strongly encourage you to cross
  register early if possible, to avoid delayed access to course
  materials.

- We follow MIT's [Academic Calendar](https://registrar.mit.edu/calendar), and do not have additional extensions or
  accommodations based on home university calendar. Especially
  important will be for you to plan ahead for our two in-person
  exams. 

- We'll have a **midterm exam** (on Wednesday March 20, 2024, 7:30pm-9:30pm).  We'll also have a **final exam** during MIT's final exam period, Friday, May 17 through Wednesday, May 22; the final exam is to be scheduled by the Registrar.
<comment>

- **Wellesley seniors**: Please note that [Wellesley](https://webapps.wellesley.edu/class_schedule/academic_calendar.php?start_year=2023&end_year=2024) requires letter grades by May 14 at noon for senior graduation purposes. Unfortunately, we will not be able to get a letter grade ready into Wellesley system by that deadline. 

</comment>
- If you're not familiar with MIT campus, you might find the
  [whereis](https://whereis.mit.edu) site helpful.


<catsoop-section>Listeners
</catsoop-section>
Due to capacity and other constraints, we will not accept Listener
registrants in 6.390 this semester.

<catsoop-section>LA Applications
</catsoop-section>

[LA Applications for 6.390](https://eecsla.mit.edu/spring24) have opened. 
Consider joining our teaching team! Requirements and expectations are on the application site.

<catsoop-section>Course Number Change</catsoop-section>

Since fall22, all MIT EECS (Course 6) subjects have been renumbered
(rationale and details can be found
[here](https://www.eecs.mit.edu/academics/subject-numbering/)). This
subject used to be called 6.036; moving forward, we'll refer to it
internally as 6.390 ("six three-nine-oh"). But for registration
purposes, please register for **6.3900** (note the extra zero).


<catsoop-section>Other Questions?</catsoop-section>

Feel free to drop us an email at
[`6.390-inquiry@mit.edu`](mailto:6.390-inquiry@mit.edu). We'd love to
hear from you!
