from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from .models import TodoListItem


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.add_item_url = reverse('add_item')
        self.update_item_url = reverse('update_item', args=[10])
        self.delete_item_url = reverse('delete', args=[10])
        self.item1 = TodoListItem.objects.create(
            id=10,
            title='Buy milk',
            created=datetime.now(),
            complete=False
        )

    def test_todo_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todolist.html')

    def test_add_item(self):
        item = {
             'id': 1,
            'title': 'Finish DevOps project',
            'created': datetime.now(),
            'complete': False
        }
        response = self.client.post(self.add_item_url, item)
        item1 = TodoListItem.objects.get(id=1)
        self.assertEqual(item1.title, 'Finish DevOps project')
        self.assertEqual(response.status_code, 302)

    def test_update_item_GET(self):
        response = self.client.get(self.update_item_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_todolist.html')

    def test_update_item_POST(self):
        item = {
            'title': 'Buy milk and eggs',
            'complete': False
        }
        response = self.client.post(self.update_item_url, item)
        self.assertEqual(response.status_code, 302)
        item2 = TodoListItem.objects.get(id=10)
        self.assertEqual(item2.title, 'Buy milk and eggs')

    def test_delete_item_GET(self):
        response = self.client.get(self.delete_item_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')

    def test_delete_item_POST(self):
        response = self.client.post(self.delete_item_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(TodoListItem.objects.filter(id=10).exists())

