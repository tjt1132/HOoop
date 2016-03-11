"""file: new_main.py"""
import random
import target
import medium
import generator
import detector
import radar
import screen
import renderizer

def main():
    """Main function."""

    time_step = 0.25
    sampling_rate = 0.01

    trgts = []

    for i in range(10):
        trgts.append(target.Target(random.random() * 30, random.random() * 0.5,
                                   2, 0,
                                   ([0, 100], [100, 0])))

    mdm = medium.Medium(trgts)

    #test_data = np.random.rand(2, 25)

    gen = generator.Generator(0.2, 0, 10, 0)
    dec = detector.Detector()
    rdr = radar.Radar(gen, dec)
    scr = screen.Screen(rdr, mdm, 0)

    rndr = renderizer.Renderizer(scr)

    rndr.show()

if __name__ == "__main__":
    main()
