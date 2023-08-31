#class Company:
    #attributes: name, founding_year
    #relationships: freebies, devs

    #method give_freebie(dev, item_name, value):
        #create a new Freebie with dev, item_name, value, and this company
        #add the new Freebie to the company's freebies
        #commit changes

    #class method oldest_company():
        #return the company with the earliest founding year

#class Dev:
    #attributes: name
    #relationships: freebies, companies

    #method received_one(item_name):
        #for each freebie in dev's freebies:
            #if freebie has item_name:
                #return True
        #return False

    #method give_away(other_dev, freebie):
        #if freebie's dev is this dev:
            #change freebie's dev to other_dev
            #commit changes

#class Freebie:
    #attributes: dev, company, item_name, value
    #relationships: dev, company

    method print_details():
        return formatted string with dev's name, item_name, and company's name

# Sample usage
create instances of Company, Dev
company.give_freebie(dev, item_name, value)
oldest_company = Company.oldest_company()
received = dev.received_one(item_name)
freebie_details = freebie.print_details()
dev.give_away(other_dev, freebie)
