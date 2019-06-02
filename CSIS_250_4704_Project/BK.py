
from __future__ import division
import serial
import time
import decimal
import telnetlib

def _str2num( num, factor = 10 ):
    """Takes a number in the supply's format, which always has one
    decimal place, and returns a decimal number reflecting it.
    """
    return decimal.Decimal( num ) / factor

def _num2str( s, length = 3, factor = 10 ):
    """Turns a number, which may be a decimal, integer, or float,
    and turns it into a supply-formatted string.
    """
    dec = decimal.Decimal( s )
    return ( '%0' + str( length ) + 'i' ) % int( dec * factor )

def _numfields( s, fields, factor = 10 ):
    """
    Generates numbers of the given lengths in the string.
    """
    pos = 0
    for field in fields:
        yield _str2num( s[pos:pos + field], factor )
        pos += field

class Supply( object ):
    def __init__( self, tel = None, ident = None ):
        self.ident = ident
        self.tel = tel
        if not ident == None:
            ident = ident.lower()
            if ( ident.startswith( "com" ) ):
                self.ser = serial.Serial( ident, 9600, 8, 'N', 1 )
                self.ser.timeout = 10
        elif not tel == None:
            self.tel = telnetlib.Telnet()
            self.tel.open( tel, 15 )
            self.tel.read_until( 'Login ' )
            self.tel.write( 'dvttst\n' )
            time.sleep( 0.2 )
            self.tel.read_until( 'Password' )
            self.tel.write( 'dvttst\n' )
            self.tel.read_until( 'menu' )
        else:
            raise TypeError( "None Type cannot used to initiate Power Supply" )

    def togglePowerSupply( self , duration = 0 ):
        self.disable()
        time.sleep( duration )
        self.enable()


    def command( self, code, param = '', address = '00' ):
        # Put this communication in an isolated little transaction.
        if not self.ident == None:
            self.ser.flushInput()
            self.ser.flushOutput()

            self.ser.write( code + address + param + "\r" )
            self.ser.flush()
        elif not self.tel == None:
            self.tel.write( code + address + param + "\r" )
        out = None
        while True:
            # Read until CR.
            resp = ''
            # resp = self.tel.rawq_getchar()
            while True:
                if not self.ident:
                    char = self.tel.rawq_getchar()
                else:
                    char = self.ser.read()
                if char == '\r':
                    break
                else:
                    resp += char


            if resp == 'OK':
                return out

            if out is not None:
                # print 'received more than one line of output without OK!'
                return resp

            out = resp

    def start( self ):
        self.command( 'SESS' )
    def close( self ):
        self.command( 'ENDS' )
    def voltage( self, volts ):
        self.command( 'VOLT', _num2str( volts ) )
    def reading( self ):
        resp = self.command( 'GETD' )
        volts, amps = _numfields( resp, ( 4, 4 ), 1 )
        return volts / 100, amps / 1000
    def maxima( self ):
        resp = self.command( 'GMAX' )
        return tuple( _numfields( resp, ( 3, 3 ) ) )
    def settings( self ):
        resp = self.command( 'GETS' )
        return tuple( _numfields( resp, ( 3, 3 ) ) )
    def enable( self ):
        """Enable output."""
        self.command( 'SOUT', '0' )
    def disable( self ):
        """Disable output."""
        self.command( 'SOUT', '1' )

    def __del__( self ):
        self.close()
        if not self.tel == None:
            self.tel.close()
        else:
            self.ser.close()

# Just some tests to show it's working.
if __name__ == '__main__':
    comport = raw_input("Enter the COM port for Power Supply: ")
    sup = Supply( ident = comport )
    time.sleep( 0.5 )
    sup.voltage( 0.0 )
    sup.enable()
#    time.sleep(3.0)
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
