order=eval(input("enter order amount"))

discount=eval(input("enter discount"))

disval= order*(discount/100)

net= order-disval

print ("order was : " ,order, "now is : ",net)