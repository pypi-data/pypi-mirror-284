from .all_courses import AllCoursesQueryData, DEFINITION as ALL_COURSES_QUERY
from .canvas_course_data import (
    Term,
    Assignment,
    AssignmentConnection,
    AssignmentGroup,
    AssignmentGroupConnection,
    ModuleItemInterface,
    File,
    Page,
    ModuleItem,
    Module,
    ModuleConnection,
    CanvasCourseData as Course,
    DEFINITION as COURSE_DATA_FRAGMENT,
)
from .course_mail import (
    CourseMailQueryData,
    ConversationParticipant,
    DEFINITION as COURSE_MAIL_QUERY,
)
from .single_course import SingleCourseQueryData, DEFINITION as SINGLE_COURSE_QUERY
