import flet as ft
import random

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    words = ["Chinese Kenpo", "Jujutsu", "Boxing", "Sumo", "Silat", "Pro-wrestling", "Karate", "Military Combat Techniques", "Headbutt", "Seiken", "Nukite", "Rear Naked Choke", "Axe Kick", "Suplex", "Cord-Cut", "Eye-Poke", "150 Kilo Backflip", "Chicken Wing Facelock", "Chains", "Knives", "Nunchaku", "Shivs", "Pipes", "Primitive Tools", "Grip Strength", "Demon Back", "Bite Attack", "Ground-and-Pound", "Joint Lock", "Throwing Techniques", "Iron Body", "Pressure Point Strike", "Bone Crushing Punch", "Bear Hug", "Palm Strike", "Finger Snap Strike"]
    
    random.shuffle(words)
    game_words = words[:17]

    mistakes = 0
    current_index = 0

    word_label = ft.Text(value=f"Word: {game_words[current_index]}", size=20)
    status_label = ft.Text(value="", size=19)
    progress_label = ft.Text(value=f"Progress: {current_index}/{len(game_words)}", size=16)
    accuracy_label = ft.Text(value="Accuracy: 0%", size=14)
    input_field = ft.TextField(hint_text="Type here", autofocus=True, width=270)

    def submit_word(e):

    page.update()



ft.app(target=main)
