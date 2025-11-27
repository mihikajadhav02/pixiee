# Building Pixiee: A Retro Todo App with Django and AI Assistance

![Pixiee mascot bouncing cheerfully](https://github.com/mihikajadhav02/pixiee/blob/main/todos/static/todos/images/mascot.png?raw=true)

*How I built a charming, pixel-art todo application in one evening using AI tools — and what's next for this little project.*

---

## The Beginning: A Homework Assignment That Sparked Joy

It started as a simple homework assignment for the [AI Dev Tools Zoomcamp 2025](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/) by DataTalks.Club. The task? Build a Django todo application using AI assistance. The requirements were straightforward:

- Create, edit, and delete todos
- Assign due dates
- Mark tasks as resolved

But somewhere between "create a basic CRUD app" and "make it functional," I thought: *Why not make it cute?*

And that's how **Pixiee** was born.

## The Design Philosophy: Nostalgia Meets Functionality

I've always had a soft spot for retro gaming aesthetics. There's something about chunky pixels, bold borders, and vibrant color palettes that feels both nostalgic and timeless. So instead of building yet another minimalist todo app with rounded corners and subtle shadows, I decided to embrace the pixel art aesthetic wholeheartedly.

### Key Design Decisions

**1. Pixel-Perfect Typography**
I chose two Google Fonts that perfectly capture the retro vibe:
- **Press Start 2P** for headers — that classic arcade game feel
- **VT323** for body text — reminiscent of old terminal displays

**2. A Curated Color Palette**
Instead of generic primary colors, I went with:
- Soft cream background (#fdf6e3) for easy on the eyes
- Cute pink (#ff6b6b) for primary actions
- Teal (#4ecdc4) for secondary elements
- Sunny yellow (#ffe66d) as an accent
- Deep charcoal (#2b2b2b) for borders and text

**3. Custom Pixel Art Icons**
Rather than using a standard icon library, I created (well, had help creating) custom pixelated icons for:
- Adding new tasks (plus icon)
- Editing tasks (pencil icon)
- Deleting tasks (trash icon)
- Completed tasks (checkmark icon)

All rendered with `image-rendering: pixelated` to maintain that crisp, retro look.

**4. The Bouncing Mascot**
Every good app needs a mascot, right? Pixiee features an adorable character that gently bounces up and down using CSS animations. It's a small touch, but it makes the app feel alive and welcoming.

```css
@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

.mascot-bounce {
    animation: bounce 2s infinite ease-in-out;
}
```

## The Development Process: AI as a Pair Programming Partner

This project was built entirely with AI assistance (specifically, using Antigravity by Google DeepMind). Here's what that looked like in practice:

### What Worked Really Well

**1. Rapid Prototyping**
I could describe what I wanted ("make it pixelated with retro vibes") and get immediate implementation suggestions. The AI understood the aesthetic direction and helped translate it into code.

**2. Learning by Doing**
I had zero Django experience before this project. The AI acted as both a teacher and a coding partner, explaining concepts while implementing them. Within hours, I understood:
- Django's MVT (Model-View-Template) architecture
- Class-based views
- Template inheritance
- Static file management
- Testing in Django

**3. Iterative Refinement**
The back-and-forth was incredibly natural:
- "Make the icons bigger"
- "Reduce the spacing around the mascot"
- "Add a bounce animation"

Each request was understood and implemented correctly.

### The Technical Stack

- **Backend**: Django 5.2.8
- **Database**: SQLite3 (perfect for a small project)
- **Package Manager**: uv (blazingly fast!)
- **Styling**: Vanilla CSS (no frameworks needed)
- **Testing**: Django's built-in test framework

## Key Features Under the Hood

### 1. Clean Model Design
```python
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

Simple, but effective. Everything a todo needs, nothing it doesn't.

### 2. Class-Based Views
Using Django's generic views made CRUD operations incredibly clean:
- `ListView` for displaying all todos
- `CreateView` for adding new tasks
- `UpdateView` for editing
- `DeleteView` for removal

### 3. Comprehensive Testing
Five test cases covering:
- Model creation and string representation
- List view rendering
- Create, update, and delete operations

All passing! ✅

## Challenges and Learning Moments

### Challenge 1: Static Files
Getting Django to properly serve static files (images, CSS) required understanding the `STATIC_URL` setting and using the `{% static %}` template tag. Small detail, but crucial for the pixel art to display correctly.

### Challenge 2: Template Inheritance
Learning how to structure templates with a base layout and content blocks took some iteration, but once it clicked, it made the codebase so much cleaner.

### Challenge 3: CSS in Django Templates
The linter didn't love inline CSS with Django template tags, but it renders perfectly in the browser. Sometimes you have to trust the output over the warnings!

## What I Learned

1. **AI tools are incredible for learning new frameworks** — I went from zero Django knowledge to a working app in hours
2. **Design matters** — A cute aesthetic makes even a simple todo app feel special
3. **Small animations make a big difference** — That bouncing mascot brings so much personality
4. **Testing is easier than you think** — Django's test framework is straightforward and gives you confidence
5. **Learning in public is powerful** — Sharing this journey helps solidify my understanding

## Future Plans: Where Pixiee Goes Next

This is just version 1.0. Here's what I'm thinking for future iterations:

### Short-term Goals (Next Few Weeks)

**1. User Authentication**
Right now, Pixiee is single-user. Adding Django's built-in authentication (or maybe even Google OAuth for that social login convenience) would make it multi-user ready.

**2. Task Categories/Tags**
Being able to organize tasks by project or category would add a lot of utility. Imagine color-coded pixel badges for different categories!

**3. Priority Levels**
Not all tasks are created equal. Adding priority levels (High, Medium, Low) with different visual indicators would help with task management.

**4. Dark Mode Toggle**
A pixel-art dark mode with neon colors? Yes, please! This would be both functional and aesthetically pleasing.

### Medium-term Goals (Next Few Months)

**5. Recurring Tasks**
For those daily/weekly todos that keep coming back. This would require some interesting database design for recurrence patterns.

**6. Task Filtering and Sorting**
- Filter by completion status
- Sort by due date, priority, or creation date
- Search functionality

**7. Drag-and-Drop Reordering**
Manual task ordering with a smooth drag-and-drop interface. This would be a fun JavaScript challenge!

**8. Statistics Dashboard**
A pixel-art dashboard showing:
- Tasks completed this week/month
- Productivity streaks
- Most productive days
- Overdue task warnings

### Long-term Vision (6+ Months)

**9. Mobile App**
A React Native or Flutter version with the same pixel aesthetic. Imagine Pixiee in your pocket!

**10. Collaboration Features**
- Share task lists with friends/team
- Assign tasks to others
- Comments and attachments

**11. Gamification**
- Earn pixel coins for completing tasks
- Unlock new mascot outfits
- Achievement badges
- Level up system

**12. API Development**
Build a REST API so others can build their own Pixiee clients or integrations.

**13. Pomodoro Timer Integration**
Built-in focus timer with pixel art animations. Work sessions could earn you rewards!

**14. AI-Powered Features**
- Smart task suggestions based on patterns
- Automatic due date recommendations
- Task breakdown for large projects
- Natural language task input ("Remind me to call mom tomorrow at 3pm")

## Why This Matters

In a world of sleek, minimalist productivity apps, Pixiee is a reminder that software can be both functional *and* fun. It doesn't have to choose between utility and personality.

More importantly, this project demonstrates the power of AI-assisted development for learning. I went from knowing nothing about Django to having a fully functional, tested, and deployed web application in a single evening. That's remarkable.

## Try It Yourself!

The entire project is open source and available on GitHub:
👉 [github.com/mihikajadhav02/pixiee](https://github.com/mihikajadhav02/pixiee)

Whether you want to:
- Learn Django
- Experiment with pixel art design
- Fork it and make it your own
- Contribute new features

You're welcome to dive in!

## Final Thoughts

Building Pixiee taught me that the best projects often come from adding a personal touch to simple requirements. What started as "build a basic todo app" became an exercise in design, nostalgia, and making technology feel more human.

The bouncing mascot isn't just decoration — it's a reminder that our tools should bring us joy, not just productivity.

So here's to Pixiee, to learning in public, to AI-assisted development, and to making the web a little more colorful, one pixel at a time.

---

**What would you add to Pixiee?** Drop your ideas in the comments! And if you build something with it, I'd love to see what you create.

*Keep questing, keep completing!* 🎮✨

---

*This project was created as part of the AI Dev Tools Zoomcamp 2025 by DataTalks.Club. Special thanks to the community for the inspiration and support!*

**Connect with me:**
- GitHub: [@mihikajadhav02](https://github.com/mihikajadhav02)
- Project Repo: [Pixiee](https://github.com/mihikajadhav02/pixiee)

#Django #WebDevelopment #AIAssistedDevelopment #PixelArt #TodoApp #LearningInPublic #Python
