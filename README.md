# 🎮 Pixiee - A Cute Pixelated Todo App

![Pixiee](todos/static/todos/images/mascot.png)

A charming, retro-styled todo application built with Django, featuring a pixelated aesthetic and an adorable bouncing mascot!

## ✨ Features

- ✅ **Create, Edit, and Delete Tasks** - Full CRUD functionality for managing your todos
- 📅 **Due Dates** - Assign deadlines to keep yourself on track
- ✓ **Mark as Resolved** - Check off completed tasks with satisfaction
- 🎨 **Pixel Art Design** - Retro gaming vibes with custom pixelated icons
- 🎭 **Animated Mascot** - A bouncing companion to keep you company
- 🎯 **Clean UI** - Simple, intuitive interface with chunky borders and vibrant colors

## 🛠️ Tech Stack

- **Backend**: Django 5.2.8
- **Database**: SQLite3
- **Styling**: Vanilla CSS with pixel-perfect design
- **Fonts**: Press Start 2P & VT323 (Google Fonts)
- **Package Manager**: uv

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- uv (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mihikajadhav02/pixiee.git
   cd pixiee
   ```

2. **Create a virtual environment**
   ```bash
   uv venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   uv pip install django --python venv
   ```

4. **Run migrations**
   ```bash
   ./venv/bin/python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   ./venv/bin/python manage.py runserver
   ```

6. **Open your browser**
   Navigate to `http://127.0.0.1:8000/` and start managing your tasks!

## 🧪 Running Tests

```bash
./venv/bin/python manage.py test
```

All tests should pass with 5 test cases covering:
- Todo model creation
- List view functionality
- Create, update, and delete operations

## 📁 Project Structure

```
pixiee/
├── todo_project/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todos/                 # Todo app
│   ├── models.py         # Todo model
│   ├── views.py          # Class-based views
│   ├── urls.py           # URL routing
│   ├── tests.py          # Test cases
│   ├── static/           # Static files
│   │   └── todos/images/ # Pixelated icons & mascot
│   └── templates/        # HTML templates
│       └── todos/
│           ├── base.html
│           ├── todo_list.html
│           ├── todo_form.html
│           └── todo_confirm_delete.html
├── manage.py
└── db.sqlite3
```

## 🎨 Design Philosophy

Pixiee embraces a nostalgic pixel art aesthetic inspired by retro games:

- **Chunky Borders**: Bold 4px borders for that classic pixel look
- **Vibrant Colors**: Carefully curated palette (pink, teal, yellow, cream)
- **Pixel Fonts**: Press Start 2P for headers, VT323 for body text
- **Smooth Animations**: Bouncing mascot and button press effects
- **Image Rendering**: `image-rendering: pixelated` for crisp pixel art

## 📝 Usage

### Creating a Task
1. Click the "New Task" button with the pixelated plus icon
2. Fill in the title, description (optional), and due date (optional)
3. Click "Save Quest" to add it to your list

### Editing a Task
1. Click the edit icon (pencil) next to any task
2. Modify the details
3. Save your changes

### Completing a Task
1. Edit the task
2. Check the "Mark as Completed?" checkbox
3. The task will appear with a checkmark and strikethrough

### Deleting a Task
1. Click the delete icon (trash) next to any task
2. Confirm the deletion

## 🎓 About This Project

This project was created as part of the **AI Dev Tools Zoomcamp 2025** by DataTalks.Club. It demonstrates:

- Building a Django application with AI assistance
- Implementing CRUD operations
- Creating a custom UI design
- Writing comprehensive tests
- Following best practices in web development

## 🤝 Contributing

Feel free to fork this project and make it your own! Some ideas for enhancements:

- Add user authentication
- Implement task categories/tags
- Add priority levels
- Create a dark mode toggle
- Add task filtering and sorting
- Implement drag-and-drop reordering

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **DataTalks.Club** for the AI Dev Tools Zoomcamp
- **Google Fonts** for the retro pixel fonts
- **Django** for the amazing web framework

---

Made with 💖 and pixels by [Mihika Jadhav](https://github.com/mihikajadhav02)

*Keep questing, keep completing! 🎮✨*
