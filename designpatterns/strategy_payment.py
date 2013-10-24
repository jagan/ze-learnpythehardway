"""
Illustrating Strategy design pattern using various modes of Payment
"""
from abc import ABCMeta, abstractmethod
import collections

class AbstractPaymentMethod(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def input_details(self):
        raise NotImplemented()

    @abstractmethod
    def pay(self, amount):
        raise NotImplemented()

class CreditCardPayment(AbstractPaymentMethod):
    def __init__(self, merchant_account_no):
        self.merchant_account_no = merchant_account_no

    def input_details(self):
        self.card_number = raw_input('Card Number: ')
        self.merchant = raw_input('Card Type [Visa/MasterCard]: ')
        self.cvv = raw_input('CVV: ')

    def pay(self, amount):
        print 'Paid %f using %s Credit Card (%s)' % (amount, self.merchant, self.card_number)

class PaypalPayment(AbstractPaymentMethod):
    def __init__(self, merchant_id):
        self.merchant_id = merchant_id

    def input_details(self):
        self.payer_email_id = raw_input('PayPal Id: ')
        self.passcode = raw_input('PayPal Passcode: ')

    def pay(self, amount):
        print 'Paid %f using PayPal to merchant account (%s)' % (amount, self.merchant_id)

Article = collections.namedtuple('Article', 'id name price')

class PurchaseProcessor(object):
    def purchase(self, article):
        print 'You have chosen to buy article: %s' % article.name
        payment_methods = [CreditCardPayment('123-456-6778'), PaypalPayment('xyz.merchant@paypal.com')]
        for i, payment_method in enumerate(payment_methods):
            print '%d. %s' % (i + 1, payment_method.__class__.__name__)
        i = raw_input('Enter the payment method number that you want to use: ')
        payment_method = payment_methods[int(i) - 1]

        print 'Please enter the following Payment details:'
        payment_method.input_details()
        payment_method.pay(article.price)
        print 'Thanks for choosing our store to buy stuff!'

def main():
    articles = [
        Article(100, 'Lux Soap', 22.5),
        Article(110, 'Axe Deo', 52.0),
        Article(100, 'Milk Bikies Biscuit - 100g', 10.0),
    ]
    for i, article in enumerate(articles):
        print '%d. %s' % (i+1, article)
    i = raw_input('Enter the article number that you want to buy: ')
    article = articles[int(i)-1]
    purchase_processor = PurchaseProcessor()
    purchase_processor.purchase(article)

if __name__ == "__main__":
    while True:
        p = raw_input('Do you want to buy an article? ')
        if p.lower() in ['n', 'no', 'nop', 'nope']:
            print 'Thanks for shopping with us!'
            break
        elif p.lower() in ['y', 'yep', 'yes', 'ya']:
            main()
