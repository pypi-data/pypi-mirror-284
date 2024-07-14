import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.automap
import os
import sys
import contextlib
import json
import zipfile
import io


# will be placed in CWD and not overwritten
OUTZIP="dban-generated-stub.zip"



if not os.path.isfile(".env") and "DBNAME" not in os.environ.keys():
    sys.stderr.write("""

#bash env file for sourcing

export DBUSER=root
export DBPASS=foo123
export DBHOST=localhost
export DBPORT=33060
export DBNAME=testdb
export DBCAFILENAME=

#or      

DBUSER=root
DBPASS=foo123
DBHOST=localhost
DBPORT=33060
DBNAME=testdb
DBCAFILENAME=





""")
    sys.stderr.flush()
    sys.exit(1)

if os.path.isfile(OUTZIP):
    sys.stderr.write("error wil not overwrite %s\n" % OUTZIP)
    sys.stderr.flush()
    sys.exit(1)



class OrgModeSection:


    def __init__(self, title) -> None:
        self._title = title
        self._subsections = []
        self._lines = []


    def add_subsection(self, title):
        self._subsections.append(OrgModeSubSection(title=title))
        self._lines = []
        return self._subsections[-1]


class OrgModeSubSubSection:

    def __init__(self, title) -> None:
        self._title = title
        self._lines = []
        self._subsubsubsections = [] # non existent yet


class OrgModeSubSection:

    def __init__(self, title) -> None:
        self._title = title
        self._lines = []
        self._subsubsections = []


    def add_subsubsection(self, title):
        self._subsubsections.append(OrgModeSubSubSection(title=title))
        self._lines = []
        return self._subsubsections[-1]


class OrgModeWriter:

    def __init__(self) -> None:
        self._sections = []
        self._pre = [
            '#+TODO: TODO IN-PROGRESS CANCELED DONE',
            '#+OPTIONS: author:nil'
        ]

    def sourcify(self, src: str) -> list:
        res = []
        res.append("#+begin_src")
        for line in src.split("\n"):
            res.append(line)
        res.append("#+end_src")
        return list(res)


    def add_section(self, title):
        self._sections.append(OrgModeSection(title=title))
        return self._sections[-1]


    def write_file(self, filename):
        with open(filename, 'w') as f:
            for pre_line in self._pre:
                f.write("%s\n\n" % pre_line)
            for s in self._sections:
                f.write("\n* %s\n\n" % s._title)
                for section_line in s._lines:
                    f.write("%s\n" % section_line)
                for ss in s._subsections:
                    f.write("\n** %s\n\n" % ss._title)
                    for subsection_line in ss._lines:
                        f.write("%s\n" % subsection_line)
                    for sss in ss._subsubsections:
                        f.write("\n*** %s\n\n" % sss._title)
                        for subsubsection_line in sss._lines:
                            f.write("%s\n" % subsubsection_line)

        return self


org = OrgModeWriter()

# with contextlib.suppress(FileNotFoundError): os.unlink("test.sql")

# def prerunsql(x):
#     e = sqlalchemy.create_engine("sqlite:///test.sql")
#     with e.connect() as c:
#         c.exec_driver_sql(x)
#         c.commit()
#         c.close()

# prerunsql("CREATE TABLE test(id integer primary key, name text);")


#src_engine = sqlalchemy.create_engine("sqlite:///test.sql")


def sloppy_env_loader(filename=".env"):
    import os
    if os.path.isfile(filename):
        env_lines = [x for x in open(filename, "r").read().strip().split("\n") if x.find("=") > -1]
        for env_line in env_lines:
            idx = env_line.find("=")
            k = env_line[0:idx]
            if k.startswith("export "):
                k = k.split(" ")[1]
            v = env_line[idx+1:]
            os.environ[k] = v


sloppy_env_loader()

mysql_user = os.getenv("DBUSER")
mysql_pass = os.getenv("DBPASS")
mysql_host = os.getenv("DBHOST")
mysql_port = os.getenv("DBPORT")
mysql_name = os.getenv("DBNAME")
mysql_cafilename = os.getenv("DBCAFILENAME")

mysqlconstr = "mysql+pymysql://%s:%s@%s:%s/%s" % (mysql_user, mysql_pass, mysql_host, mysql_port, mysql_name)

src_engine = None

# https://stackoverflow.com/questions/48742736/using-ssl-with-sqlalchemy
if mysql_cafilename == None:
    src_engine = sqlalchemy.create_engine(mysqlconstr)
