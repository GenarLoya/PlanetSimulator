#Esto es para agregar la path principal del proyecto y poder incluir modulos en carpetas de jerarquia anterior

import sys
from os.path import dirname, abspath

dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

#########################################################

#from logging import basicConfig, info, INFO
#basicConfig(level=INFO, format='[%(levelname)] (%(threadname)-s) %(message)')

from Utilities.obtains import interval

COLOR_FILL = 0,0,0
COLOR_DRAW = 255,255,255
SIZE = WIDHT, HEIGHT = 1300, 700
PLANETS_IN_SYSTEM = interval(dir + '\Resources\Probabilitys\Planet_counter.csv')
MOONS_IN_PLANET = interval(dir + '\Resources\Probabilitys\Moon_counter.csv')
DISCOVERY_FACILITY = interval(dir + '\Resources/Probabilitys/Discovery_facility.csv')