# ⚙️ Algorithmic Complexity, Randomized Algorithms & Greedy Scheduling

## 📘 Homework: goit-algo2-hw-11

This project contains two independent tasks:

1. **Task 1** — Performance comparison of **randomized vs deterministic QuickSort**
2. **Task 2** — Class scheduling using a **greedy algorithm**

---

## 🧠 Task 1: Randomized vs Deterministic QuickSort

### 📌 Goal

Compare the execution time of two sorting approaches on large arrays:

- `randomized_quick_sort(arr)` — uses a random pivot
- `deterministic_quick_sort(arr)` — uses a fixed pivot (first, last, or middle)

### 🛠 Implementation Requirements

- Create arrays of size: `10_000`, `50_000`, `100_000`, `500_000`
- Fill them with random integers
- Run each algorithm 5 times on each array
- Record the average time using `timeit`
- Output comparison as:
  - 📄 Formatted table in terminal
  - 📊 Graph with labeled axes and legend

### ✅ Example Output

```
Розмір масиву: 10000
   Рандомізований QuickSort: 0.0189 секунд
   Детермінований QuickSort: 0.0189 секунд
...
```

📈 Example graph:

- Title: `Порівняння часу сортування QuickSort`
- X-axis: Array size
- Y-axis: Time in seconds
- Two lines: Randomized and Deterministic

---

## 🧩 Task 2: Class Schedule Using Greedy Algorithm

### 📌 Goal

Assign the **minimum number of teachers** to cover all university subjects using a greedy algorithm.

### 📚 Given Subjects

```
{'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
```

### 👩‍🏫 Teachers

Each teacher has:

- First name, last name, age, email
- A set of subjects they can teach

### ✅ Requirements

- Implement class `Teacher` with the listed attributes
- Implement function:
  ```python
  def create_schedule(subjects: Set[str], teachers: List[Teacher]) -> List[Teacher]
  ```
- Use greedy logic:

  - Prefer teachers who can cover the most **remaining** uncovered subjects
  - If tie, prefer **younger teacher**

- If not all subjects can be covered, output:
  ```
  Неможливо покрити всі предмети наявними викладачами.
  ```

### ✅ Example Output (Terminal)

```
Розклад занять:
Сергій Коваленко, 50 років, email: s.kovalenko@example.com
   Викладає предмети: Інформатика, Математика

Наталія Шевченко, 29 років, email: n.shevchenko@example.com
   Викладає предмети: Хімія, Біологія

Дмитро Бондаренко, 35 років, email: d.bondarenko@example.com
   Викладає предмети: Фізика
```

---

## 📂 Project Structure

```
goit-algo2-hw-11/
├── quicksort_comparison.py          # Task 1
├── greedy_schedule.py               # Task 2
├── README.md
```

---

## 🛠 Run Instructions

```bash
python quicksort_comparison.py
python greedy_schedule.py
```
