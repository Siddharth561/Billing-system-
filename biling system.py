#:< using right side space
#:> use left space
#:^ use middle space
#"-"* use line
#" "* use space of title

item={
      1:"tea",
      2:"poha",
      3:"vadapav",
      4:"samosa",
      5:"idli",
      6:"dhosa",
      7:"misal",
      8:"pavbhaji"
    } 
price={
    1:10,
    2:40,
    3:20,
    4:60,
    5:80,
    6:10,
    7:70,
    8:18
    }
ikey=[]
item_quant=[]
print("-"*95)
print(" "*40," SK SNAKS")
print("-"*95)
while True:
    print(""" 
                    Menu
        1.tea               2.poha
        3.vadapav           4.samosa
        5.idli              6.dhosa
        7.misal             8.pavbhaji
    """)
   
    sel_item = int(input("enter your choice :"))
    quantity = int(input("enter quantity :"))
    # ikey.append(sel_item)
    item_quant.append({sel_item:quantity})
    user_choice = input(" do you want continune  : ")
    ttl_price = 0
    ttl_qty = 0
    ttl_bill = 0
    if user_choice=="n":
        print("-"*80)
        print("|{:<20}|{:<20}|{:<20}|{:<20}".format("item", "price", "quantity", "amount"))
        print("-"*80)
        
        length = len(item_quant)
        index = 0
        for i in item_quant:
            index +=1
            item_key = i.keys()
            price_key =i.values()
            i_key = next(iter(item_key))
            p_key = next(iter(price_key))

            ttl_price += price[i_key]
            ttl_qty += p_key
            ttl_bill += (int(price[i_key]) * int(p_key))
            
            print("|{:<20}|{:<20}|{:<20}|{:<20}".format(item[i_key], price[i_key], p_key ,int(price[i_key]) * int(p_key) ))
            if length == index:
                print("-" * 80)
                print("|{:<20}|{:<20}|{:<20}|{:<20}".format("Total",ttl_price, ttl_qty,ttl_bill))
                print("-" * 80)
        break
   
    

   
    # index = 0
    # for i in quant:
        # print(i)
        # print(f"item{ikey[index]},price{ikey[index]},qun{ikey[index]},price{ikey[index]},amount{ikey[index]}")
        # index += 1
        #  sum=sum+price(ikey[ikey])*quant(ikey[ikey])
    
    