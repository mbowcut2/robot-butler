"""
This file contains lists of words used to populate templates
"""

ROOMS = ['living room', 'bathroom', 'bedroom', 'kitchen']
OBJECTS = {
    'living room':[
        'couch',
        'chair',
        'television',
        'endtable',
        'coffeetable',
        'lamp',
        'bookcase'
        ],
    'bathroom':[
        'toilet',
        'bathtub',
        'shower',
        'mirror',
        'rug'
        ],
    'bedroom':[
        'bed',
        'dresser',
        'desk',
        'chair',
        'computer',
        'bookcase'
        ],
    'kitchen':[
        'table',
        'chair',
        'sink',
        'dishwasher',
        'stove',
        'oven',
        'microwave',
        'refrigerator',
        'freezer',
        'cupboard'
        ],
    'floor': ['action figure',
        'book',
        'empty soda can',
        'guitar',
        'candy wrapper',
        'shoe',
        'sock',
        'shirt',
        'pair of pants',
        'plate'
        ]
    }
UNUSUAL_OBJECTS = ['dead body', 'sword', 'time machine', 'dragon']
AMBIGUOUS_OBJECTS = ['helicopter', 'airplane', 'train'] # These objects would be inferred to be toys in context. I'm curious to see how the model would handle them.
