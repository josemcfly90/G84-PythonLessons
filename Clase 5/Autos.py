autos = {'autos':{
    1:{'marca':'Tesla',
    'modelos':{
        1:'Modelo 1',
        2:'Modelo 2',
        3:'Modelo 3',
        4:'Modelo 4'
        }},
    2:{'marca':'Toyota',
    'modelos':{
        1:'Fortuner',
        2:'Prado',
        3:'Tundra',
        4:'Corola'
        }},
    3:{'marca':'Range Rover',
    'modelo':{
        1:'Evoque',
        2:'Defender',
        }},
    4:{'marca':'Mazda',
    'modelos':{
        1:'Mazda 2',
        2:'Mazda 3',
        3:'CX 30'
        }},
    5:{'marca':'Audi',
    'modelos':{
        1:'A7',
        2:'A5',
        3:'A3'
        }}}}
m1 = len(autos['autos'][1]['modelos'])
m2 = len(autos['autos'][2]['modelos'])
m3 = len(autos['autos'][3]['modelos'])
m4 = len(autos['autos'][4]['modelos'])

print(m1, m2, m3, m4)