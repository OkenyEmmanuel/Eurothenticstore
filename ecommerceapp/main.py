from .pay  import PayClass

callPay = PayClass.momopay("50", "EUR", "1234 test99", "256772677494", "THank you")
print(callPay["response"])
