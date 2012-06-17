#!/usr/bin/python

class Anteroposterior(Axis):
    synonyms = ["rostrocaudal", "craniocaudal", "cephalocaudal", "AP"]
    description = "from head end to opposite end of body or tail"
class Anterior(Anteroposterior): pass
class Posterior(Anteroposterior): pass

class Dorsoventral(Axis):
    description = "from spinal column (back) to belly (front)"
    synonyms = ["DV"]
class Dorsal(Dorsoventral): pass
class Ventral(Dorsoventral): pass

class Mediolateral(Axis):
    description = "from center of organism to one or other side (with respect to the organism, not the observer)"
    synonyms = ["ML", "LR"]

class Proximodistal(Axis):
    description = "from tip of an appendage (distal) to where it joins the body (proximal)"
class Proximal(Proximodistal): pass
class Distal(Proximodistal): pass

class Place:
    '''a place contains three axises and is purely locational'''
    axises = [Proximodistal(), Mediolateral(), Dorsoventral(), Anteroposterior()]
    def relate(self, direction, other):
        '''relates this self with respect to another Place, somewhere on the axises'''

        for axis in axises:
            if isinstance(axis, direction): 

class NamedRegion(list, Place):
    '''a named region in the brain, possibly with subregions'''
    def __init__(self, name):
        list.__init__(self)
        self.name = name

class TestBrain(unittest.TestCase):
    def test_connection_relations(self):
        brainstem = Place()
        cortex = Place()
        brainstem.relate(Anterior, cortex)
        brainstem.posterior_to(cortex)
        cortex.anterior_to(brainstem)

