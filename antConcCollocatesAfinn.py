from afinn import Afinn
import sys
import glob

if __name__ == '__main__':
    myAfinn = Afinn()

    total_positive = 0
    total_negative = 0
    for filename in glob.glob('collocates/*.txt'):
        with open(filename, 'r') as f:
            lines = list(map(lambda x: x.strip().split('\t'), f))[2:]
            positive = 0
            negative = 0

            for line in lines:
                score = myAfinn.score(line[5])
                if score > 0.0:
                    positive += int(line[1])
                elif score < 0.0:
                    negative += int(line[1])

            result = float(positive) / (positive + negative) if positive > 0 else 0.0
            total_positive += positive
            total_negative += negative

            print('====[%s]====' % filename)
            print('positive: %d' % positive)
            print('negative: %d' % negative)
            print('rate:     %f' % result)

    print('\n====Total====')
    print('positive: %d' % total_positive)
    print('negative: %d' % total_negative)
    print('rate:     %f' % (
        float(total_positive) / (total_positive + total_negative)))
