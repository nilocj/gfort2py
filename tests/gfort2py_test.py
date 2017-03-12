import os, sys
import numpy as np
import gfort2py as gf
import unittest2 as unittest
import subprocess
import numpy.testing as np_test

os.chdir('tests')
subprocess.check_output(["make"])
x=gf.fFort('./tester.so','tester.mod',reload=True)


class TestStringMethods(unittest.TestCase):
	
	def test_mising_var(self):	
		with self.assertRaises(AttributeError) as cm:
			a=x.invalid_var
	
	def test_a_str(self):
		v='123456798'
		x.a_str=v
		self.assertEqual(x.a_str,v)
		
	def test_a_str_bad_length(self):
		v='132456789kjhgjhf'
		x.a_str=v
		self.assertEqual(x.a_str,v[0:10])
		
	def test_a_int(self):
		v=1
		x.a_int=v
		self.assertEqual(x.a_int,v)
		
	def test_a_int_str(self):
		with self.assertRaises(ValueError) as cm:
			x.a_int='abc'
			
	def test_a_real(self):
		v=1.0
		x.a_real=v
		self.assertEqual(x.a_real,v)
	
	def test_a_real_str(self):	
		with self.assertRaises(ValueError) as cm:
			x.a_real='abc'
			
	def test_const_int_set(self):	
		with self.assertRaises(ValueError) as cm:
			x.const_int=2
			
	def test_const_int(self):	
		self.assertEqual(x.const_int,1)	

	def test_const_int_p1(self):	
		self.assertEqual(x.const_int_p1,2)	

	def test_const_int_long(self):	
		self.assertEqual(x.const_int_lp,1)	

	def test_const_real_dp(self):	
		self.assertEqual(x.const_real_dp,1.0)
		
	def test_const_real_qp(self):	
		self.assertEqual(x.const_real_qp,1.0)

	def test_const_int_arr_error(self):	
		with self.assertRaises(ValueError) as cm:
			x.const_int_arr='abc'
		
	def test_const_int_arr(self):	
		np_test.assert_array_equal(x.const_int_arr,np.array([1,2,3,4,5,6,7,8,9,0],dtype='int'))

	def test_const_real_arr(self):	
		np_test.assert_array_equal(x.const_real_arr,np.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,0.0],dtype='float'))

	def test_const_dp_arr(self):	
		np_test.assert_array_equal(x.const_real_dp_arr,np.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,0.0],dtype='float'))

	def test_b_int_exp_1d(self):
		v=np.random.randint(0,100,size=(5))
		x.b_int_exp_1d=v
		np_test.assert_array_equal(x.b_int_exp_1d,v)
		
	def test_b_int_exp_2d(self):
		v=np.random.randint(0,100,size=(5,5))
		x.b_int_exp_2d=v
		np_test.assert_array_equal(x.b_int_exp_2d,v)
		
	def test_b_int_exp_3d(self):
		v=np.random.randint(0,100,size=(5,5,5))
		x.b_int_exp_3d=v
		np_test.assert_array_equal(x.b_int_exp_3d,v)
		
	def test_b_int_exp_4d(self):
		v=np.random.randint(0,100,size=(5,5,5,5))
		x.b_int_exp_4d=v
		np_test.assert_array_equal(x.b_int_exp_4d,v)
		
	def test_b_int_exp_5d(self):
		v=np.random.randint(0,100,size=(5,5,5,5,5))
		x.b_int_exp_5d=v
		np_test.assert_array_equal(x.b_int_exp_5d,v)
		
	def test_b_real_exp_1d(self):
		v=np.random.random(size=(5))
		x.b_real_exp_1d=v
		np_test.assert_allclose(x.b_real_exp_1d,v)
		
	def test_b_real_exp_2d(self):
		v=np.random.random(size=(5,5))
		x.b_real_exp_2d=v
		np_test.assert_allclose(x.b_real_exp_2d,v)
		
	def test_b_real_exp_3d(self):
		v=np.random.random(size=(5,5,5))
		x.b_real_exp_3d=v
		np_test.assert_allclose(x.b_real_exp_3d,v)
		
	def test_b_real_exp_4d(self):
		v=np.random.random(size=(5,5,5,5))
		x.b_real_exp_4d=v
		np_test.assert_allclose(x.b_real_exp_4d,v)
		
	def test_b_real_exp_5d(self):
		v=np.random.random(size=(5,5,5,5,5))
		x.b_real_exp_5d=v
		np_test.assert_allclose(x.b_real_exp_5d,v)
		
	def test_b_real_dp_exp_1d(self):
		v=np.random.random(size=(5))
		x.b_real_dp_exp_1d=v
		np_test.assert_allclose(x.b_real_dp_exp_1d,v)
		
	def test_b_real_dp_exp_2d(self):
		v=np.random.random(size=(5,5))
		x.b_real_dp_exp_2d=v
		np_test.assert_allclose(x.b_real_dp_exp_2d,v)
		
	def test_b_real_dp_exp_3d(self):
		v=np.random.random(size=(5,5,5))
		x.b_real_dp_exp_3d=v
		np_test.assert_allclose(x.b_real_dp_exp_3d,v)
		
	def test_b_real_dp_exp_4d(self):
		v=np.random.random(size=(5,5,5,5))
		x.b_real_dp_exp_4d=v
		np_test.assert_allclose(x.b_real_dp_exp_4d,v)
		
	def test_b_real_dp_exp_5d(self):
		v=np.random.random(size=(5,5,5,5,5))
		x.b_real_dp_exp_5d=v
		np_test.assert_allclose(x.b_real_dp_exp_5d,v)

	def test_a_int_point(self):
		v=1
		x.a_int_point=v
		self.assertEqual(x.a_int_point,v)

	def test_a_int_lp_point(self):
		v=1
		x.a_int_lp_point=v
		self.assertEqual(x.a_int_lp_point,v)

	def test_a_real_point(self):
		v=1.0
		x.a_real_point=v
		self.assertEqual(x.a_real_point,v)
		
	def test_a_real_dp_point(self):
		v=1.0
		x.a_real_dp_point=v
		self.assertEqual(x.a_real_dp_point,v)
		
	def test_a_real_qp_point(self):
		v=1.0
		x.a_real_qp_point=v
		self.assertEqual(x.a_real_qp_point,v)
		
	def test_a_str_point(self):
		v='abcdefghij'
		x.a_str_point=v
		self.assertEqual(x.a_str_point,v)

	def test_a_int_target(self):
		v=1
		x.a_int_target=v
		self.assertEqual(x.a_int_target,v)

	def test_a_int_lp_target(self):
		v=1
		x.a_int_lp_target=v
		self.assertEqual(x.a_int_lp_target,v)

	def test_a_real_target(self):
		v=1.0
		x.a_real_target=v
		self.assertEqual(x.a_real_target,v)
		
	def test_a_real_dp_target(self):
		v=1.0
		x.a_real_dp_target=v
		self.assertEqual(x.a_real_dp_target,v)
		
	def test_a_real_qp_target(self):
		v=1.0
		x.a_real_qp_target=v
		self.assertEqual(x.a_real_qp_target,v)
		
	def test_a_str_target(self):
		v='abcdefghij'
		x.a_str_target=v
		self.assertEqual(x.a_str_target,v)



if __name__ == '__main__':
	unittest.main() 



