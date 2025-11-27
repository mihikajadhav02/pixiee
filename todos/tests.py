from django.test import TestCase
from django.urls import reverse
from .models import Todo
from datetime import date

class TodoModelTest(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(
            title="Test Task",
            description="Test Description",
            due_date=date(2023, 12, 31),
            is_resolved=False
        )

    def test_todo_creation(self):
        self.assertTrue(isinstance(self.todo, Todo))
        self.assertEqual(self.todo.__str__(), self.todo.title)
        self.assertEqual(self.todo.title, "Test Task")

class TodoViewTest(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(
            title="View Test Task",
            description="Testing Views",
            is_resolved=False
        )

    def test_todo_list_view(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Task")
        self.assertTemplateUsed(response, 'todos/todo_list.html')

    def test_todo_create_view(self):
        response = self.client.post(reverse('todo_create'), {
            'title': 'New Task',
            'description': 'New Description',
            'is_resolved': False
        })
        self.assertEqual(response.status_code, 302) # Redirects after success
        self.assertEqual(Todo.objects.last().title, 'New Task')

    def test_todo_update_view(self):
        response = self.client.post(reverse('todo_update', args=[self.todo.pk]), {
            'title': 'Updated Task',
            'description': 'Testing Views',
            'is_resolved': True
        })
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Task')
        self.assertTrue(self.todo.is_resolved)

    def test_todo_delete_view(self):
        response = self.client.post(reverse('todo_delete', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 0)
