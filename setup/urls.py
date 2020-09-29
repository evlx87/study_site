from setup.views import main_view, create_course, create_category

URLS = {
    '/': main_view,
    '/create-course/': create_course,
    '/create-category/': create_category
}
