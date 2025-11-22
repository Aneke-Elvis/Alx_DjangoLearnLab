📚 Django Advanced Model RelationshipsThis project, named django-models, focuses on mastering the Object-Relational Mapper (ORM) in Django by implementing and querying complex model relationships: ForeignKey, ManyToMany, and OneToOne.

🎯 ObjectiveThe goal of this task was to model a simple library system to demonstrate the three core relationship types and provide clear query samples for each.

⚙️ Project StructureThe core logic is contained within the relationship_app.django-models/
├── LibraryProject/          # Main project configuration
│   └── relationship_app/    # The new application
│       ├── models.py        # Model definitions
│       └── query_samples.py # Script for demonstrating queries
└── manage.py

📖 Model Relationships DefinedThe following models were defined in relationship_app/models.py to showcase the relationships:ModelRelationshipDescriptionBookForeignKey to AuthorOne Author can write Many Books.LibraryManyToManyField to BookMany Books can be in Many Libraries.LibrarianOneToOneField to LibraryOne Librarian is assigned to One Library.

🚀 Setup and ExecutionTo set up and run the sample queries:Activate Virtual Environment:Bashsource venv/bin/activate  # macOS/Linux
venv\Scripts\activate.bat # Windows CMD
Apply Migrations:(Ensure models are correctly defined before running)Bashpython manage.py makemigrations relationship_app
python manage.py migrate
Run Sample Queries Script:This script initializes sample data and executes the required queries against the database. Run this command from the django-models directory:Bashpython LibraryProject/relationship_app/query_samples.py

✅ Query Examples ImplementedThe query_samples.py script demonstrates the following ORM operations:Query all books by a specific author (ForeignKey reverse lookup).List all books available in a specific library (ManyToManyField lookup).Retrieve the librarian assigned to a specific library (OneToOneField reverse lookup).

# Django Security Enhancements

## 1. Secure Settings

The following settings were applied in `settings.py`:

- `DEBUG = False` – disable debug in production
- `SECURE_BROWSER_XSS_FILTER = True` – activates XSS protection
- `X_FRAME_OPTIONS = "DENY"` – prevents clickjacking
- `SECURE_CONTENT_TYPE_NOSNIFF = True` – disables content sniffing
- `SESSION_COOKIE_SECURE = True` – cookies sent only via HTTPS
- `CSRF_COOKIE_SECURE = True` – CSRF cookie secured
- `SECURE_HSTS_SECONDS` – enables HTTP Strict Transport Security
- Content Security Policy added via `django-csp` middleware

## 2. CSRF Protection

All forms now include:

```html
{% csrf_token %}
