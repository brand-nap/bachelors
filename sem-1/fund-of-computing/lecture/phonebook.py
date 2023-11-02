def main():
    lastname = [];
    firstname = [];
    phoneNumber = []l
    print ("enter done for last, first and phone number to end input");
    last = input ("Give me your last name: ");
    first = input("Give me your first name: ");
    number = input ("Give me your phone number: ");


    while (last != "done" and first != "done" and number != "done"):
        lastname.append (last);
        firstname.append (first);
        phoneNumber.append (number);
        last = input ("Give me your last name: ");
        first = input("Give me your first name: ");
        number = input ("Give me your phone number: ");

    last = input ("what last name are you looking for?: ");
    first = input ("what first name are you looking for?: ");
