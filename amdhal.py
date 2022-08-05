import numpy as np
from time import time

def simple_mandelbort(height, width, r_low, r_high, i_low, i_high, max_iters):

    real_vals = np.linspace(r_low, r_high, width)
    img_vals = np.linspace(i_low, i_high, height)


    man_graph = np.ones((height, width), dtype=np.float32)

    for x in range(width):
        for y in range(height):
        
            c = np.complex64( real_vals[x] + img_vals[y] * 1j)
            z = np.complex64(0)

            for i in range(max_iters):

                z = z**2 + c

                if (np.abs(z) > 2):
                    man_graph[y, x] = 0 
                    break
    return man_graph

if __name__ == "__main__":

    t1 = time()
    mandel = simple_mandelbort(521, 521, -2, 2, -2, 2, 256)
    t2 = time()

    print(f"Time taken to build the set was : {t2 - t1}")
