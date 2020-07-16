from machine import Pin,I2C
class my_class:
  """这是一个简单的类"""
  i  = 12345
  
  def f(self):
    return 'hello gaoliang'
   
class my_complex:
  
  def __init__(self,x,y):
    self.r = x
    self.t = y
  
class my_max30100(object):
  def __init__(self):
    self.i2c = I2C(-1,scl=Pin(22), sda=Pin(23),freq=50000)
    self.i2c_address = self.i2c.scan()
    print(self.i2c.scan())
    
    
class my_oled1306(object):
  
  def __init__(self):
    self.i2c = I2C(-1,scl=Pin(17), sda=Pin(16),freq=50000)
    self.i2c_address = self.i2c.scan()[0]

    init_command = [0xae, 0x00, 0x10, 0x40, 0xb0, 0x81,
                    0xff, 0xa0, 0xa6, 0xa8, 0x3f, 0xc0,
                    0xd3, 0x00, 0xd5, 0x80, 0xd8, 0x05,
                    0xd9, 0xf1, 0xda, 0x12, 0xdb, 0x30,
                    0x8d, 0x14]
                    
    for i in init_command:
      self.i2c.writeto_mem(self.i2c_address, 0x00 , chr(i))
    self.clear()
    self.i2c.writeto_mem(self.i2c_address, 0x00 , chr(0xaf)) 

  def clear(self):
    for i in range(8):
      self.i2c.writeto_mem(self.i2c_address, 0x00, chr(0xb0+i))
      self.i2c.writeto_mem(self.i2c_address, 0x00, chr(0x00))
      self.i2c.writeto_mem(self.i2c_address, 0x00, chr(0x10))
      for n in range(128):
        self.i2c.writeto_mem(self.i2c_address, 0x40, chr(0x00))  
        
  def set_pos(self, x, y):
    if x<128 and y<8:
      self.i2c.writeto_mem(self.i2c_address, 0x00, chr(0xb0+y))
      self.i2c.writeto_mem(self.i2c_address, 0x00, chr(((x&0xf0)>>4)|0x10))
      self.i2c.writeto_mem(self.i2c_address, 0x00, chr(x&0x0f))
	        
  def char(self, x, y, ch):
    Font6x8  = [[0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                [0x00, 0x00, 0x00, 0x2f, 0x00, 0x00],
                [0x00, 0x00, 0x07, 0x00, 0x07, 0x00],
                [0x00, 0x14, 0x7f, 0x14, 0x7f, 0x14],
                [0x00, 0x24, 0x2a, 0x7f, 0x2a, 0x12],
                [0x00, 0x62, 0x64, 0x08, 0x13, 0x23],
                [0x00, 0x36, 0x49, 0x55, 0x22, 0x50],
                [0x00, 0x00, 0x05, 0x03, 0x00, 0x00],
                [0x00, 0x00, 0x1c, 0x22, 0x41, 0x00],
                [0x00, 0x00, 0x41, 0x22, 0x1c, 0x00],
                [0x00, 0x14, 0x08, 0x3E, 0x08, 0x14],
                [0x00, 0x08, 0x08, 0x3E, 0x08, 0x08],
                [0x00, 0x00, 0x00, 0xA0, 0x60, 0x00],
                [0x00, 0x08, 0x08, 0x08, 0x08, 0x08],
                [0x00, 0x00, 0x60, 0x60, 0x00, 0x00],
                [0x00, 0x20, 0x10, 0x08, 0x04, 0x02],
                [0x00, 0x3E, 0x51, 0x49, 0x45, 0x3E],
                [0x00, 0x00, 0x42, 0x7F, 0x40, 0x00],
                [0x00, 0x42, 0x61, 0x51, 0x49, 0x46],
                [0x00, 0x21, 0x41, 0x45, 0x4B, 0x31],
                [0x00, 0x18, 0x14, 0x12, 0x7F, 0x10],
                [0x00, 0x27, 0x45, 0x45, 0x45, 0x39],
                [0x00, 0x3C, 0x4A, 0x49, 0x49, 0x30],
                [0x00, 0x01, 0x71, 0x09, 0x05, 0x03],
                [0x00, 0x36, 0x49, 0x49, 0x49, 0x36],
                [0x00, 0x06, 0x49, 0x49, 0x29, 0x1E],
                [0x00, 0x00, 0x36, 0x36, 0x00, 0x00],
                [0x00, 0x00, 0x56, 0x36, 0x00, 0x00],
                [0x00, 0x08, 0x14, 0x22, 0x41, 0x00],
                [0x00, 0x14, 0x14, 0x14, 0x14, 0x14],
                [0x00, 0x00, 0x41, 0x22, 0x14, 0x08],
                [0x00, 0x02, 0x01, 0x51, 0x09, 0x06],
                [0x00, 0x32, 0x49, 0x59, 0x51, 0x3E],
                [0x00, 0x7C, 0x12, 0x11, 0x12, 0x7C],
                [0x00, 0x7F, 0x49, 0x49, 0x49, 0x36],
                [0x00, 0x3E, 0x41, 0x41, 0x41, 0x22],
                [0x00, 0x7F, 0x41, 0x41, 0x22, 0x1C],
                [0x00, 0x7F, 0x49, 0x49, 0x49, 0x41],
                [0x00, 0x7F, 0x09, 0x09, 0x09, 0x01],
                [0x00, 0x3E, 0x41, 0x49, 0x49, 0x7A],
                [0x00, 0x7F, 0x08, 0x08, 0x08, 0x7F],
                [0x00, 0x00, 0x41, 0x7F, 0x41, 0x00],
                [0x00, 0x20, 0x40, 0x41, 0x3F, 0x01],
                [0x00, 0x7F, 0x08, 0x14, 0x22, 0x41],
                [0x00, 0x7F, 0x40, 0x40, 0x40, 0x40],
                [0x00, 0x7F, 0x02, 0x0C, 0x02, 0x7F],
                [0x00, 0x7F, 0x04, 0x08, 0x10, 0x7F],
                [0x00, 0x3E, 0x41, 0x41, 0x41, 0x3E],
                [0x00, 0x7F, 0x09, 0x09, 0x09, 0x06],
                [0x00, 0x3E, 0x41, 0x51, 0x21, 0x5E],
                [0x00, 0x7F, 0x09, 0x19, 0x29, 0x46],
                [0x00, 0x46, 0x49, 0x49, 0x49, 0x31],
                [0x00, 0x01, 0x01, 0x7F, 0x01, 0x01],
                [0x00, 0x3F, 0x40, 0x40, 0x40, 0x3F],
                [0x00, 0x1F, 0x20, 0x40, 0x20, 0x1F],
                [0x00, 0x3F, 0x40, 0x38, 0x40, 0x3F],
                [0x00, 0x63, 0x14, 0x08, 0x14, 0x63],
                [0x00, 0x07, 0x08, 0x70, 0x08, 0x07],
                [0x00, 0x61, 0x51, 0x49, 0x45, 0x43],
                [0x00, 0x00, 0x7F, 0x41, 0x41, 0x00],
                [0x00, 0x55, 0x2A, 0x55, 0x2A, 0x55],
                [0x00, 0x00, 0x41, 0x41, 0x7F, 0x00],
                [0x00, 0x04, 0x02, 0x01, 0x02, 0x04],
                [0x00, 0x40, 0x40, 0x40, 0x40, 0x40],
                [0x00, 0x00, 0x01, 0x02, 0x04, 0x00],
                [0x00, 0x20, 0x54, 0x54, 0x54, 0x78],
                [0x00, 0x7F, 0x48, 0x44, 0x44, 0x38],
                [0x00, 0x38, 0x44, 0x44, 0x44, 0x20],
                [0x00, 0x38, 0x44, 0x44, 0x48, 0x7F],
                [0x00, 0x38, 0x54, 0x54, 0x54, 0x18],
                [0x00, 0x08, 0x7E, 0x09, 0x01, 0x02],
                [0x00, 0x18, 0xA4, 0xA4, 0xA4, 0x7C],
                [0x00, 0x7F, 0x08, 0x04, 0x04, 0x78],
                [0x00, 0x00, 0x44, 0x7D, 0x40, 0x00],
                [0x00, 0x40, 0x80, 0x84, 0x7D, 0x00],
                [0x00, 0x7F, 0x10, 0x28, 0x44, 0x00],
                [0x00, 0x00, 0x41, 0x7F, 0x40, 0x00],
                [0x00, 0x7C, 0x04, 0x18, 0x04, 0x78],
                [0x00, 0x7C, 0x08, 0x04, 0x04, 0x78],
                [0x00, 0x38, 0x44, 0x44, 0x44, 0x38],
                [0x00, 0xFC, 0x24, 0x24, 0x24, 0x18],
                [0x00, 0x18, 0x24, 0x24, 0x18, 0xFC],
                [0x00, 0x7C, 0x08, 0x04, 0x04, 0x08],
                [0x00, 0x48, 0x54, 0x54, 0x54, 0x20],
                [0x00, 0x04, 0x3F, 0x44, 0x40, 0x20],
                [0x00, 0x3C, 0x40, 0x40, 0x20, 0x7C],
                [0x00, 0x1C, 0x20, 0x40, 0x20, 0x1C],
                [0x00, 0x3C, 0x40, 0x30, 0x40, 0x3C],
                [0x00, 0x44, 0x28, 0x10, 0x28, 0x44],
                [0x00, 0x1C, 0xA0, 0xA0, 0xA0, 0x7C],
                [0x00, 0x44, 0x64, 0x54, 0x4C, 0x44],
                [0x00, 0x00, 0x10, 0xFE, 0x82, 0x00],
                [0x00, 0x00, 0x00, 0xFF, 0x00, 0x00],
                [0x00, 0x82, 0xFE, 0x10, 0x00, 0x00],
                [0x02, 0x01, 0x01, 0x02, 0x02, 0x01]]
    i = 0
    c = ord(ch)-32
    if c < 99:
      self.set_pos(x,y)
    for i in range(6):
      self.i2c.writeto_mem(self.i2c_address, 0x40, chr(Font6x8[c][i]))
	
  def string(self, x, y, buf):
    for i in buf:
      if i == '\0':
        break
      self.char(x, y, i)
      x = x + 6;
      if x>122:
        x = 0
        y = y + 1
