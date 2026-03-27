#implementation(python)
import random

class Gene:
    def __init__(self):
        self.value = random.randint(0, 1)

    def mutate(self):
        # Flip the bit: 0 becomes 1, 1 becomes 0
        self.value = 1 if self.value == 0 else 0

class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:  # 1/2 chance to flip
                gene.mutate()

class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                chromosome.mutate()
    
    def is_all_ones(self):
        return all(gene.value == 1 for chrom in self.chromosomes for gene in chrom.genes)

class Organism:
    def __init__(self, dna, environment_prob):
        self.dna = dna
        self.environment_prob = environment_prob # Probability the DNA mutates at all

    def evolve(self):
        if random.random() < self.environment_prob:
            self.dna.mutate()
            
#running the sumilation
def run_simulation():
    my_dna = DNA()
    # High environment probability speeds up the process
    human = Organism(my_dna, environment_prob=0.8) 
    
    generations = 0
    while not human.dna.is_all_ones():
        human.evolve()
        generations += 1
        
        # Optional: Print progress every 100,000 generations 
        # so you know the script is still running!
        if generations % 100000 == 0:
            current_ones = sum(gene.value for chrom in human.dna.chromosomes for gene in chrom.genes)
            print(f"Gen {generations}: {current_ones}/100 genes are '1'")

    print(f"Success! Evolution reached perfection in {generations} generations.")

# run_simulation()