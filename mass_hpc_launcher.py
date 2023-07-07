import os

template_file = 'hpc_launcher.template'
#template_file = 'hpc_launcher.psb2.template'

run_nums = "0-99"
#run_nums = "8,11,46,57,91"

name = "Plexicase"
basedir = "/usr/local/research/compsci/helmuth/ktran/plexicase/option1/"

cmd_line_params = """"""
#cmd_line_params = """--ast-strategy :newest-out"""
#cmd_line_params = """--ast-strategy :biggest-out """

problems = [

            ### Composite
   "area-of-rectangle",
   "centimeters-to-meters",
   "count-true",
   "filter-bounds",
   "first-index-of-true",
   "get-vals-of-key",
   "min-key",
   "max-applied-fn",
   "set-cartesian-product",
   "set-symmetric-difference",
   "sets-with-element",
   "simple-encryption",
   "sum-2-vals",
   "sum-2-vals-polymorphic",
   "sum-2D",
   "sum-vector-vals",
   "time-sheet"

]

with open(template_file, 'r') as hpc_template:
    hpc_launcher_template = hpc_template.read()


for problem in problems:

    hpc_launcher = hpc_launcher_template.replace("#qsub-name#", problem + name)
    hpc_launcher = hpc_launcher.replace("#namespace#", problem)
    hpc_launcher = hpc_launcher.replace("#dir#", basedir)
    hpc_launcher = hpc_launcher.replace("#run-nums#", run_nums)
    hpc_launcher = hpc_launcher.replace("#cmd-line-params#", cmd_line_params)


    temp_filename = "temp_launcher.run"
    with open(temp_filename, 'w') as temp_launcher:
        temp_launcher.write(hpc_launcher)

    os.system("qsub " + temp_filename)
    os.remove(temp_filename)



