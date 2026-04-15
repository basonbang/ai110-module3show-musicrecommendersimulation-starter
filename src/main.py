"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\n{'=' * 50}")
    print(f"  Top {len(recommendations)} Recommendations for: {user_prefs.get('genre', '?')} / {user_prefs.get('mood', '?')}")
    print(f"{'=' * 50}\n")

    for rank, (song, score, explanation) in enumerate(recommendations, 1):
        reasons = explanation.split(" | ")
        print(f"  #{rank}  {song['title']} by {song['artist']}")
        print(f"       Score: {score:.2f}")
        for reason in reasons:
            print(f"         - {reason}")
        print()


if __name__ == "__main__":
    main()