else:
    src_engine = sqlalchemy.create_engine(mysqlconstr, connect_args={"ssl": {"ssl_ca":mysql_cafilename}})


Src_Base = sqlalchemy.ext.automap.automap_base()
src_session = sqlalchemy.orm.Session(src_engine)

Src_Base.prepare(autoload_with=src_engine)




src_metadata = sqlalchemy.MetaData()
src_metadata.reflect(bind=src_engine)

section_tables = org.add_section("Tables")

#subsection_spec = section_tables.add_subsection(title="spec")
#subsection_spec._lines += org.sourcify("""a new way
#to do it""")

for database_table in src_metadata.sorted_tables:
    subsection_table = section_tables.add_subsection(title="Table =" + database_table.fullname + "=")
    subsubsection_columns = subsection_table.add_subsubsection(title="Columns - %d" % len(database_table.columns))
    #subsubsection_columns._lines.append("Column definitions.")
    for col in database_table.columns:
        subsubsection_columns._lines.append("  - =" + col.name + "= of type =" + str(col.type) + "=")
    
    subsubsection_fks = subsection_table.add_subsubsection(title="Foreign Keys - %d" % len(database_table.foreign_keys))
    for fk in database_table.foreign_keys:
        subsubsection_fks._lines.append("  - =" + fk.name + "= pointing to =" + fk.target_fullname + "=")


# t_test = Src_Base.classes.table1

# x = t_test(name="oink")
# src_session.add(x)
# src_session.commit()

org.write_file("database.org")

outzip_actual = zipfile.ZipFile(OUTZIP, 'w')

with io.StringIO() as f:
    f.write("from typing import overload\n\n")
    for database_table in src_metadata.sorted_tables:
        if database_table.name.find("-") > -1:
            continue
        tablevars = []
        f.write("class TABLE_%s:\n" % (database_table.name))
        f.write("\n")
        for fk in database_table.foreign_keys:
            f.write("    %s = None\n" % (fk.name))
            tablevars.append(fk.name + ": " + fk.get_referent().type.python_type.__name__)
        for col in database_table.columns:
            f.write("    %s = None\n" % (col.name))
            tablevars.append(col.name + ": " + col.type.python_type.__name__)
        f.write("\n")
        init_signature = ", ".join(tablevars)
        f.write("    @overload\n")
        f.write("    def __init__ (self, %s) -> None:\n" % init_signature)
        f.write("        print('NOOOOOOOOOOO')\n")
        f.write("\n")
        f.write("\n")
    outzip_actual.writestr("tables/__init__.py", f.getvalue())

with io.StringIO() as f:
    f.write("""#from tables import *

import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.automap
import os

def sloppy_env_loader(filename=".env"):
    import os
    if os.path.isfile(filename):
        env_lines = [x for x in open(filename, "r").read().strip().split("\\n") if x.find("=") > -1]
        for env_line in env_lines:
            idx = env_line.find("=")
            k = env_line[0:idx]
            if k.startswith("export "):
                k = k.split(" ")[1]
            v = env_line[idx+1:]
            os.environ[k] = v


sloppy_env_loader()


mysql_user = os.getenv("DBUSER")
mysql_pass = os.getenv("DBPASS")
mysql_host = os.getenv("DBHOST")
mysql_port = os.getenv("DBPORT")
mysql_name = os.getenv("DBNAME")
mysql_cafilename = os.getenv("DBCAFILENAME")

mysqlconstr = "mysql+pymysql://%s:%s@%s:%s/%s" % (mysql_user, mysql_pass, mysql_host, mysql_port, mysql_name)

src_engine = None

# https://stackoverflow.com/questions/48742736/using-ssl-with-sqlalchemy
if mysql_cafilename == None:
    src_engine = sqlalchemy.create_engine(mysqlconstr)
else:
    src_engine = sqlalchemy.create_engine(mysqlconstr, connect_args={"ssl": {"ssl_ca":mysql_cafilename}})


Src_Base = sqlalchemy.ext.automap.automap_base()
src_session = sqlalchemy.orm.Session(src_engine)

Src_Base.prepare(autoload_with=src_engine)




src_metadata = sqlalchemy.MetaData()
src_metadata.reflect(bind=src_engine)

#from tables import *
""")
    f.write("\n")
    for database_table in src_metadata.sorted_tables:
        if database_table.name.find("-") > -1:
            continue
        f.write("TABLE_%s = %s.classes.%s\n" % (database_table.name,'Src_Base',database_table.name))
    outzip_actual.writestr("mainstub.py", f.getvalue())
