import bge
from bge import logic
import q8

def main(cont):
    own = cont.owner

    scene = logic.getCurrentScene()
    objects = scene.objects
    objects["cube_100"].visible = False
    objects["cube_101"].visible = True
    objects["cube_102"].visible = True

    d1 = [0.001, 0.005, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008]
    qd1 = q8.Q8(random = True)
    qd1.constant_velocity(objects["cube_101"], d1)
    qd1.constant_velocity(objects["cube_102"], d1)

    # A cyclic timer

    if not 'timer' in own:
        own['timer'] = 0

    repeat_after = 600
    own['timer'] += 1
    own['timer'] %= repeat_after

    print(own['timer'])
