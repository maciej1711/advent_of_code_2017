from collections import defaultdict
import argparse
"""
--- Day 20: Particle Swarm ---

Suddenly, the GPU contacts you, asking for help. Someone has asked it to simulate too many particles, and it won't be able to finish them all in time to render the next frame at this rate.

It transmits to you a buffer (your puzzle input) listing each particle in order (starting with particle 0, then particle 1, particle 2, and so on). For each particle, it provides the X, Y, and Z coordinates for the particle's position (p), velocity (v), and acceleration (a), each in the format <X,Y,Z>.

Each tick, all particles are updated simultaneously. A particle's properties are updated in the following order:

    Increase the X velocity by the X acceleration.
    Increase the Y velocity by the Y acceleration.
    Increase the Z velocity by the Z acceleration.
    Increase the X position by the X velocity.
    Increase the Y position by the Y velocity.
    Increase the Z position by the Z velocity.

Because of seemingly tenuous rationale involving z-buffering, the GPU would like to know which particle will stay closest to position <0,0,0> in the long term. Measure this using the Manhattan distance, which in this situation is simply the sum of the absolute values of a particle's X, Y, and Z position.

For example, suppose you are only given two particles, both of which stay entirely on the X-axis (for simplicity). Drawing the current states of particles 0 and 1 (in that order) with an adjacent a number line and diagram of current X positions (marked in parenthesis), the following would take place:

p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>                         (0)(1)

p=< 4,0,0>, v=< 1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=< 2,0,0>, v=<-2,0,0>, a=<-2,0,0>                      (1)   (0)

p=< 4,0,0>, v=< 0,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=<-2,0,0>, v=<-4,0,0>, a=<-2,0,0>          (1)               (0)

p=< 3,0,0>, v=<-1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=<-8,0,0>, v=<-6,0,0>, a=<-2,0,0>                         (0)

At this point, particle 1 will never be closer to <0,0,0> than particle 0, and so, in the long run, particle 0 will stay closest.

Which particle will stay closest to position <0,0,0> in the long term?

"""


class Particle(object):
    """
    Class that generates the Partivle objects with position, velocity and acceleration factors
    """
    def __init__(self, position, velocity, acceleration):
        """
        :param position: position of a particle
        :param velocity:  velocity of a particle
        :param acceleration: acceleration of a particle
        """
        self.p = position
        self.v = velocity
        self.a = acceleration

    def step(self):
        """
        Modify the position and velocity of particle
        :return:
        """
        for i in xrange(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]

    def dist(self):
        """
        Calculate the distance from the center
        :return:
        """
        return sum([abs(x) for x in self.p])


def open_file(file_name):
    '''
    Opens a file and returns its content as a list. By summing the absolute value of all 3 vectors of position
    '''
    with open(file_name[0], 'r') as input_file:
        content = input_file.readlines()
    return content


def calculate_distance(file_name, part2):
    """
    This program iterates over lines connected with group {0} and append all of the possible groups
    to a set collection to avoid duplicated entries.
    :param file_name: name of a file with input data
    :return:
    """
    content = open_file(file_name)
    i = 0
    parts = {}
    # Generate particles
    for line in content:
        ts = line.strip().split(", ")
        poss = [int(x) for x in ts[0].split("=")[1][1:-1].split(",")]
        velo = [int(x) for x in ts[1].split("=")[1][1:-1].split(",")]
        acce = [int(x) for x in ts[2].split("=")[1][1:-1].split(",")]
        parts[i] = Particle(poss, velo, acce)
        i += 1
    j = 0
    # Assume that 1000 iteration will be enough to calculate results
    while j < 1000:
        min_dist = None
        min_part = None
        for i, part in parts.iteritems():
            part.step()
            if min_dist is None or part.dist() < min_dist:
                min_part = i
                min_dist = part.dist()
        if part2:
            pos_dict = defaultdict(list)
            for i, part in parts.iteritems():
                k = tuple(part.p)
                pos_dict[k].append(i)

            for k, v in pos_dict.iteritems():
                if len(v) > 1:
                    for i in v:
                        del parts[i]
        j += 1
        if j == 1000 and part2:
            print "Number of particles left after removing coillided: %i" % len(parts)
            print "Particle with shortest distance after removing collided: %s" % min_part

        elif j == 1000:
            print "Particle with shortest distance: %s" % min_part


def main():
    parser = argparse.ArgumentParser(
            description="Script contain a particle generator, position modifier and a distance counter"
                        "Execute the script by typing python particles.py --name file_name",
        )
    parser.add_argument('--name', help='Name of a file to open', nargs='*')
    args = parser.parse_args()
    calculate_distance(args.name, False)
    calculate_distance(args.name, True)


if __name__ == "__main__":
    main()
