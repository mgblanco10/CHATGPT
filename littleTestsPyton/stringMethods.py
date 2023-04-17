def sales_prices(item_and_price):
    item = ""
    price = ""
    item_or_price = item_and_price.split()

    for x in item_or_price:
        if x.isalpha():
            item += x + " "

        else:
            price = x

    item = item.strip()
    return "{} are on sale for ${}".format(item,price)

print(sales_prices("Winter fleece jackets 49.99"))
# Should print "Winter fleece jackets are on sale for $49.99"

# This function accepts a string variable "data_field".  
def count_words(data_field):
    split_data = data_field.split()
    return len(split_data)

print(count_words("Catalog item 3523: Organic raw pumpkin seeds in shell"))
# Should print 9

# The lists need to be combined with the years in chronological order.
def record_profit_years(recent_first, recent_last):
    recent_first.reverse()
    recent_last.extend(recent_first)
    return recent_last

recent_first = [2022, 2018, 2011, 2006]
recent_last = [1989, 1992, 1997, 2001]

print(record_profit_years(recent_first, recent_last))
# Should print [1989, 1992, 1997, 2001, 2006, 2011, 2018, 2022]

# The function accepts two parameters: a start year and an end year.
def list_years(start, end):
    return [year for year in range(start, end+1)]

print(list_years(1972, 1975)) 
# Should print [1972, 1973, 1974, 1975]

# The network() function accepts a dictionary "servers" as a parameter.
def network(servers): 
    result = ""
    for hostname, IP_address in servers.items():
        result += "The IP address of the {} server is {}".format(hostname, IP_address) + "\n"
    return result 

print(network({"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}))

# Should print:
# The IP address of the Domain Name Server server is 8.8.8.8
# The IP address of the Gateway Server server is 192.168.1.1
# The IP address of the Print Server server is 192.168.1.33
# The IP address of the Mail Server server is 192.168.1.190

# The scores() function accepts a dictionary "game_scores" as a parameter.
def reset_scores(game_scores):
    new_game_scores = game_scores.copy() 
    for player, score in new_game_scores.items():
        new_game_scores[player] = 0
  
    return new_game_scores

game1_scores = {"Arshi": 3, "Catalina": 7, "Diego": 6}
 
print(reset_scores(game1_scores))
# Should print {'Arshi': 0, 'Catalina': 0, 'Diego': 0}