# 📚 Homework 5 — REST API + MCP Meals Server

**Author:** Anushka Rajesh Khadatkar (018383963)

A two-part project: a full-stack **Books & Authors REST API** with Redux frontend (Part 1), and a **Claude-connected MCP Meals Server** (Part 2).

---

## 📁 Repository Structure

```
homework-5/
│
├── README.md
│
├── part1-books-api/
│   ├── backend/
│   │   ├── main.py               # FastAPI app entry point
│   │   ├── models.py             # SQLAlchemy models (Author, Book)
│   │   ├── schemas.py            # Pydantic schemas
│   │   ├── database.py           # DB connection & session
│   │   ├── crud.py               # CRUD logic
│   │   └── requirements.txt
│   │
│   └── frontend/
│       ├── src/
│       │   ├── store/
│       │   │   ├── index.js
│       │   │   ├── authorsSlice.js
│       │   │   └── booksSlice.js
│       │   ├── components/
│       │   │   ├── AuthorList.jsx
│       │   │   ├── BookList.jsx
│       │   │   ├── CreateForm.jsx
│       │   │   └── UpdateForm.jsx
│       │   ├── App.jsx
│       │   └── main.jsx
│       ├── package.json
│       └── vite.config.js
│
├── part2-mcp-server/
│   ├── meals_server.py           # MCP server (main file)
│   ├── requirements.txt
│   └── screenshots/
│       ├── claude_connect.png
│       ├── mcp_server.png
│       ├── meal_by_id.png
│       ├── meal_by_ingredient.png
│       ├── meal_by_name.png
│       └── random_meal.png
│
└── .gitignore
```

---

## 🚀 Getting Started with GitHub Desktop

### 1. Clone the Repository
1. Open **GitHub Desktop**
2. Click **File → Clone Repository**
3. Paste your repo URL and choose a local path
4. Click **Clone**

### 2. Making Changes & Committing
1. Make edits to your files locally
2. Open **GitHub Desktop** — changed files appear automatically in the left panel
3. Write a **commit message** (e.g., `Add MCP server for meals`)
4. Click **Commit to main**
5. Click **Push origin** to sync to GitHub

### 3. Pushing New Screenshots
1. Drop new `.png` files into `part2-mcp-server/screenshots/`
2. GitHub Desktop will detect them automatically
3. Commit and push as above

---

## Part 1 — Books & Authors REST API

A FastAPI backend with a React + Redux frontend for managing Authors and Books.

### 🛠️ Backend Setup

```bash
cd part1-books-api/backend
pip install -r requirements.txt
uvicorn main:app --reload
```

API runs at: `http://localhost:8000`  
Swagger docs: `http://localhost:8000/docs`

### 🎨 Frontend Setup

```bash
cd part1-books-api/frontend
npm install
npm run dev
```

### 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/authors` | Create a new author |
| GET | `/authors` | List all authors |
| GET | `/authors/{id}` | Get author by ID |
| PUT | `/authors/{id}` | Update author |
| DELETE | `/authors/{id}` | Delete author |
| POST | `/books` | Create a new book |
| GET | `/books` | List all books |
| GET | `/books/{id}` | Get book by ID |
| PUT | `/books/{id}` | Update book |
| DELETE | `/books/{id}` | Delete book |
| GET | `/authors/{id}/books` | Get all books by an author |

### 🗄️ Database Design

**Author Table**

| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY |
| name | VARCHAR | NOT NULL |
| email | VARCHAR | UNIQUE, NOT NULL |
| bio | TEXT | |

**Books Table**

| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY |
| title | VARCHAR | NOT NULL |
| author_id | INTEGER | FOREIGN KEY → Author |
| genre | VARCHAR | |
| published_year | INTEGER | |

### ✅ Validation & Error Handling

- **422** — Invalid email format
- **404** — Resource not found (e.g., author_id = 99)
- **400** — Duplicate email constraint violation
- **400** — Cannot delete an author who has associated books

### 🔄 Redux Setup

The frontend uses Redux Toolkit for state management with separate slices for `authors` and `books`, handling async CRUD operations via `createAsyncThunk`.

---

## Part 2 — MCP Meals Server (Claude Integration)

An MCP (Model Context Protocol) server that connects to Claude and allows querying a meals database using natural language.

### 🛠️ Setup

```bash
cd part2-mcp-server
pip install -r requirements.txt
python meals_server.py
```

### 🔌 Connecting to Claude Desktop

1. Open **Claude Desktop → Settings → Developer**
2. Click **Edit Config** to open `claude_desktop_config.json`
3. Add the following:

```json
{
  "mcpServers": {
    "meals": {
      "command": "python",
      "args": ["/absolute/path/to/part2-mcp-server/meals_server.py"]
    }
  }
}
```

4. Restart Claude Desktop
5. The meals tools will appear in Claude's tool panel ✅

### 🧰 Available MCP Tools

| Tool | Description |
|------|-------------|
| `meal_by_name` | Search for meals by name |
| `meal_by_ingredient` | Find meals containing a specific ingredient |
| `meal_by_id` | Get full details of a meal by ID |
| `random_meal` | Fetch a random meal suggestion |

### 📸 Screenshots

#### MCP Server Running in Claude

![MCP Server](screenshots/mcp_server.png)

#### Claude Connected to Meals Server

![Claude Connect](screenshots/claude_connect.png)

#### Search Meals by Name

![Meal by Name](screenshots/meal_by_name.png)

#### Search by Ingredient

![Meal by Ingredient](screenshots/meal_by_ingredient.png)

#### Meal Details (by ID)

![Meal by ID](screenshots/meal_by_id.png)

#### Random Meal

![Random Meal](screenshots/random_meal.png)

---

## 📦 Dependencies

### Part 1 — Backend (`requirements.txt`)
```
fastapi
uvicorn
sqlalchemy
pydantic[email]
```

### Part 2 — MCP Server (`requirements.txt`)
```
mcp
httpx
```

---

## 📝 .gitignore

```
# Python
__pycache__/
*.pyc
venv/
.env

# Node
node_modules/
dist/
.DS_Store
```

---

*Homework 5 — Anushka Rajesh Khadatkar (018383963)*
