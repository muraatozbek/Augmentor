

import Augmentor

p = Augmentor.Pipeline("C:/Users/Murat/Desktop/m/")

p.rotate(probability=1.0, max_left_rotation=5, max_right_rotation=10)
p.zoom(probability=0.3, min_factor=1.1, max_factor=1.6)
p.flip_left_right(probability=0.4)
p.flip_top_bottom(probability=0.8)
p.rotate90(probability=0.1)
p.black_and_white(probability=0.3, threshold=128)



p.sample(20)

