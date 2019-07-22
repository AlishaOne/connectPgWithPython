import unittest

import psycopg2


class UserTableTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        try:
            self.connection = psycopg2.connect(dbname='test', user='postgres', password='postgres', host='localhost',
                                               port='5432')  # for role as postgres, password is not needed
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            print("You are connected to - ", record, "\n")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def get_row_col(self, rows, field_index):
        for row in rows:
            yield list(row).pop(field_index)

    def test_user_table_row_data_correct(self):
        print("-------testing start-------")
        self.expect_user = [('Test', 'Z', 'test@gmail.com', True),
                            ('gz', 'z', 'gz@gz.com', True),
                            ('AnonymousUser', 'Z', 'AnonymousUser@anonymoususer.com', False)]

        sql = "SELECT first_name,last_name,email,is_staff FROM user;"
        self.cursor.execute(sql)
        self.rows = list(self.cursor.fetchall())
        self.total_rows = len(self.rows)
        print(f'Total rows: {self.total_rows}')
        print(f'all of the records from user table: {self.rows}')

        # Check is each row field correct TODO 
        for row in self.rows:
            for i in range(0, 4):
                print("******************** actual data *********************")
                print(f' actal data, row  {i} field, value is {list(row).pop(i)}')
                self.expect_col = list(row).pop(i)
                self.actual_col = next(self.get_row_col(self.expect_user, i))
                print(f'XXXXX expect data : {self.actual_col}')
                # assert self.expect_col == self.actual_col

        # Check is each row correct
        for j in range(0, self.total_rows):
            print("++++++++++++++++++++++++++++++++++++++++++++++++++")
            self.actual_row = list(self.rows[j])
            print(f'actual: {self.actual_row}')
            self.expect_row = list(self.expect_user[j])
            print(f'expect: {self.expect_row}')
            assert self.expect_row == self.actual_row

        # check one row's data
        # first_name = list(self.rows[2]).pop(0)
        # last_name = list(self.rows[2]).pop(1)
        # email = list(self.rows[2]).pop(2)
        # is_staff = list(self.rows[2]).pop(3)
        # print(f'Expect data is: {expect_user}')
        # print(f'Database data is: {list(rows[2])}')
        # assert first_name == expect_user[0]
        # assert last_name == expect_user[1]
        # assert email == expect_user[2]
        # assert is_staff == expect_user[3]
        # assert expect_user == list(rows[2])

    def tearDown(self):
        # closing database connection.
        if (self.connection):
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")
