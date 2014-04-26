#-*- coding: utf-8 -*-
"""
    test.digilent
    ~~~~~~~~~~~~~

    Test cases for digilent driver for Linux USB JTAG controller

    :copyright: (c) 2014 by Jessy Diamond Exum
    :license: Pending, see LICENSE for more details.
"""

import unittest
from bitarray import bitarray

from adapt.jtagStateMachine import JTAGStateMachine


class TestJtagStateMachine(unittest.TestCase):

    def setUp(self):
        """Emulate device connection"""
        pass

    def test_initialize_correct_defaults(self):
        sm = JTAGStateMachine()
        self.assertEquals(sm.state, "_PRE5")

    def test_set_state(self):
        sm = JTAGStateMachine()
        sm.state = "RTI"
        self.assertEqual(sm.state, "RTI")

        def assign_state_wrapper(sm, value):
            sm.state = value
        self.assertRaises(ValueError, assign_state_wrapper(sm, "RTI"))

    def test_transition_bit(self):
        """Assume the actual state list is correct because 
        otherwise we have a lot of transitions to test."""
        sm = JTAGStateMachine()
        sm.state = "CAPTUREDR"
        sm.transition_bit(True)
        self.assertEqual(sm.state, "EXIT1DR")
        sm.transition_bit(True)
        self.assertEqual(sm.state, "UPDATEDR")

        sm.state = "CAPTUREDR"
        sm.transition_bit(False)
        self.assertEqual(sm.state, "SHIFTDR")
        sm.transition_bit(False)
        self.assertEqual(sm.state, "SHIFTDR")
        sm.transition_bit(True)
        self.assertEqual(sm.state, "EXIT1DR")

    def test_calc_transition_to_state_changes_nothing(self):
        sm = JTAGStateMachine()
        self.assertEqual(sm.state, "_PRE5")
        sm.calc_transition_to_state("SHIFTDR")
        self.assertEqual(sm.state, "_PRE5")

    def test_invalid_calc_transition_to_state(self):
        sm = JTAGStateMachine()

        def do_bits(bits):
            for bit in bits[::-1]:
                sm.transition_bit(bit)

        self.assertRaises(ValueError, sm.calc_transition_to_state, ("INV"))

        #Test a path to _PRE5 is calculatable under initial conditions
        sm.state = "_PRE3"
        path = sm.calc_transition_to_state("_PRE5")
        self.assertEqual(path, bitarray('0'))
        do_bits(path)
        self.assertEqual(sm.state, "_PRE5")

        sm.state = "SHIFTDR"
        self.assertRaises(ValueError, sm.calc_transition_to_state, ("_PRE5"))

    def test_calc_transition_to_state(self):
        sm = JTAGStateMachine()

        def do_bits(bits):
            for bit in bits[::-1]:
                sm.transition_bit(bit)

        path = sm.calc_transition_to_state("RTI")
        self.assertEqual(path, bitarray('011111'))
        do_bits(path)
        self.assertEqual(sm.state, "RTI")
        
        path = sm.calc_transition_to_state("RTI")
        self.assertEqual(path, bitarray())
        do_bits(path)
        self.assertEqual(sm.state, "RTI")
        
        path = sm.calc_transition_to_state("TLR")
        self.assertEqual(path, bitarray('111'))
        do_bits(path)
        self.assertEqual(sm.state, "TLR")
        
        path = sm.calc_transition_to_state("SHIFTDR")
        self.assertEqual(path, bitarray('0010'))
        do_bits(path)
        self.assertEqual(sm.state, "SHIFTDR")
        
        path = sm.calc_transition_to_state("SHIFTIR")
        self.assertEqual(path, bitarray('001111'))
        do_bits(path)
        self.assertEqual(sm.state, "SHIFTIR")
