import time
import os
import os.path
import json 
import shutil
import math
import numpy as np
import matplotlib.pyplot as plt
import subprocess


current_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
filename = "rimea_06_corner.scenario"
new_filename = "rimea_06_corner_task3.scenario"
base_dir = current_path + "/scenarios/"

#scenario scenario file
in_file = open(base_dir + filename, "r")
data = json.load(in_file)
in_file.close()

#rename
tmp = data["name"]
data["name"] = "rimea_06_corner_task3.scenario"

#add pedestrian
tmp = data["scenario"]["topography"]["dynamicElements"]
ped ={
        "source" : None,
        "targetIds" : [ 2 ],
        "position" : {
          "x" : 11.6,
          "y" : 1.5
        },
        "velocity" : {
          "x" : 0.0,
          "y" : 0.0
        },
        "nextTargetListIndex" : 0,
        "freeFlowSpeed" : 1.752612703047805,
        "attributes" : {
          "id" : -1,
          "radius" : 0.2,
          "densityDependentSpeed" : False,
          "speedDistributionMean" : 1.34,
          "speedDistributionStandardDeviation" : 0.26,
          "minimumSpeed" : 0.5,
          "maximumSpeed" : 2.2,
          "acceleration" : 2.0,
          "footStepsToStore" : 4,
          "searchRadius" : 1.0,
          "angleCalculationType" : "USE_CENTER",
          "targetOrientationAngleThreshold" : 45.0
        },
        "idAsTarget" : -1,
        "isChild" : False,
        "isLikelyInjured" : False,
        "mostImportantEvent" : None,
        "salientBehavior" : "TARGET_ORIENTED",
        "groupIds" : [ ],
        "trajectory" : {
          "footSteps" : [ ]
        },
        "groupSizes" : [ ],
        "modelPedestrianMap" : None,
        "type" : "PEDESTRIAN"
      }
tmp.append(ped)

data["scenario"]["topography"]["dynamicElements"] = tmp

#save the file with new name
out_file = open(base_dir + new_filename, "w+")
out_file.write(json.dumps(data))
out_file.close()

#Call vadere-console.jar
#os.system('cmd /c "java -jar vadere-console.jar scenario-run --scenario-file "/senarios/rimea_06_corner_task3.scenario" --output-dir output')

subprocess.run("echo 'join the dark side'", shell=True, stderr=subprocess.PIPE)
