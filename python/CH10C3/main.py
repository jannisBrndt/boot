def calculate_total(items_purchased, pinned_list):
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }

    # Don't touch above this line

    # list of items not purchased
    unpurchased_items = []
    # dict of all items bought
    receipt = {}
    # total sum of items purchased
    total_cost = 0.0
    
    # create receipt
    for item in items_purchased:
        receipt[item] = item_prices[item]
        print(item_prices[item])

    # calculate total shopping cost 
    for item in receipt:
        price = receipt[item]
        total_cost += price

    for item in pinned_list:
        if item not in items_purchased:
            unpurchased_items.append(item)
    
    return unpurchased_items, receipt, total_cost

def main():
    items_purchased = ['health_potion',
                       'mana_potion',
                       'gold_dust',
                       'herbs',
                       'crystal_shard',
                       'dwarven_ale'
                       ]
    pinned_list = ['health_potion',
                   'mana_potion',
                   'ice_cold_milk',
                   'gold_dust',
                   'herbs',
                   'crystal_shard',
                   'magic_ring',
                   'dwarven_ale',
                   'mystic_amulet'
                   ]
    calculate_total(items_purchased, pinned_list)

main()
