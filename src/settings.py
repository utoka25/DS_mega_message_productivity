#--------------Идентификатор проекта------------------
PROJECT = 'megazip'
TASK = 'message_productivity'

#----------Параметры подключения к MySQL--------------
MYSQL_HOST_NAME = 'staging-db-megazip.s25.dev'
MYSQL_USER      = 'megazip'
MYSQL_PASS      = 'megazip'
MYSQL_DB_NAME   = 'megazip'

#----------Параметры подключения к CH--------------
CH_HOST_NAME  = '5.188.142.30'
CH_CLIENT_PORT = 9000
CH_HTTP_PORT  = 8123
CH_USER       = 'reports'
CH_DB_NAME    = 'reports'

#-------------------------------------------
CH_PASS      = '6sWm2Z3T94u.E96F'
# CH_URL        = 'clickhouse://' + CH_USER + ':' + CH_PASS + '@' + CH_HOST_NAME + ':' + str(CH_HTTP_PORT) + '/' + CH_DB_NAME

CH_URL        = f'clickhouse://{CH_USER}:{CH_PASS}@{CH_HOST_NAME}:{str(CH_HTTP_PORT)}/{CH_DB_NAME}'