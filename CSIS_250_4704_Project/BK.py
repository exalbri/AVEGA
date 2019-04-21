# module to access all seral ports in PC.
import serial 

# Just some tests to show it's working. More code must be added.
if __name__ == '__main__':
    comport = raw_input("Enter the COM port for Power Supply: ")
    sup = Supply( ident = comport )
    time.sleep( 0.5 )
    sup.voltage( 0.0 )
    sup.enable()
# time.sleep(3.0)
    print( 'Reading', sup.reading())

    print( 'Maxima', sup.maxima())
    print( 'Settings', sup.settings())

    sup.disable()

    print( 'Disabled; reading', sup.reading())

    time.sleep( 2.0 )
    sup.voltage( 12.0 )
    sup.enable()


print( 'Enabled; reading', sup.reading())
time.sleep( 0.5 )
