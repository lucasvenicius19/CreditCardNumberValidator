class CardNumber:
    def __init__(self):
        self.credit_card_number = self.get_valid_credit_card_number()
        
    
    def get_valid_credit_card_number(self):
        while True:
                # Ask user credit card number
                user_input = input("Enter your credit card number: ")
                if self.is_valid_credit_card_number(user_input):
                    return int(user_input)
                else:
                    print("Invalid input! Credit card number must be at least 13 DIGITS and at maximum 16 DIGITS!")
                    
                    
    def is_valid_credit_card_number(self, number):
        return number.isdigit() and 13 <= len(number) <= 16
                        

    def isolate_digits(self):
        # Isolating each digit from the right most to the left most digit
        self.card_length = str(self.credit_card_number)
        self.digits = [int(d) for d in self.card_length[::-1]]

    
    def multiplying_even_positioned_digits(self):
        for i in range(1, len(self.digits), 2):
            self.digits[i] *= 2
        
        
    def check_products(self):
        for i in range(1, len(self.digits), 2):
            if self.digits[i] >= 10:
                self.digits[i] = self.digits[i] // 10 + self.digits[i] % 10
         
            
    def add_products(self):
        self.sum_products = sum(self.digits[1::2])
        
        
    def final_sum(self):
        self.sum = sum(self.digits[::2]) + self.sum_products
        
        
    def check_sum_final_digit(self):
        return self.sum % 10 == 0
            
            
    def check_starting_digits(self):
        card_length = len(self.card_length)
        if card_length == 15 and (
            self.card_length.startswith("34") or 
            self.card_length.startswith("37")
        ):
            return "AMEX\n"
        elif card_length == 16 and (
            self.card_length.startswith("51") or 
            self.card_length.startswith("52") or 
            self.card_length.startswith("53") or 
            self.card_length.startswith("54") or 
            self.card_length.startswith("55")
        ):
            return "MASTER\n"
        elif (
            (card_length == 13 or card_length == 16) and 
            self.card_length.startswith("4")
        ):
            return "VISA\n"
        else:
            return "INVALID\n"
           
        
    def validate_credit_card(self):
        self.isolate_digits()
        self.multiplying_even_positioned_digits()
        self.check_products()
        self.add_products()
        self.final_sum()
        if self.check_sum_final_digit():
            card_type = self.check_starting_digits()
            return card_type
        else:
            return "INVALID\n"


if __name__ == "__main__":
    card_type= CardNumber().validate_credit_card()
    print(card_type)
