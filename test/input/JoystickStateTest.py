import unittest
from blow.input.JoystickState import *

class JoystickStateTest(unittest.TestCase):
    
    def setUp(self):
        self.joy = JoystickState()
    
    def testConstructor(self):
        self.assertEquals([], self.joy.getPressed())
        self.assertEquals([], self.joy.getHolded())

    def testPressHoldRelease(self):
        self.joy.press(JoystickButton_Up)
        self.assertTrue(self.joy.isPressed(JoystickButton_Up))
        self.assertFalse(self.joy.isHolded(JoystickButton_Up))
        self.assertFalse(self.joy.isReleased(JoystickButton_Up))
        
        self.joy.hold(JoystickButton_Up)
        self.assertFalse(self.joy.isPressed(JoystickButton_Up))
        self.assertTrue(self.joy.isHolded(JoystickButton_Up))
        self.assertFalse(self.joy.isReleased(JoystickButton_Up))
        
        self.joy.release(JoystickButton_Up)
        self.assertFalse(self.joy.isPressed(JoystickButton_Up))
        self.assertFalse(self.joy.isHolded(JoystickButton_Up))
        self.assertTrue(self.joy.isReleased(JoystickButton_Up))

    def testPressRelease(self):
        self.joy.press(JoystickButton_Up)
        self.assertTrue(self.joy.isPressed(JoystickButton_Up))
        self.assertFalse(self.joy.isHolded(JoystickButton_Up))
        self.assertFalse(self.joy.isReleased(JoystickButton_Up))
        
        self.joy.release(JoystickButton_Up)
        self.assertFalse(self.joy.isPressed(JoystickButton_Up))
        self.assertFalse(self.joy.isHolded(JoystickButton_Up))
        self.assertTrue(self.joy.isReleased(JoystickButton_Up))

    def testPressTwice(self):
        self.joy.press(JoystickButton_Up)
        self.joy.press(JoystickButton_Up)
        self.assertTrue(self.joy.isPressed(JoystickButton_Up))
        self.assertEquals([JoystickButton_Up], self.joy.getPressed())
    
    def testSetPressedAsHolded(self):
        self.joy.press(JoystickButton_Up)
        self.joy.press(JoystickButton_1)
        self.joy.setPressedAsHolded()
        self.assertFalse(self.joy.isPressed(JoystickButton_Up))
        self.assertFalse(self.joy.isPressed(JoystickButton_1))
        self.assertTrue(self.joy.isHolded(JoystickButton_Up))
        self.assertTrue(self.joy.isHolded(JoystickButton_1))
    
    def testSetPressedAsHolded2(self):
        self.joy.press(JoystickButton_Up)
        self.joy.setPressedAsHolded()
        
        self.joy.press(JoystickButton_1)
        self.joy.setPressedAsHolded()
        
        self.assertTrue(self.joy.isHolded(JoystickButton_Up))
        self.assertTrue(self.joy.isHolded(JoystickButton_1))
        
    def testHoldNotPressedButton(self):
        self.assertRaises(JoystickError, lambda: self.joy.hold(JoystickButton_Up))
    
    def testPressHoldedButton(self):
        self.joy.press(JoystickButton_Up)
        self.joy.hold(JoystickButton_Up)
        self.assertRaises(JoystickError, lambda: self.joy.press(JoystickButton_Up))


