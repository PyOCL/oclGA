import random
from gene import Gene
from chromosome import Chromosome
from math import pi, sqrt, asin, cos, sin, pow

def calc_linear_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calc_spherical_distance(x1, y1, x2, y2):
    def rad(deg):
        return deg * pi / 180.0
    rad_x1 = rad(x1)
    rad_x2 = rad(x2)
    a = rad_x1 - rad_x2
    b = rad(y1) - rad(y2)
    s = 2 * asin(sqrt(pow(sin(a/2),2)+cos(rad_x1)*cos(rad_x2)*pow(sin(b/2),2)))
    s = s * 6378.137
    s = round( s * 10000 ) / 10000
    return s

def create_chromosomes_by_cityids(num_of_chromosomes, city_ids):
    chromosomes = []

    for x in range(num_of_chromosomes):
        genes = []
        random.seed(x)
        random.shuffle(city_ids)
        for city_id in city_ids:
            g = Gene([city_id], elements=set(city_ids), name='city %s'%str(x))
            genes.append(g)

        c = Chromosome(genes)
        chromosomes.append(c)

    return chromosomes

def custom_mutate(c1, prob):
    ori_candidates = range(c1.num_of_genes)
    for idx1 in ori_candidates:
        if random.random() < prob:
            candidates_remain = [x for x in ori_candidates if x != idx1]
            idx2 = random.sample(candidates_remain, 1)[0]
            c1.swap(idx1, idx2)

def custom_crossover(c1, c2, point):
    for i in range(c1.num_of_genes):
        if c1.dna[i] == c2.dna[point]:
            c1.swap(point, i)
            break