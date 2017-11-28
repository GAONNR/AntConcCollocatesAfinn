from afinn import Afinn
import glob

if __name__ == '__main__':
    myAfinn = Afinn()

    categories = ['souvenir', 'shopping', 'drinks', 'meal', 'exhibition',
                  'garden', 'architecture', 'accessibility', 'traditional',
                  'sports', 'walking', 'photo', 'experience',
                  'festival', 'tranquil', 'trendy', 'religious',
                  'accomodation']
    total = list()
    for foldername in categories:
        total_positive = 0
        total_negative = 0
        for filename in glob.glob('collocates/%s/*.txt' % foldername):
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

                result = float(positive) / (positive +
                                            negative) if positive > 0 else 0.0
                total_positive += positive
                total_negative += negative

                print('====[%s]====' % filename)
                print('positive: %d' % positive)
                print('negative: %d' % negative)
                print('rate:     %f' % result)

        total_rate = float(total_positive) \
            / (total_positive + total_negative) if total_positive > 0 else 0.0
        print('\n====Category: %s====' % foldername)
        print('positive: %d' % total_positive)
        print('negative: %d' % total_negative)
        print('rate:     %f' % total_rate)

        total.append((foldername, total_positive,
                      total_negative, total_rate))

    print('\n\n')
    for rate in total:
        print('Category: %s\tPositive: %d\tNegative: %d\tRate: %f' %
              (rate[0], rate[1], rate[2], rate[3]))
