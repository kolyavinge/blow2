import unittest
from blow.input.JoystickState import *

class JoystickStateTest(unittest.TestCase):
    
    def testConstructor(self):
        joy = JoystickState()
        self.assertFalse(joy.isLeftPressed())
        self.assertFalse(joy.isRightPressed())
        self.assertFalse(joy.isUpPressed())
        self.assertFalse(joy.isDownPressed())
        self.assertEquals([], joy.getPressedButtons())
        
    def testLeftPressRelease(self):
        joy = JoystickState()
        joy.pressLeft()
        self.assertTrue(joy.isLeftPressed())
        joy.releaseLeft()
        self.assertFalse(joy.isLeftPressed())
        
    def testRightPressRelease(self):
        joy = JoystickState()
        joy.pressRight()
        self.assertTrue(joy.isRightPressed())
        joy.releaseRight()
        self.assertFalse(joy.isRightPressed())
        
    def testUptPressRelease(self):
        joy = JoystickState()
        joy.pressUp()
        self.assertTrue(joy.isUpPressed())
        joy.releaseUp()
        self.assertFalse(joy.isUpPressed())
        
    def testDownPressRelease(self):
        joy = JoystickState()
        joy.pressDown()
        self.assertTrue(joy.isDownPressed())
        joy.releaseDown()
        self.assertFalse(joy.isDownPressed())

    def testPressReleaseButton(self):
        joy = JoystickState()
        joy.pressButton(2)
        self.assertTrue(joy.isButtonPressed(2))
        joy.releaseButton(2)
        self.assertFalse(joy.isButtonPressed(2))
        
    def testGetPressedButtons(self):
        joy = JoystickState()
        joy.pressButton(2)
        joy.pressButton(3)
        self.assertEquals([2, 3], joy.getPressedButtons())
    
    def testTwicePress(self):
        joy = JoystickState()
        joy.pressButton(2)
        joy.pressButton(2)
        self.assertEquals([2], joy.getPressedButtons())
    
    def testReleaseButton(self):
        joy = JoystickState()
        joy.releaseButton(2)
        self.assertEquals([], joy.getPressedButtons())
        
        
