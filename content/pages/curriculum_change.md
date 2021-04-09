Title: Curriculum Transition
url: curriculum-change.html
save_as: curriculum-change.html
sortorder: 70
status:hidden


> This document is a **working draft** and may not accurately reflect current or future policy.


# Curriculum Transition

After years of careful analysis and design, including piloting new courses and getting approvals from the school and university, the CS department is changing its curriculum. The largest component of this change involves moving topics between courses to reduce duplication and improve flow. Because of that change, it is generally not possible to mix-and-match courses from the old and new curriculum.

## Roughly-equivalent courses

The following pairs of courses are similar enough in content that either one may be taken in place of the other:

| Old Course | New Course | Differences |
|------------|------------|-------------|
| CS 2102 Discrete Mathematics | CS 2120 Discrete Mathematics and Theory 1 | 2120 is more fully specified, including coverage of proof writing skills; these were optional in 2102 and present in only some sections |
| CS 3102 Theory of Computation | CS 3120 Discrete Mathematics and Theory 2 | 3120 has an additional prerequisite (CS 3100 or CS 4102) and includes more coverage of the mathematical characteristics of algorithms and data structures |
| CS 4102 Algorithms | CS 3100 Data Structures and Algorithms 2 | 4102 focuses more on proofs of algorithm correctness, and 3100 covers a wider array of algorithms including basic machine learning algorithms |

SIS has been coded to accept either course in place of the other.
Before you take a course, SIS will show only one of the two options
(the one that matches the curricular requirements you declared);
after you are enroll in the alternative course it will show up as meeting the other course's requirements.

## Per-degree course sets

Because of content motion, degrees require a full change in CS courses;
mixing and matching is not permitted except (a) for the three courses listed above and (b) in special cases which can be worked out and approved on an individual basis.

By default, the academic year in which you declare a major or minor is used to pick the version of the major or minor you are in.
As a special case for the BS CS, BA CS, and CS Minor, students who declare the after the new requirements are in place but who have the old requirements will be placed in the old requirements instead.


### BS CS

A student must either graduate under [the AY 20-21 record](http://records.ureg.virginia.edu/preview_program.php?catoid=49&poid=6227) (or earlier), which includes these courses:

- CS 2110
- CS 2150
- CS/ECE 2330
- CS 3330
- CS 4414

Or under the AY 21-22 record (or later), which includes these courses:

- CS 2100
- CS 2130
- CS 3130
- CS 3140

There are other requirements for each (including the three roughly-equivalent courses, CS 3240, etc);
students should consult the record for more details.

By default, the academic year in which you declare a major is used to pick the version of the major you are in.
As a special case, students who declare the major in AY 21-22 or later but who have taken AY 20-21 courses will be given the AY 20-21 degree requirements.

### BA CS

A student must either graduate under [the AY 21-22 record](http://records.ureg.virginia.edu/preview_program.php?catoid=49&poid=6226) (or earlier), which includes these courses:

- CS 2110 (prereq)
- CS 2150
- CS 3330

Or under the AY 22-23 record (or later), which includes these courses:

- CS 2100 (prereq)
- CS 2130
- CS 3130
- CS 3140

There are other differences between these two degree versions,
including other CS courses; students should consult the record for more details.

By default, the academic year in which you declare a major is used to pick the version of the major you are in.
As a special case, students who declare the major in AY 22-23 or later but who have taken AY 21-22 courses will be given the AY 22-23 degree requirements.

### CS Minor

A student must either use [the AY 20-21 record](http://records.ureg.virginia.edu/preview_program.php?catoid=49&poid=6227#Minor) (or earlier), which includes these courses:

- CS 2110
- CS 2150

Or the AY 21-22 record (or later), which includes these courses:

- CS 2100
- CS 2130
- CS 3140

There are other requirements for each (including CS 2102 or 2120 and several CS electives);
students should consult the record for more details.

# Anticipated schedule of changes

The exact change schedule will vary based on the speed at which the new BA CS program is approved (the following assumes it will be approved prior to Spring 2022) and the facility with which we can transition students who took old course prereqs into new or changed courses.

Entries show "—" if the course is not planned on being offered;
a new course number if a different course will satisfy this requirement;
and "changed" if the course will remain, but its contents or prerequisites change.


| Course | Fall 2021 | Spring 2022 | Fall 2022 | Spring 2023 | Fall 2023 | Spring 2024 and beyond |
|:-------|:---------:|:-----------:|:---------:|:-----------:|:---------:|:----------------------:|
| CS 2100| —         | Yes         | Yes       | Yes         | Yes       | Yes                    |
| CS 2120| Yes       | Yes         | Yes       | Yes         | Yes       | Yes                    |
| CS 2130| —         | Yes         | Yes       | Yes         | Yes       | Yes                    |
| CS 3100| —         | —           | Yes       | Yes         | Yes       | Yes                    |
| CS 3120| —         | —           | —         | Yes         | Yes       | Yes                    |
| CS 3130| —         | —           | Yes       | Yes         | Yes       | Yes                    |
| CS 3140| —         | —           | Yes       | Yes         | Yes       | Yes                    |
| CS 3240| Yes       | Yes         | Yes       | Yes         | Changed\* | Changed\*              |
| CS 4457| Yes       | Yes         | Yes       | Yes         | Yes       | Changed\*              |

| Course | Fall 2021 | Spring 2022 | Fall 2022 | Spring 2023 | Fall 2023 | Spring 2024 and beyond |
|:-------|:---------:|:-----------:|:---------:|:-----------:|:---------:|:----------------------:|
| CS 2102| CS 2120   | CS 2120     | CS 2120   | CS 2120     | CS 2120   | CS 2120                |
| CS 2110| Yes       | —           | —         | —           | —         | —                      |
| CS 2150| Yes       | Yes         | —         | —           | —         | —                      |
| CS 2330| Yes       | Yes         | ECE 2330  | ECE 2330    | ECE 2330  | ECE 2330               |
| CS 3102| Yes       | Yes         | Yes       | Yes         | CS 3120†  | CS 3120†               |
| CS 3240| Yes       | Yes         | Yes       | Yes         | Changed\* | Changed\*              |
| CS 3330| Yes       | Yes         | Yes       | Yes         | Changed\* | Changed\*              |
| CS 4102| Yes       | Yes         | CS 3100   | CS 3100     | CS 3100   | CS 3100                |
| CS 4414| Yes       | Yes         | Yes       | Yes         | Yes       | Changed\*              |
| CS 4457| Yes       | Yes         | Yes       | Yes         | Yes       | Changed\*              |


\* Adds a prereq and changes content

† Has extra prereqs compared to the course it replaces




# Q&A

- **Which courses should I take?**

    Whichever are offered when you are ready for your second CS course.
    In practice, this generally means that if you take CS 2100, you use the new courses;
    if you take CS 2110, you use the old courses.

- **I'm in a degree program not listed here. How will this effect me?**

    We haven't had official word from other degree programs yet.
    When we do, we'll add it here.

- **I took some of the old courses, then took a year off and now the rest of the old courses are not offered. What do I do?**

    You'll need an individual plan to help your situation.
    Please contact your academic advisor in CS, who can put you in touch with the current curriculum change coordinator.

- **I took some of the old courses and some of the new courses before I saw this. What do I do?**

    Generally, you'll need to pick one or the other to complete the degree.
    Please contact your academic advisor in CS to help decide which one to complete.
