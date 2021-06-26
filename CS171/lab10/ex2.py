import re


def countSmileys(arr):
    valid_eyes = [':', ';']
    valid_nose = ['-', '~']
    valid_mouth = [')', 'D']

    count = 0

    for i, item in enumerate(arr):

        if len(item) == 2:
            # no nose
            if item[0] in valid_eyes and item[1] in valid_mouth:
                count += 1

        elif len(item) == 3:
            # has nose
            if item[0] in valid_eyes and item[1] in valid_nose and item[2] in valid_mouth:
                count += 1

    return count


if __name__ == '__main__':
    print(countSmileys([':)', ';(', ';}', ':-D']))
    print(countSmileys([';D', ':-(', ':-)', ';~)']))
    print(countSmileys([';]', ':[', ';*', ':$', ';-D']))
