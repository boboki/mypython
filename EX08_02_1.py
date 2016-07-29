import random

if __name__ == '__main__':
    print('module_1')

class tools:
    def generate_random_nums(self,length):
        nums=[]
        for i in range(length):
            nums.append(random.randint(1,100))
        return nums