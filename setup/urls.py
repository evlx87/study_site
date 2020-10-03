from setup.views import main_view, create_course, CategoryListView, CategoryCreateView, StudentListView, \
    StudentCreateView, AddStudentByCourseCreateView

URLS = {
    '/': main_view,
    '/category-list/': CategoryListView(),
    '/student-list/': StudentListView(),

    '/create-course/': create_course,
    '/create-category/': CategoryCreateView(),
    '/create-student/': StudentCreateView(),

    '/add-student/': AddStudentByCourseCreateView(),
}
