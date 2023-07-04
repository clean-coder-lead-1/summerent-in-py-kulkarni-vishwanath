import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
    """Unit tests for typewise_alert module.
    """

    def test_infers_breach_as_per_limits(self):
      """Test the breach based on temperature range and threshold.
      """
      self.assertTrue(typewise_alert.infer_breach(20, [50,100]) == 'TOO_LOW')   
      self.assertTrue(typewise_alert.infer_breach(120, [50,100]) == 'TOO_HIGH')
      self.assertTrue(typewise_alert.infer_breach(70, [50,100]) == 'NORMAL')
    
    def test_infers_breach_as_per_limits_border_cases(self):
      """Test the breach based on temperature range and threshold considering the borderline cases.
      """
      self.assertTrue(typewise_alert.infer_breach(50, [50,100]) == 'NORMAL')
      self.assertTrue(typewise_alert.infer_breach(100, [50,100]) == 'NORMAL')
    
    def test_classify_temperature_breach_passive(self):
      """Test the classify temperature breach function based on passive cooling.
      """
      self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING",40) == 'TOO_HIGH')
      self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING",-10) == 'TOO_LOW')
      self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING",35) == 'NORMAL')

    def test_classify_temperature_breach_med_active(self):
      """Test the classify temperature breach function based on medium active cooling.
      """
      self.assertTrue(typewise_alert.classify_temperature_breach("MED_ACTIVE_COOLING",50) == 'TOO_HIGH')
      self.assertTrue(typewise_alert.classify_temperature_breach("MED_ACTIVE_COOLING",-10) == 'TOO_LOW')
      self.assertTrue(typewise_alert.classify_temperature_breach("MED_ACTIVE_COOLING",40) == 'NORMAL')
    
    def test_classify_temperature_breach_hi_active(self):
      """Test the classify temperature breach function based on Hi active cooling.
      """
      self.assertTrue(typewise_alert.classify_temperature_breach("HI_ACTIVE_COOLING",50) == 'TOO_HIGH')
      self.assertTrue(typewise_alert.classify_temperature_breach("HI_ACTIVE_COOLING",-10) == 'TOO_LOW')
      self.assertTrue(typewise_alert.classify_temperature_breach("HI_ACTIVE_COOLING",45) == 'NORMAL')

    def test_send_to_email(self):
      """Test the send to email function.
      """
      self.assertIn("TOO_LOW",typewise_alert.send_to_email("TOO_LOW"))
      self.assertIn("TOO_HIGH",typewise_alert.send_to_email("TOO_HIGH"))

    def test_send_to_controller(self):
      """Test the send to controller function.
      """
      self.assertIn("TOO_LOW",typewise_alert.send_to_controller("TOO_LOW"))
      self.assertIn("TOO_HIGH",typewise_alert.send_to_controller("TOO_HIGH"))
    
   


if __name__ == '__main__':
  unittest.main()
