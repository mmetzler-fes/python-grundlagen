def any_function(argument_1, argument_2="default value", *args, **kwargs):
	return argument_1, argument_2, args, kwargs

ergebnis=any_function("test", "11", 12,13, x=15,y=17)
#print (ergebnis)

my_list = [1,2,5,7]
even_numbers = map(lambda x: x * 2, my_list)
print(list(even_numbers))