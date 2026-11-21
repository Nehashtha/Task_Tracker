import pytest
from main import Task, Taskmanager

"""
manager	Creates an empty temporary database
task_manager	Adds sample tasks to the database
db_connection	Opens a connection and cursor, then closes the connection after the test
"""
@pytest.fixture

def manager(tmp_path):

    """
    tmp_path creates a temporary directory
    we are creating separate database to test without impacting existing database

    :param tmp_path:
    :return:
    """
    db_path=tmp_path/ "test_database.db"


    print("Temporary directory:", tmp_path)
    print("Database path:", db_path)
    print("Directory exists:", tmp_path.exists())
    taskmanager = Taskmanager(str(db_path))
    taskmanager.create_Database()
    return taskmanager

@pytest.fixture
def task_manager(manager):

    task1 = Task(1, "Learn Python", "High", "Learning",
                "Practice pytest", "2026-12-01")
    task2 = Task(2, 'food', 'low', 'grocery',
                 'buy vegetables', '2026-08-30')
    task3 = Task(3, 'bills', 'low', 'house',
                 'hydro bills', '2026-08-30')
    task4 = Task(4, 'fruits', 'medium', 'grocery',
                 'buy fruits', '2026-08-03')

    manager.add_task(task1)
    manager.add_task(task2)
    manager.add_task(task3)
    manager.add_task(task4)

    return manager

@pytest.fixture
def db_connection(manager):
    db,cur= manager.database()
    yield db,cur
    db.close()

def test_add_task(manager,db_connection):
    task1=Task (1, 'food', 'high', 'grocery', 'buy vegetables', '2026-08-30')
    task3=Task(3, 'bills', 'low', 'house', 'hydro bills', '2026-08-30' )

    result1=manager.add_task(task1)
    result2=manager.add_task(task3)
    assert result1 is True
    assert result2 is True
    db,cur=db_connection
    sql= """SELECT category FROM task_tracker ORDER BY taskid"""
    cur.execute(sql)
    data=cur.fetchall()
    assert len(data)==2
    assert data[0][0]=='grocery'
    assert data[1][0]=='house'


def test_remove_task(task_manager, db_connection):


    result= task_manager.remove_task(1)
    assert result is True
    db,cur=db_connection
    sql="""SELECT * FROM task_tracker"""
    cur.execute(sql)
    data=cur.fetchall()
    assert len(data)==3



def test_update_task(task_manager,db_connection):

    newtask=Task(3, 'renovate', 'medium', 'house', 'renovate roof', '2026-08-30' )
    result=task_manager.update_task(newtask)
    # assert manager.tasks[0].category=='house'
    assert result is True
    db,cur= db_connection

    sql="""SELECT category, task FROM task_tracker WHERE taskid=?"""
    cur.execute(sql,(3,))
    data= cur.fetchone()
    assert data is not None
    assert data[0]=='house'
    assert data[1]=='renovate'


def test_search_by_word(task_manager,db_connection):
    result= task_manager.search_by_word('buy')
    assert len(result) == 2
    db,cur= db_connection

    sql="""SELECT category FROM task_tracker WHERE description  LIKE ? """
    cur.execute(sql,('%buy%',))
    data=cur.fetchall()
    assert len(data)==2

def test_filter_by_id(task_manager, db_connection):
    """
    sql oarameter should always be givesn as tuple
    fetchone() returns one database row as a tuple.

    fetchone() returns one row; fetchall() returns a list of rows.
    python counts the number of columns in that tuple. Your table has 6 columns, so len(result) returns 6.
    :param task_manager:
    :return:
    """
    result=task_manager.filter_by_id(2)
    # assert len(result) == 1
    assert result is not None
    assert result[0] == 2
    assert result[3] == 'grocery'
    db, cur = db_connection

    sql=("""SELECT category FROM task_tracker WHERE taskid=?""")
    cur.execute(sql,(2,))
    data = cur.fetchone()
    assert data is not None
    assert data[0] == 'grocery'



def test_filter_by_category(task_manager,db_connection):

    result= task_manager.filter_by_category('grocery')
    assert len(result) == 2
    db, cur = db_connection
    sql="""SELECT category FROM task_tracker WHERE category=? """
    cur.execute(sql,('grocery',))
    data = cur.fetchall()
    assert len(data) == 2
    for row in data:
        assert row[0] == 'grocery'

@pytest.mark.parametrize('category,expected',[
    ('Learning',1),
    ('grocery',2),
    ('house',1)])

def test_filter_by_category_param(task_manager,db_connection,category, expected):
    result=task_manager.filter_by_category(category)
    assert len(result)==expected


