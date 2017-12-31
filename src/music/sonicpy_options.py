from psonic import *
from multiprocessing import Process
# FIND AND REPLACE
# :%s/ =.*//g
# :%s#\n#,

NOTES = [
    C2, Cs2, Db2, D2, Ds2, Eb2, E2, F2, Fs2, Gb2, G2,
    Gs2, Ab2, A2, As2, Bb2, B2, C3, Cs3, Db3, D3, Ds3,
    Eb3, E3, F3, Fs3, Gb3, G3, Gs3, Ab3, A3, As3, Bb3,
    B3, C4, Cs4, Db4, D4, Ds4, Eb4, E4, F4, Fs4, Gb4,
    G4, Gs4, Ab4, A4, As4, Bb4, B4, C5, Cs5, Db5, D5,
    Ds5, Eb5, E5, F5, Fs5, Gb5, G5, Gs5, Ab5, A5, As5,
    Bb5, B5, C6, R,
]

SYNTHS = [
    DULL_BELL, PRETTY_BELL, SINE, SQUARE, PULSE,
    SUBPULSE, DTRI, DPULSE, FM, MOD_FM, MOD_SAW,
    MOD_DSAW, MOD_SINE, MOD_TRI, MOD_PULSE, SUPERSAW,
    HOOVER, SYNTH_VIOLIN, PLUCK, PIANO, GROWL,
    DARK_AMBIENCE, DARK_SEA_HORN, HOLLOW, ZAWA, NOISE,
    GNOISE, BNOISE, CNOISE, DSAW, TB303, BLADE, PROPHET,
    SAW, BEEP, TRI, CHIPLEAD, CHIPBASS, CHIPNOISE,
    TECHSAWS, SOUND_IN, SOUND_IN_STEREO,
]

SCALES = [
    DIATONIC, IONIAN, MAJOR, DORIAN, PHRYGIAN, LYDIAN,
    MIXOLYDIAN, AEOLIAN, MINOR, LOCRIAN, HEX_MAJOR6,
    HEX_DORIAN, HEX_PHRYGIAN, HEX_MAJOR7, HEX_SUS,
    HEX_AEOLIAN, MINOR_PENTATONIC, YU, MAJOR_PENTATONIC,
    GONG, EGYPTIAN, SHANG, JIAO, ZHI, RITUSEN, WHOLE_TONE,
    WHOLE, CHROMATIC, HARMONIC_MINOR, MELODIC_MINOR_ASC,
    HUNGARIAN_MINOR, OCTATONIC, MESSIAEN1, MESSIAEN2,
    MESSIAEN3, MESSIAEN4, MESSIAEN5, MESSIAEN6, MESSIAEN7,
    SUPER_LOCRIAN, HIRAJOSHI, KUMOI, NEAPLOLITAN_MAJOR,
    BARTOK, BHAIRAV, LOCRIAN_MAJOR, AHIRBHAIRAV, ENIGMATIC,
    NEAPLOLITAN_MINOR, PELOG, AUGMENTED2, SCRIABIN,
    HARMONIC_MAJOR, MELODIC_MINOR_DESC, ROMANIAN_MINOR,
    HINDU, IWATO, MELODIC_MINOR, DIMISHED2, MARVA,
    MELODIC_MAJOR, INDIAN, SPANISH, PROMETHEUS, DIMISHED,
    TODI, LEADING_WHOLE, AUGMENTED, PRUVI, CHINESE,
    LYDIAN_MINOR, I, II, III, IV, V, VI, VII, VIII,
]

CHORD_QUAL = [
    MAJOR7, DOM7, MINOR7, AUG, DIM, DIM7,
]


