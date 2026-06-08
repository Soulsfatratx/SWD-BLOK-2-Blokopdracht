# SWD-BLOK-2-Blokopdracht — Workspace Intelligence

## Project Overview
Tetris game project built with pygame. Collaborative work across multiple files: board.py (game grid logic), tetromino.py (shapes/rotations), score.py (point counting), renderer.py (UI/styling), main.py (game loop).

## Stack
- Python 3.13
- pygame 2.6.1
- VS Code

## Current Status
renderer.py is being designed and planned. .intelligence folder initialized. .venv created with Python 3.13 and pygame installed.

---

## Session Log

### Session 2026-06-07
**What we did:**
- Initialized .intelligence folder for SWD-BLOK-2-Blokopdracht
- Documented renderer.py project targets and design specifications
- Created .venv with Python 3.13 and installed pygame 2.6.1

**What worked:**
- .venv creation with Python 3.13 (compatible with pygame wheels)
- pygame installation in dedicated venv

**What broke:**
- Terminal session retained odysseus .venv activation after folder removal
- pygame fails with Python 3.14 (distutils removed)

**Why it broke:**
- PowerShell retains activated venv path in terminal session
- Python 3.14 removed setuptools._distutils.msvccompiler required by pygame build

**How we fixed it:**
- Created dedicated .venv with Python 3.13
- Installed pygame 2.6.1-cp313 wheel

**Current known issues:**
- renderer.py implementation pending (design specs documented, no code changes yet)
- board.py grid format confirmed: 2D array of color strings

**Next steps:**
- Implement renderer.py functions based on design specs
- Test full game with all collaborators' files

---

## Renderer.py Project Targets

### Design Specifications
- **Style:** Modern clean (dark background, bright blocks, subtle borders)
- **Preview box:** Right side above board
- **Scoreboard:** Bottom-middle
- **Game over:** Overlay banner solid color rectangle in middle with score + "Game Over", rest of game blurred in background
- **Grid format:** board.py sends 2D array of color strings
- **Cell size:** CELL_SIZE variable (default 60, adjustable later)
- **Border:** Thin 1px border around each block
- **Background per level:** 6 levels with different colors

### Background Colors per Level
- Level 1: `#1a1a2e` (deep navy)
- Level 2: `#2d2d3e` (mid navy)
- Level 3: `#3e3e4f` (light navy)
- Level 4: `#4f4f60` (gray navy)
- Level 5: `#606071` (mid gray)
- Level 6: `#717182` (light gray)

### Functions to Implement
- `draw_board(screen, grid)` — render the game grid from board.py color strings
- `draw_block(screen, shape, x, y)` — render falling tetromino using COLORS from tetromino.py
- `draw_score(screen, score)` — render score at bottom-middle
- `draw_preview(screen, shape)` — render next piece preview box on right side above board
- `draw_game_over(screen, score)` — render game over overlay banner

### Data Structures
- `CELL_SIZE` — adjustable pixel size per cell (default 60)
- `columns = 10` — grid width
- `rows = 20` — grid height
- `width = CELL_SIZE * columns` — screen width
- `height = CELL_SIZE * rows` — screen height
- `LEVEL_COLORS` — dict mapping level to background hex color
- `BOARD_BORDER = 1` — 1px border per block

### Dependencies
- board.py → grid (2D array of color strings)
- tetromino.py → SHAPES, COLORS (for block rendering and preview)
- score.py → score value (for scoreboard)
- main.py → shape, x, y (current falling position), next_shape (preview)

---

## Patterns That Work
[Will be populated as solutions are discovered]

---

## Patterns That Break
[Will be populated as problems are identified]

---

## Dependencies & Versions
## Last updated: 2026-06-07

| Package | Version | Notes |
|---|---|---|
| pygame | 2.6.1 | Requires Python 3.13, no cp314 wheel available |
| Python | 3.13.8 | Used in SWD-BLOK-2-Blokopdracht .venv |

---

## File Structure Notes
- Each collaborator has own file: board.py, tetromino.py, score.py, renderer.py, main.py
- renderer.py receives data from board.py, tetromino.py, score.py, main.py
- CELL_SIZE is adjustable variable for pixel scaling
- Background colors change per level (6 levels defined)