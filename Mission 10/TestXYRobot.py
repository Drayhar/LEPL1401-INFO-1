import unittest
import XYRobot as XY

class TestTurtleBot(unittest.TestCase):

    def setUp(self):
        self.t = XY.XYRobot("tBot")

    def test_init(self):
        self.assertEqual(self.t.getangle(), 0,     "Your turtleBot is not facing EAST as expected")
        self.assertEqual(self.t.position(), (0,0), "Your turtleBot is not in 0,0 as expected")

    def test_turnleft(self):
        expected_position = self.t.position()
        expected_angle = (self.t.getangle() + 270)
        self.t.turnleft()
        # below we are using assertAlmostEqual instead if assertEqual to allow for inaccurate calculations
        self.assertAlmostEqual(self.t.getangle(), expected_angle, 1, "wrong angle")
        self.assertEqual(self.t.position(), expected_position, "Your turtleBot changed position while turning left")

    def test_turnright(self):
        expected_position = self.t.position()
        expected_angle = (self.t.getangle() + 90)
        self.t.turnright()
        self.assertAlmostEqual(self.t.getangle(), expected_angle, 1, "wrong angle")
        self.assertEqual(self.t.position(), expected_position, "Your turtleBot changed position while turning right")

    def test_turn(self):
        expected_position = self.t.position()
        expected_angle = self.t.getangle()
        self.t.turnleft()
        self.t.turnleft()
        self.t.turnright()
        self.t.turnright()
        self.assertAlmostEqual(self.t.getangle(), expected_angle, 1, "wrong angle")
        self.assertEqual(self.t.position(), expected_position, "Your turtleBot changed position while turning")

    def test_moveforward(self):
        forward = 50
        expected_position = (self.t.getx() + 50, self.t.gety())
        expected_angle = self.t.getangle()
        self.t.moveforward(50)
        self.assertEqual(self.t.position(), expected_position, "Your turtleBot has not moved forward "+str(forward)+" as expected")
        self.assertAlmostEqual(self.t.getangle(), expected_angle, 1, "wrong angle")

    def test_movebackward(self):
        backward = 50
        expected_position = (self.t.getx() - 50, self.t.gety())
        expected_angle = self.t.getangle()
        self.t.movebackward(50)
        self.assertEqual(self.t.position(), expected_position, "Your turtleBot has not moved backward "+str(backward)+" as expected")
        self.assertAlmostEqual(self.t.getangle(), expected_angle, 1, "wrong angle")

    def test_move(self):
        expected_position = self.t.position()
        expected_angle = self.t.getangle()
        self.t.moveforward(50)
        self.t.movebackward(10)
        self.t.movebackward(90)
        self.t.moveforward(50)
        self.assertAlmostEqual(self.t.getangle(), expected_angle, 1,"Your turtleBot took a wrong turn or did not update its angle")
        self.assertEqual(self.t.position(), expected_position, "Your turtleBot changed position while turning")

    def test_getHistory(self):
        self.t.moveforward(50)
        self.t.turnleft()
        expected_history = [("forward", 50), ("left", -90)]
        self.assertEqual(self.t.getHistory(), expected_history, "The History is not what it is supposed to be")

    def test_unplay(self):
        inital_position = (self.t.getx(), self.t.gety())
        inital_angle = self.t.getangle()
        self.t.moveforward(50)
        self.t.turnleft()
        self.t.moveforward(50)
        self.t.unplay()
        end_position = (self.t.getx(), self.t.gety())
        end_angle = self.t.getangle()
        self.assertEqual(inital_position, end_position, "The end position isn't good")
        self.assertAlmostEqual(inital_angle, end_angle, 0, "The angle at the end isn't good")

if __name__ == '__main__':
    unittest.main(verbosity=2)