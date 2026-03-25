#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")


name = "G8X.2026.T04.GE2.SUBMISSION"
default_task = "publish"

@init
def set_properties(project):
    project.set_property("coverage_include_patterns", ["uc3m_consulting.enterprise_manager"])

    project.set_property("coverage_break_build", True)
    project.set_property("coverage_threshold_warn", 0)
    project.set_property("coverage_threshold_fail", 70)
