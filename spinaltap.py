class Amp:
    # this is the blueprint for an amp object
    def __init__(self, wattage, tube, make, model, ohms, color='black', speaker_size=12):
        self.wattage = wattage
        self.tube = tube
        self.make = make
        self.model = model
        self.ohms = ohms
        self.color = color
        self.speaker_size = speaker_size
        self.max_volume = 11
        self.volume = 0

    def __str__(self):
        return f'{self.make} {self.model}'

    def turn_up(self, new_volume):
        # instance method, called on an instance of a class
        if new_volume <= self.max_volume:
            if self.volume == self.max_volume:
                print('Fire your guitarist.')
                return
            else:
                self.volume = new_volume

        else:
            print("Zir, this is a Wendy's")

jeromes_amp = Amp(20, False, 'Marshall', 'Valvestate 2000', 8, color='gold/black')
# this creates an instance of amp, a representation of an actual amp

print(f"Starting volume for Jerome's amp: {jeromes_amp.volume}")
jeromes_amp.turn_up(11)
print(f"New volume for Jerome's amp: {jeromes_amp.volume}")