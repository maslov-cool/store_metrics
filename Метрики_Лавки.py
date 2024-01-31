n, k = map(int, input().split())
shop_barcode_ = [input() for _ in range(n)]
not_shop_barcode_ = [input() for _ in range(k)]


def solve(shop_barcode, not_shop_barcode):
    def right_barcode(code):
        if len(code.replace(' ', '')) == 15 and code[:4].isdigit() and code[4] in 'abc'\
                and code[5] == '-' and code[6:9].isalpha() and code[9:].isdigit():
            return True
        return False
    right_barcode_shop, wrong_barcode_shop, right_barcode_not_shop = 0, 0, 0
    for barcode in shop_barcode:
        if right_barcode(barcode):
            right_barcode_shop += 1
        else:
            wrong_barcode_shop += 1
    for barcode in not_shop_barcode:
        if right_barcode(barcode):
            right_barcode_not_shop += 1
    print("{0:.4f}".format(right_barcode_shop / (right_barcode_shop + wrong_barcode_shop)),
          "{0:.4f}".format(right_barcode_shop / (right_barcode_shop + right_barcode_not_shop)))


solve(shop_barcode_, not_shop_barcode_)
