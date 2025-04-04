import random
import time
from IPython.display import display, clear_output

class SlotMachine:
    def __init__(self, pronouns, verbs, objects):
        self.pronouns = pronouns
        self.verbs = verbs
        self.objects = objects

    def display_frame(self, p, v, o):
        print("---------------------")
        print("| {:<10} | {:<10} | {:<15} |".format("Pronomen", "Verb", "Objekt"))
        print("---------------------")
        print("| {:<10} | {:<10} | {:<15} |".format(p, v, o))
        print("---------------------")

    def animate_spin(self, duration=2):
        updates_per_second = 6
        total_updates = int(duration * updates_per_second)
        delay = 1 / updates_per_second

        print("Slot Machine dreht sich...\n")

        for _ in range(total_updates):
            pronoun = random.choice(self.pronouns)
            verb = random.choice(self.verbs)
            obj = random.choice(self.objects)

            clear_output(wait=True)
            print("Slot Machine dreht sich...\n")
            self.display_frame(pronoun, verb, obj)
            time.sleep(delay)

        return random.choice(self.pronouns), random.choice(self.verbs), random.choice(self.objects)

    def play(self):
        while True:
            action = input("Drücke Enter, um den Hebel zu ziehen (oder 'q' zum Beenden)...")
            clear_output(wait=True)

            if action.lower() == 'q':
                print("Spiel beendet.")
                break

            final_pronoun, final_verb, final_object = self.animate_spin()

            clear_output(wait=True)
            print("--- Ergebnis ---")
            self.display_frame(final_pronoun, final_verb, final_object)
            print("\n")

if __name__ == "__main__":
    pronouns = ["ich", "du", "er", "sie", "es", "wir", "ihr", "Sie"]
    #verbs = ["fahren", "haben", "zurückkommen", "ankommen", "kaufen", "fliegen", "liegen", "finden", "stehen", "nutzen", "gehen"]
    verbs = ["fahren", "haben", "kaufen", "fliegen", "finden", "nutzen"]
    #verbs = ["sein"]
    objects = ["der Zug", "der Bus", "die U-Bahn", "die S-Bahn", "das Auto", "das Fahrrad", "der Koffer", "die Tasche", "das Gepäck", "der Rücksack", "das Motorrad", "der Motorroller", "das Taxi", "das Flugzeug", "das Boot", "die Straßenbahn", "die Fähre"]

    game = SlotMachine(pronouns, verbs, objects)
    game.play()
