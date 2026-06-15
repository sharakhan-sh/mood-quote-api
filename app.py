from fastapi import FastAPI

app = FastAPI()

mood_quotes = {
    "happy": "Keep shining. Your energy can light up someone's day ✨",

    "sad": "Storms don't last forever. Better days are coming 🌈",

    "tired": "Rest is not quitting. Even champions recover 🔋",

    "motivated": "Small steps every day create massive success 🚀",

    "angry": "Control your emotions before they control your decisions 🧠"
}

@app.get("/")
def home():
    return {
        "available_moods": list(mood_quotes.keys())
    }

@app.get("/mood/{mood}")
def mood_check(mood):

    mood = mood.lower()

    if mood in mood_quotes:
        return {
            "mood": mood,
            "quote": mood_quotes[mood]
        }

    return {
        "message": "Your mood is temporary... just like your exam stress (hopefully)."
    }
