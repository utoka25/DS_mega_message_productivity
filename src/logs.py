import pandas as pd
    

def set_log(connection, project, task, date_start, date_end, status, log):
    # Запись логов в БД
    log = pd.DataFrame(data=[[project, task, date_start, date_end, status, log]], 
                        columns=['project', 'task', 'date_start', 'date_end', 'status', 'log'])
    log.to_sql('project_logs', connection, if_exists='append', index=False)