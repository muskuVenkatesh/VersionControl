
---

## 🌱 Branching Strategy

### 1️⃣ Initial Setup
- Created a GitHub repository
- Cloned using SSH
- Created a branch named after username: `Tutedude`
- Added Flask project files
- Merged `Tutedude` → `main`

---

### 2️⃣ API JSON Update
- Created branch: `Tutedude_new`
- Updated JSON file used in `/api` route
- Merged `Tutedude_new` → `main`
- Resolved merge conflicts by accepting `Tutedude_new` changes

---

### 3️⃣ Feature Branches
- Created branches:
  - `master_1` → Frontend development
  - `master_2` → Backend API development

#### 🖥️ master_1 (Frontend)
- Created To-Do page
- Form fields:
  - Item Name
  - Item Description

#### 🔧 master_2 (Backend)
- Created `/submittodoitem` route
- Accepts POST data:
  - itemName
  - itemDescription
- Stores data in MongoDB

✔ Both branches were merged into `main`

---

## 🧩 Sequential Commits (master_1)

Enhancements made **one field per commit**:
1. Added Item ID field
2. Added Item UUID field
3. Added Item Hash field

Each change was committed separately to maintain clean history.

---

## ⏪ Git Reset & Rebase

### 🔹 Git Reset
- Used `git reset --soft` on `main`
- Rolled back to commit with **only Item ID**
- Re-committed the state

### 🔹 Git Rebase
- Rebased `master_1` onto `main`
- Preserved individual commits (no squashing)
- Resolved conflicts manually
- Force-pushed rebased branch as required

Commands used:
```bash
git rebase origin/main
git rebase --continue
git push origin master_1 --force-with-lease
