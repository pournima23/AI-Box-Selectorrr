# AI-Assisted Box Selection System

## About the Project

This project was developed as part of a Django hiring assignment.

The objective of the application is to recommend the most suitable shipping box for a product based on its dimensions and weight. Instead of selecting a box manually, the system compares the product with all available shipping boxes and recommends the most appropriate one.

The application also displays the estimated shipping cost of the recommended box.

---

## Features

- Add and manage products using Django Admin.
- Store multiple shipping boxes with their dimensions, weight capacity and cost.
- Recommend the best shipping box for a selected product.
- Display the recommended box and shipping cost.
- Simple and responsive user interface built using Bootstrap.
- SQLite database for storing project data.

---

## Technologies Used

- Python 3
- Django
- SQLite
- HTML5
- Bootstrap 5
- Git
- GitHub

---

## Project Workflow

1. Open the home page.
2. View the list of available products.
3. Click the **Recommend Box** button.
4. The system checks every available shipping box.
5. It compares:
   - Product Length
   - Product Width
   - Product Height
   - Product Weight
6. Boxes that cannot fit the product are ignored.
7. From the remaining boxes, the system recommends a suitable shipping box.
8. The recommendation page displays:
   - Product Name
   - Recommended Box
   - Shipping Cost

---

## Project Structure

```
AI-Box-Selectorrr/
│
├── api/
│   ├── migrations/
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── box_selector/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── db.sqlite3
└── README.md
```

---

## How to Run the Project

Clone the repository

```bash
git clone https://github.com/pournima23/AI-Box-Selectorrr.git
```

Go to the project directory

```bash
cd AI-Box-Selectorrr
```

Install Django

```bash
pip install django
```

Run database migrations

```bash
python manage.py migrate
```

Start the development server

```bash
python manage.py runserver
```

Open your browser and visit

```
http://127.0.0.1:8000/
```

---

## Sample Output

- Home page displays all available products.
- Clicking **Recommend Box** opens the recommendation page.
- The recommended shipping box and its shipping cost are displayed.

---

## Future Improvements

- Support multiple products in a single order.
- Improve packing logic using AI-based optimization.
- Provide REST APIs.
- Deploy the application on a cloud platform.

---

## Author
**Pournima Mali**