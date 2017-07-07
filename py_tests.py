import unittest,coverage,os
import sqlss, data
#sub class of TestCase... used to define tests
class Test_sqlite(unittest.TestCase):
    a=True
    # test that checks sqlite table creation
    def test_create(self):
        obj=sqlss.dbs()
        str = obj.create_table("database", data.json)
        self.assertEqual("created", str)


    # test that check data insertion
    @unittest.skip("")   #skipping the test
    def test_insert(self):
        obj=sqlss.dbs()
        self.assertEqual("inserted",obj.insert("database",data.json_insert))

    def suite():
        suite=unittest.TestSuite()
        suite.addTest(Test_sqlite('test_create'))
        suite.addTest(Test_sqlite('test_insert'))
        return suite


#  coverage API 
def cov():
    """Runs the unit tests with coverage."""
    cov = coverage.coverage()
    cov.start()
    """ runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)"""
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_sqlite)
    unittest.TextTestRunner(verbosity=2).run(suite)

    cov.stop()
    cov.save()
    print ('Coverage Summary:'
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'coverage')
    cov.html_report(directory=covdir)
    cov.load()
    c=coverage.CoverageData()

    cov.erase()
	
	
if __name__ == '__main__':
    cov()


