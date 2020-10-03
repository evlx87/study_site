from setup.views import main_view, create_course, create_category, list_category

URLS = {
    '/': main_view,
    '/category-list/': list_category,
    '/create-course/': create_course,
    '/create-category/': create_category,
}
