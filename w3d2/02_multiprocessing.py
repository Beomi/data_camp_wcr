from multiprocessing import Pool
 
def doubler(number):
    return number * 2
 
if __name__ == '__main__':
    numbers = range(999)
    pool = Pool(processes=3)
    print(pool.map(doubler, numbers))
