# python3

import matplotlib.pyplot as plt
import matplotlib.animation as anim
import sys
import time

def main():
    fin = open("pi.file", 'r')

    vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    vals_per_update = 1000
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    mode = "animate"

    def update(i):
        for i in range(0, vals_per_update):
            c = fin.read(1)

            if not c:
                alive = False
                return
            
            if c == '.' or c == '\n':
                return
            
            num = int(c)
            vals[num] += 1

        ax.clear()
        ax.bar(range(0, len(vals)), vals)
    
    def run():
        while True:
            c = fin.read(1)

            if not c:
                break
            
            if c == '.' or c == '\n':
                continue
            
            num = int(c)
            vals[num] += 1
    
    if mode == "animate":
        a = anim.FuncAnimation(fig, update)
    elif mode == "run":
        run()
        ax.bar(range(0, len(vals)), vals)
        plt.ylim(min(vals)*0.99, max(vals)*1.01)
    plt.show()

    print("Mean: {}".format(sum(vals)/len(vals)))
    print("Max: {}".format(max(vals)))
    print("Min: {}".format(min(vals)))
    print("Range: {}".format(max(vals) - min(vals)))

if __name__ == "__main__":
    main()