class Samples(object):

    def drums(self):
        sounds = [
            DRUM_BASS_HARD, DRUM_BASS_SOFT, DRUM_COWBELL,
            DRUM_CYMBAL_CLOSED, DRUM_CYMBAL_HARD, DRUM_CYMBAL_OPEN,
            DRUM_CYMBAL_PEDAL, DRUM_CYMBAL_SOFT, DRUM_HEAVY_KICK,
            DRUM_ROLL, DRUM_SNARE_HARD, DRUM_SNARE_SOFT, DRUM_SPLASH_HARD,
            DRUM_SPLASH_SOFT, DRUM_TOM_HI_HARD, DRUM_TOM_HI_SOFT,
            DRUM_TOM_LO_HARD, DRUM_TOM_LO_SOFT, DRUM_TOM_MID_HARD,
            DRUM_TOM_MID_SOFT,
        ]
        return sounds

    def electric(self):
        sounds = [
            ELEC_BEEP, ELEC_BELL, ELEC_BLIP, ELEC_BLIP2, ELEC_BLUP,
            ELEC_BONG, ELEC_CHIME, ELEC_CYMBAL, ELEC_FILT_SNARE,
            ELEC_FLIP, ELEC_FUZZ_TOM, ELEC_HI_SNARE, ELEC_HOLLOW_KICK,
            ELEC_LO_SNARE, ELEC_MID_SNARE, ELEC_PING, ELEC_PLIP,
            ELEC_POP, ELEC_SNARE, ELEC_SOFT_KICK, ELEC_TICK, ELEC_TRIANGLE,
            ELEC_TWANG, ELEC_TWIP, ELEC_WOOD,
        ]
        return sounds

    def guitars(self):
        # NameError: name 'GUIT_EM9' is not defined
        sounds = [
            GUIT_E_FIFTHS, GUIT_E_SLIDE, GUIT_HARMONICS,
        ]
        return sounds

    def misc(self):
        sounds = [
            MISC_BURP, MISC_CINEBOOM, MISC_CROW,
        ]
        return sounds

    def percurssive(self):
        # NameError: name 'PERC_SNAP' is not defined
        # NameError: name 'PERC_SNAP2' is not defined
        sounds = [
            PERC_BELL, PERC_SWASH, PERC_TILL,
        ]
        return sounds

    def ambient(self):
        sounds = [
            AMBI_CHOIR, AMBI_DARK_WOOSH, AMBI_DRONE, AMBI_GLASS_HUM,
            AMBI_GLASS_RUB, AMBI_HAUNTED_HUM, AMBI_LUNAR_LAND, AMBI_PIANO,
            AMBI_SOFT_BUZZ, AMBI_SWOOSH,
        ]
        return sounds

    def bass(self):
        sounds = [
            BASS_DNB_F, BASS_DROP_C, BASS_HARD_C, BASS_HIT_C, BASS_THICK_C,
            BASS_VOXY_C, BASS_VOXY_HIT_C, BASS_WOODSY_C,
        ]
        return sounds

    def snare(self):
        # NameError: name 'SN_DOLF' is not defined
        # NameError: name 'SN_DUB' is not defined
        # NameError: name 'SN_ZOME' is not defined
        sounds = [

        ]
        return sounds

    def bass_drums(self):
        sounds = [
            BD_808, BD_ADA, BD_BOOM, BD_FAT, BD_GAS, BD_HAUS, BD_KLUB,
            BD_PURE, BD_SONE, BD_TEK, BD_ZOME, BD_ZUM,
        ]
        return sounds

    def looping(self):
        # NameError: name 'LOOP_BREAKBEAT' is not defined
        # NameError: name 'LOOP_GARZUL' is not defined
        # NameError: name 'LOOP_MIKA' is not defined
        sounds = [
            LOOP_AMEN, LOOP_AMEN_FULL, LOOP_COMPUS,
            LOOP_INDUSTRIAL, LOOP_SAFARI, LOOP_TABLA,
        ]
        return sounds

    def tabla(self):
        sounds = [
            TABLA_DHEC, TABLA_GHE1, TABLA_GHE2, TABLA_GHE3, TABLA_GHE4,
            TABLA_GHE5, TABLA_GHE6, TABLA_GHE7, TABLA_GHE8, TABLA_KE1,
            TABLA_KE2, TABLA_KE3, TABLA_NA, TABLA_NA_O, TABLA_NA_S, TABLA_RE,
            TABLA_TAS1, TABLA_TAS2, TABLA_TAS3, TABLA_TE1, TABLA_TE2,
            TABLA_TE_M, TABLA_TE_NE, TABLA_TUN1, TABLA_TUN2, TABLA_TUN3,
        ]
        return sounds

    def vinyl(self):
        sounds = [
            VINYL_BACKSPIN, VINYL_HISS, VINYL_REWIND, VINYL_SCRATCH,
        ]
        return sounds

class Effects(object):

    def effects(self):
        sounds = [
            BITCRUSHER, COMPRESSOR, ECHO, FLANGER, KRUSH, LPF, PAN,
            PANSLICER, REVERB, SLICER, WOBBLE,
        ]
        return sounds




s = Samples()
drums = s.drums()
electric = s.electric()
guitars = s.guitars()
percurssive = s.percurssive()
misc = s.misc()
ambient = s.ambient()
bass = s.bass()
snare = s.snare()
bass_drums = s.bass_drums()
looping = s.looping()
tabla = s.tabla()
vinyl = s.vinyl()



#sample(bass_drums[9], amp=3)

def intro():
    i = 16
    while i > 0:
        i -= 1
        print(i)
        sample(BD_TEK, amp=3)
        sleep(0.4)

    return True

def base_beat():
    while True:
        sample(BD_TEK, amp=3)
        sleep(0.4)
        #sample(DRUM_CYMBAL_CLOSED)
        #sleep(0.25)
        #sample(bass_drums[9], amp=3)
        #sleep(0.2)
        #sample(bass_drums[11], amp=3)

def beat_2():
    while True:
        sample(DRUM_HEAVY_KICK)
        sleep(0.2)
        sample(DRUM_CYMBAL_CLOSED)
        sleep(0.2)
        sample(DRUM_HEAVY_KICK)
        sleep(0.2)


def control():

    intro()

    base = Process(target=base_beat)
    base.start()

    alpha = Process(target=beat_2)
    alpha.start()



control()
#p.join()
#p.terminate() # to stop playing beat



#i= 0
#for item in drums:
#    i+=1
#    x = sample(item, amp=3)
#    print(i)
#    sleep(1)


method_list = [func for func in dir(s) if callable(getattr(s, func)) and not func.startswith("__")]
print(method_list)

"""
for samples in method_list:
    func = '{}.{}'.format(s, samples)
    print(func)
    for item in func:
        #use_synth(item)
        #print(item.name)
        #print(item.name)
        #play(item)
        sample(item)
        sleep(1)
"""

"""
synth(name,
      note=None, attack=None, decay=None,
      sustain_level=None, sustain=None,
      release=None, cutoff=None,
      cutoff_attack=None, amp=None, pan=None)

play(note,
     attack=None, decay=None, sustain_level=None,
     sustain=None, release=None, cutoff=None,
     cutoff_attack=None, amp=None, pan=None)

play_pattern_timed(notes, times, release=None)

play_pattern(notes)

sample(sample,
       rate=None, attack=None, sustain=None,
       release=None, beat_stretch=None, start=None,
       finish=None, amp=None, pan=None)

chord(root_note, chord_quality)

scale(root_note, scale_mode, num_octaves=1)

"""

