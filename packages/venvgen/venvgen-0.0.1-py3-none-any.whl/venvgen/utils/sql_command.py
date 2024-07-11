create_venv_info_sql = '''
CREATE TABLE IF NOT EXISTS venv_info(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    project_path VARCHAR(300) NOT NULL,
    venv_name VARCHAR(200) UNIQUE,
    created_date DATE NOT NULL,
    requirement_file VARCHAR(300),
    connect_status VARCHAR(20) NOT NULL
);
'''

insert_into_venv_info_sql = '''
INSERT INTO venv_info(project_path, venv_name, created_date, requirement_file, connect_status) 
VALUES (?, ?, ?, ?, ?);
'''

update_connect_status_venv_info_sql = '''
UPDATE venv_info
SET connect_status = ?
WHERE venv_name = ?;
'''
