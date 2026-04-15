# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run the app (from project root)
PYTHONPATH=src python3 src/main.py

# Run all tests (from project root)
PYTHONPATH=. python3 -m pytest

# Run a single test
PYTHONPATH=. python3 -m pytest tests/test_recommender.py::test_recommend_returns_top_k_sorted

# Install dependencies
pip3 install -r requirements.txt
```

## Architecture

This is a content-based music recommender simulation for classroom learning. The codebase offers two parallel interfaces for the same logic:

**Functional interface** (dict-based): `load_songs()` → `score_song()` → `recommend_songs()` — used by `src/main.py` as the primary entry point. Songs and user preferences are plain dicts.

**OOP interface** (dataclass-based): `Recommender` class with `recommend()` and `explain_recommendation()` — uses `Song` and `UserProfile` dataclasses. Used by the test suite.

Both live in `src/recommender.py`. The functional path is what `main.py` calls; the OOP path is what `tests/test_recommender.py` validates. Implementations must keep both in sync.

**Data flow**: CSV (`data/songs.csv`, 10 songs) → `load_songs()` parses with pandas → `score_song()` computes weighted proximity score per song → `recommend_songs()` sorts and returns top k with explanations.

**Scoring approach**: Content-based filtering using weighted proximity. Categorical features (genre, mood) use exact match. Numerical features (energy, acousticness, tempo, valence, danceability) use `1 - abs(song_value - user_target)` for proximity scoring.

## Key Files

- `src/recommender.py` — All recommendation logic: dataclasses, scoring, ranking, explanations
- `src/main.py` — CLI entry point demonstrating the functional interface
- `data/songs.csv` — Song catalog (10 songs, 10 columns including genre, mood, energy, tempo_bpm, valence, danceability, acousticness)
- `tests/test_recommender.py` — Tests the OOP `Recommender` class (sorted results, explanation strings)
