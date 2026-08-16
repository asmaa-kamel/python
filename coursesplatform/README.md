# Courses Platform - Course Management System

A full-featured Course Management Platform built from scratch using **Django**, designed to manage courses, instructors, students, and course enrollments with secure authentication and modern UI styling.

---

## Features Overview

### Course Management
* **Course Catalog:** View all available courses along with instructors and enrolled student counts.
* **Course Details:** Detailed view for each course showing description, instructor information, and student lists.
* **Search & Filter:** Instant search by course title and filtering courses by instructor.

### Student & Enrollment Flow
* **Student Registration:** Automatic creation and one-to-one linking of a `Student` profile upon user sign-up.
* **Course Enrollment:** Logged-in students can easily enroll in available courses.
* **Manage Enrollments:** Edit completion status or cancel/remove enrollments.
* **Student Dashboard / Profile:** Personal profile page displaying student info and all enrolled courses with completion badges.

### Authentication & Route Protection
* Full user authentication cycle (Sign Up, Log In, Log Out).
* Protected views using `@login_required` to restrict enrollment actions and profile access to logged-in users only.
* Dynamic navigation bar adapting to guest/authenticated states with user greeting.

### Admin Management
* Full Django Admin integration for managing `Instructors`, `Courses`, `Students`, and `Enrollments`.

---

## Database Architecture

* **`User` (Built-in Django):** Authentication & credentials.
* **`Student`:** Linked via `OneToOneField` to `User` for extra profile details.
* **`Instructor`:** Stores instructor descriptive information (managed via Admin).
* **`Course`:** Associated with an `Instructor` via `ForeignKey` (One-to-Many).
* **`Enrollment`:** Intermediary relation connecting `Student` and `Course` (Many-to-Many) with extra metadata (`date_enrolled`, `is_completed`).

---

## Tech Stack

* **Backend:** Python, Django
* **Database:** SQLite3
* **Frontend:** Django Templates, HTML5, CSS3
* **Forms & Validation:** Django ModelForms, CSRF Protection, Django Widget Tweaks

