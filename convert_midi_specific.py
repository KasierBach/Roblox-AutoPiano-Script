
from pyMIDI import MidiFile

midi_file = "midi/32492-con-gi-dep-hon-piano.mid"
midi = MidiFile(midi_file)
midi.save_song("song.txt")
print("Converted specific MIDI file successfully.")
