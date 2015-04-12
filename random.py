# Python program...

greeting = "lulzors" #create variable
print greeting #Print the variable

word = "This is a sentence."
print word
print word[0]
print word[1]
print word[2]

a = "10"
b = "20.999"
c = a + b

print c

a = 10
b = 666.69
c = a + b

print c

# case sensitive. GREETING =/= Greeting =/= greetinG etc

# Numeric Literals written without a decimal point are considered integers.
# Numeric Literals written WITH a decimal point are considered floats.

something = "Hello"
something_else = "Bye"

print "This string goes before the rest, dawg:",something,something_else

# Stuff to print is separated by a comma. Number of spaces is irrelevant.
# Literal Strings work as input.

a_thing = "Napoleon"

print "The name is: %s. Don't forget it!" %a_thing
print 'The name is: %s. Don\'t forget it!' %a_thing

y = [“%s=%s” % (k, v) for k, v in params.items()]
