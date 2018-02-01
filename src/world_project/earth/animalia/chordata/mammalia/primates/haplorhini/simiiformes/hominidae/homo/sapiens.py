from collections import namedtuple

"""
Wikipedia: https://en.wikipedia.org/wiki/Homo_sapiens

https://en.wikipedia.org/wiki/List_of_organs_of_the_human_body
"""

class Mind:
    """What is mind?"""

class Cells: pass
class Tissues: pass

# Organs
class Heart: pass
class Lungs: pass #
class Liver: pass
class Pharynx: pass #
class Larynx: pass #
class Arteries: pass
class Muscles: pass
class Gallbladder: pass
class Kidneys: pass #
class Skeleton: pass
class Intestines: pass
class Brain: pass
class LymphNodes: pass
class Spleen: pass
class BoneMarrow: pass
class Stomach: pass
class Veins: pass
class Pancreas: pass
class UrinaryBladder: pass #

# Systems
class CirculatorySystem: pass

Mouth = namedtuple('Mouth', 'none')
class DigestiveSystem(Mouth): pass


class EndocrineSystem: pass
class ImmuneSystem: pass
class IntegumentarySystem: pass
class LymphaticSystem: pass
class MusculoskeletalSystem:
    """
    Human Skeleton
    Joints
    Ligaments
    Muscular system
        Tendons
    """
class NervousSystem: pass
class ReproductiveSystem: pass

NasalCavity = namedtuple('NasalCavity', 'none')
Trachea = namedtuple('Trachea', 'none')
Bronchi = namedtuple('Bronchi', 'none')
Diaphragm = namedtuple('Diaphragm', 'none')
class RespiratorySystem(
    NasalCavity,
    Pharynx,
    Larynx,
    Trachea,
    Bronchi,
    Lungs,
    Diaphragm,
): pass

Ureters = namedtuple('Ureters', 'none')
Urethra = namedtuple('Urethra', 'none')
class UrinarySystem(Kidneys, Ureters, UrinaryBladder, Urethra): pass

class Organs(
    Heart,
    Lungs,
    Liver,
):
    pass

class Systems(
    CirculatorySystem,
    DigestiveSystem,
    EndocrineSystem,
    ImmuneSystem,
    IntegumentarySystem,
    LymphaticSystem,
    MusculoskeletalSystem,
    NervousSystem,
    ReproductiveSystem,
    #RespiratorySystem,
    #UrinarySystem,
    # LIMITS TO INHERITANCE?
    #TypeError: multiple bases have instance lay-out conflict
):
    pass

class Body(Cells, Tissues, Organs, Systems):
    def __init__(self):
        carbon = 65.0
        hydrogen = 18.5
        nitrogen = 3.2
        calcium = 1.5
        phosphorus = 1.0
        potassium = 0.4
        sulfur = 0.3
        sodium = 0.2
        chlorine = 0.2
        magnesium = 0.1


class Human(Mind):
    humanity = 'intact'
    nature = 'good'

class Man(Human):
    pass

class Woman(Human):
    pass

