def set_workdir(file):
   work_dir_tulip = os.path.split(os.path.dirname(os.path.abspath(file)))
   work_dir = work_dir_tulip[1]
   if work_dir == 'src':
      app_dir = os.path.abspath(os.path.join(os.path.dirname(file), '..'))
   else:
      app_dir = os.path.abspath(os.path.dirname(file))
   os.chdir(app_dir)
   print(app_dir)