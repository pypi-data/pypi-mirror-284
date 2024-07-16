import os
import datetime
from pathlib import Path
from icplot.gantt import GanttChart
from icplot.project_elements import Milestone


def test_gantt_chart():

    milestone0 = Milestone()
    milestone0.title = "My Milestone 0"
    milestone0.description = "Description of Milestone 0."
    milestone0.start_date = datetime.date(2024, 6, 30)
    milestone0.due_date = datetime.date(2024, 7, 12)

    milestone1 = Milestone()
    milestone1.title = "My Milestone 1"
    milestone1.description = "Description of Milestone 1."
    milestone1.start_date = datetime.date(2024, 7, 1)
    milestone1.due_date = datetime.date(2024, 7, 15)
    
    gantt = GanttChart()
    gantt.milestones = [milestone0,
                        milestone1]

    output_path = Path(os.getcwd()) / "gantt.svg"

    gantt.plot(output_path)
