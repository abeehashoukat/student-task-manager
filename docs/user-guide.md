# User Guide

## Starting the app
Run `python main.py` in the project folder.

## Menu options
- **1. Add**: type a title and press Enter. Empty titles are rejected.
- **2. Show**: lists all tasks. `[x]` means completed.
- **3. Mark complete**: enter the id of a task.
- **4. Delete**: enter the id of a task to remove it.
- **5. Exit**: closes the app.

## Example session
1. Choose 1, type `Study for exam`.
2. Choose 2 to see `1. [ ] Study for exam`.
3. Choose 3, enter `1`, then choose 2 to see `1. [x] Study for exam`.
4. Choose 4, enter `1` to delete it.

## Errors
If you enter an id that doesn't exist, the app shows an error message and keeps running.