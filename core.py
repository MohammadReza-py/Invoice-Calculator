from tabulate import tabulate
class CallculationOperation:
    '''give a dict , for key value give product name'''
    def __init__(self):
        self.args = {}  # {productName: {'price': productPrice, 'productDiscount': discount, 'productNumber': number}}

    def addProduct(self,product: dict):
        self.args.update(product)

    def calculationPay(self):
        factor = []
        for product, info in self.args.items():
            price = ((info['price'] - (info['price'] * info['discount'])) * info['number'])
            factor.append({
                'product name': product,
                'number': info['number'],
                'price before discount': info['price'],
                'discount': info['discount'],
                'final price': price,
            })
        total = 0
        for i in factor:
            total += i['final price']
        return {"products" : factor, 'totalPay': total}

    def tabulateShow(self, factor):
        # headers رو از کلیدهای اولین دیکشنری می‌گیریم
        headers = factor[0].keys()

        # هر دیکشنری رو به list تبدیل می‌کنیم
        rows = [list(item.values()) for item in factor]

        return tabulate(rows, headers=headers, tablefmt="fancy_grid")
