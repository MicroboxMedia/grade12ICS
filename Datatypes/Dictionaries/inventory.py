prices = [3.98, 0.97, 2.97, 3.99, 3.98, 1.98, 3.98, 1.98, 1.98, 3.98, 2.98, 2.99, 3.97, 0.97, 1.99, 0.98, 0.97, 3.99,
          2.99, 3.97, 3.99, 0.98, 3.97, 1.98, 2.99, 1.97, 2.98, 1.97, 0.98, 2.97, 3.97, 0.99, 1.97, 2.97, 2.99, 1.98,
          0.98, 1.98, 1.97, 1.98, 2.99, 1.97, 0.98, 0.97, 1.99, 3.97, 2.99, 0.99, 3.98, 3.97, 3.97, 1.99, 3.97, 3.98,
          1.98, 2.99, 2.97, 3.97, 3.99, 3.98, 3.99, 2.97, 0.97, 0.99, 1.97, 0.97, 2.99, 3.99, 0.99, 2.97, 0.98, 3.97,
          1.99, 0.99, 1.97, 0.97, 0.97, 2.99, 0.99, 0.97, 3.97, 1.99, 2.98, 3.97, 3.99]
items = ['advil', 'aspirin', 'antacids', 'antibiotic ointment', 'anti-aerial towelettes', 'automotive repair kits',
         'baking tin', 'bandages', 'bandannas', 'baking soda', 'lighters', 'boxed food', 'bungee cords', 'cable ties',
         'camping fuel', 'candles', 'canned fruits', 'canned meat', 'canned veggies', 'can openers', 'car towels',
         'chewing gum', 'clothesline', 'coffee filters', 'combs', 'compact mirror', 'condiments', 'cotton balls',
         'cookie tins', 'cough drops', 'cutting boards', 'dental floss', 'digital thermometer', 'dish towels',
         'dog food', 'duct tape', 'drop cloth', 'ear plugs', 'elastic hair bands', 'emergency cell phone chargers',
         'epsom salts', 'eyeglass repair kit', 'facial tissues', 'gauze', 'gardening globes', 'hard candies',
         'hydrogen peroxide', 'hand sanitizer', 'jarred foods', 'instant ice packs', 'knives',
         'latex dishwashing gloves', 'lip balms', 'lotions', 'magnifying glass', 'matches', 'mesh laundry bag', 'nails',
         'screws', 'plastic shoe container', 'rubbing alcohol', 'safety pins', 'salt with iodine', 'scrub buddies',
         'sewing kit', 'shoe laces', 'soaps', 'socks', 'solar lights', 'spices', 'steel wool', 'sponges', 'sugar',
         'super glue', 'sun hat', 'toothbrushes', 'tote bags', 'travel bottles', 'twine', 'utility pail', 'water',
         'wet wipes']
list_diff = len(prices) - len(items)
if list_diff > 1:
    items.extend(f"Unknown object {str(i)}" for i in range(1, list_diff + 1))
else:
    prices.extend(f"Unknown price {str(i)}" for i in range(1, list_diff*-1+1))
items_prices = dict(zip(items, prices))
print(items_prices)
