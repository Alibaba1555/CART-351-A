Collective Drums

Collective Drums is an interactive Flask web application that turns individual rhythm patterns into a collective musical experience.
Each participant creates a 6×16 beat grid—like programming a digital drum machine—and submits it to a shared server.
The app visualizes all contributions as an evolving heatmap, blending multiple user patterns and sound kits into one living composition.

The project explores how individual expression merges within collective creation in a digital context.
Every click represents a small act of participation—personal rhythms transformed into data, then remixed into communal sound.
Through this interaction, the application becomes a reflection on digital collaboration, memory, and shared presence.

Features

Interactive 6×16 rhythm grid (click to toggle beats)

User name, message, and sound kit selection

Multiple sound kits (Standard, 8-bit, Techno, Acoustic, Trap 808)

Collective playback combining the latest five patterns

Heatmap visualization showing popular beats

Recording & download of the live mix as .wav

Persistent JSON data storage on the server

Built entirely with Flask, HTML/CSS, and Vanilla JS (Tone.js)

Concept

The minimalist interface focuses attention on rhythm and participation.
Over time, random clicks and user decisions form a dynamic archive a constantly shifting “portrait of sound.”
Collective Drums invites users to reflect on how digital systems reshape creativity:
how small, individual gestures accumulate into collective meaning.

Stack

Backend: Flask (Python)
Frontend: HTML, CSS, JavaScript (Fetch API, Tone.js)
Data: JSON (server-side persistence)

Run locally with:

conda activate flask351
python app.py


Then open http://127.0.0.1:5000