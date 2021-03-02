class Basket():

   def __init__(self, request):
      self.session = request.session
      basket = self.session.get('skey')

      if 'skey' not in self.session:
         basket = self.session['skey'] = {}
      self.basket = basket

   def add(self, product, qty):
      """
      Adding and updating the users basket session data
      """
      product_id = product.id

      if product_id not in self.basket:
         self.basket[product_id] = {'price': str(product.pricce), 'qty': int(qty)}

      self.session.modified = True

   def __len__(self):
      """
      get the basket and count the qty of items
      """

      return sum(item['qty'] for item in self.basket.values())
