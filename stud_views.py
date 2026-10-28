import mysql.connector
import datetime


class con_db:
    def get_connect(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Priyan@07",
                database="student_management"
            )
            return self.con
        except Exception as e:
            return None


class StudentManager(con_db):

    def get(self):
        try:
            self.connect = super().get_connect()
            self.cursor = self.connect.cursor()

            query = "select * from student"

            self.cursor.execute(query)

            r = self.cursor.fetchall()

            print(r)

        except Exception as e:
            print(e)

    def post(self, **kwargs):
        try:
            self.connect = super().get_connect()
            self.cursor = self.connect.cursor()

            query = """insert into student
            (name, age, gender, mobile, email, course, admission_date)
            values(%s,%s,%s,%s,%s,%s,%s)"""

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)

            self.connect.commit()

            print("student added successfully")

        except Exception as e:
            print(e)

    def get_one(self, id=None):
        try:
            self.connect = super().get_connect()
            self.cursor = self.connect.cursor()

            query = "select * from student where id=%s"

            values = (id,)

            self.cursor.execute(query, values)

            r = self.cursor.fetchone()

            return r

        except Exception as e:
            return None

    def dele(self, id=None):
        try:
            r = self.get_one(id=id)

            if r != None:

                self.connect = super().get_connect()
                self.cursor = self.connect.cursor()

                query = "delete from student where id=%s"

                values = (id,)

                self.cursor.execute(query, values)

                self.connect.commit()

                print("student deleted successfully")

            else:
                print("404")

        except Exception as e:
            print(e)

    def update(self, id=None, **kwargs):
        try:
            r = self.get_one(id=id)

            if r != None:

                self.connect = super().get_connect()
                self.cursor = self.connect.cursor()

                placeholder = ""

                for k in kwargs:
                    placeholder += k + "=%s, "

                placeholder = placeholder.rstrip(", ")

                query = f"update student set {placeholder} where id=%s"

                values = [v for v in kwargs.values()]

                values.append(id)

                self.cursor.execute(query, values)

                self.connect.commit()

                print("student updated successfully")

            else:
                print("404")

        except Exception as e:
            print(e)


student = StudentManager()

# READ
# student.get()

# CREATE
# student.post(
#     name="Rahul",
#     age=21,
#     gender="Male",
#     mobile="9876543210",
#     email="rahul@gmail.com",
#     course="BCA",
#     admission_date=datetime.date.today()
# )

# READ ONE
# print(student.get_one(id=1))

# UPDATE
# student.update(
#     id=1,
#     course="Python Full Stack",
#     email="rahul_new@gmail.com"
# )

# DELETE
# student.dele(id=1)