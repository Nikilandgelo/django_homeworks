import pytest
from model_bakery import baker
from students.models import Course
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.fixture
def creating_courses():
    def create(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return create

@pytest.fixture
def abstract_user() -> APIClient:
    return APIClient()


@pytest.mark.parametrize(
    'course_name',
    [
        'Test_course',
        'Course_for_professionals',
        'Best_course_of_all_time'
    ]
)
@pytest.mark.django_db
def test_get_course(creating_courses, abstract_user: APIClient, course_name: str):
    course:list = creating_courses(_quantity = 1, name=course_name)

    response = abstract_user.get(reverse("courses-detail", kwargs={'pk': course[0].id}))
    
    assert response.status_code == 200
    assert response.data.get('name') == course_name

@pytest.mark.django_db
def test_get_many_courses(creating_courses, abstract_user: APIClient):
    courses:list = creating_courses(_quantity = 10)

    response = abstract_user.get(reverse("courses-list"))

    assert response.status_code == 200
    assert len(response.data) == len(courses)

@pytest.mark.django_db
def test_filter_id_course(creating_courses, abstract_user: APIClient):
    course:list = creating_courses(_quantity = 1)
    
    response = abstract_user.get(f'{reverse("courses-list")}?id={course[0].id}')

    assert response.status_code == 200
    assert len(response.data) == len(course)

@pytest.mark.parametrize(
    'course_name',
    [
        'Course_with_filter',
        'Filtered_course'
    ]
)
@pytest.mark.django_db
def test_filter_name_course(creating_courses, abstract_user: APIClient, course_name: str):
    course:list = creating_courses(_quantity = 1, name = course_name)
    
    response = abstract_user.get(f'{reverse("courses-list")}?name={course[0].name}')

    assert response.status_code == 200
    assert response.data[0].get("name") == course_name

@pytest.mark.django_db
def test_create_course(abstract_user: APIClient):
    
    response = abstract_user.post(reverse("courses-list"), data = {'name': 'New_course'})

    assert response.status_code == 201
    assert response.data.get("name") == 'New_course'

@pytest.mark.django_db
def test_update_course(creating_courses, abstract_user: APIClient):
    course:list = creating_courses(_quantity = 1)

    response = abstract_user.patch(reverse("courses-detail", kwargs={'pk': course[0].id}), data={'name': 'updated_name'})

    assert response.status_code == 200
    assert response.data.get("name") == 'updated_name'

@pytest.mark.django_db
def test_delete_course(creating_courses, abstract_user: APIClient):
    course:list = creating_courses(_quantity = 1)

    response = abstract_user.delete(reverse("courses-detail", kwargs={'pk': course[0].id}))

    assert response.status_code == 204