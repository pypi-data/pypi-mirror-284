"""
******************************************************************************

    Echoes Data Browser (Ebrow) is a data navigation and report generation
    tool for Echoes.
    Echoes is a RF spectrograph for SDR devices designed for meteor scatter
    Both copyright (C) 2018-2023
    Giuseppe Massimo Bertani gm_bertani(a)yahoo.it

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, http://www.gnu.org/copyleft/gpl.html

*******************************************************************************

"""
import io
import os
import sys
import traceback
import ctypes
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMessageBox
from pathlib import Path

from .mainwindow import MainWindow

app = None
mainWin = None


def excepthook(excType, excValue, tracebackobj):
    global mainWin

    """
    Global function to catch unhandled exceptions
    @param excType exception type
    @param excValue exception value
    @param tracebackobj traceback object
    """

    mainWin.busy(False, force=True)
    separator = '-' * 80
    logFile = "ebrow.log"
    notice = \
        """An unhandled exception occurred. Please report the problem\n""" \
        """using the error reporting dialog or via email to <%s>.\n""" \
        """A log has been written to "%s".\n\nError information:\n""" % \
        ("gm_bertani@yahoo.it", logFile)
    versionInfo = "GUI version: " + mainWin.version
    timeString = str(datetime.today())

    tbinfofile = io.StringIO()
    traceback.print_tb(tracebackobj, None, tbinfofile)
    tbinfofile.seek(0)
    tbinfo = tbinfofile.read()
    errmsg = 'Exception %s: \n%s' % (str(excType), str(excValue))
    sections = [separator, timeString, separator, errmsg, separator, tbinfo, separator, versionInfo]
    msg = '\n'.join(sections)
    print(msg)
    try:
        f = open(logFile, "w")
        f.write(msg)
        f.write(versionInfo)
        f.close()
    except IOError:
        pass
    errorbox = QMessageBox()
    errorbox.setWindowTitle("Echoes Data Browser")
    errorbox.setText(str(notice) + str(msg))
    errorbox.setIcon(QMessageBox.Critical)
    errorbox.exec_()
    os.abort()


def main():
    global mainWin

    # sys.stdout = None  # suppress console output
    sys.excepthook = excepthook
    app = QApplication(sys.argv)

    isBatchRMOB = False
    isBatchReport = False
    verboseLog = False
    multipleInstances = False
    argc = len(sys.argv)
    while argc > 1:
        argc -= 1
        if '--rmob' in sys.argv[argc]:
            isBatchRMOB = True
        if '--report' in sys.argv[argc]:
            isBatchReport = True
        if '--verbose' in sys.argv[argc]:
            verboseLog = True
        if '--multiple' in sys.argv[argc]:
            multipleInstances = True
        if '--help' in sys.argv[argc]:
            print("Usage: ebrow [--verbose] [--report] [--rmob] [--multiple]")
            sys.exit(0)

    workingDir = Path(Path.home(), Path("ebrow"))
    lockFilePath = workingDir / Path("ebrow.lock")
    if lockFilePath.exists():
        if not multipleInstances:
            print(
                "ERROR - Cannot run. Stale lock file ebrow.lock: another Ebrow instance is already running or has just crashed.")
            print("        Use ebrow --multiple to allow multiple instances or delete the lock file manually.")
            sys.exit(-1)
    else:
        workingDir.mkdir(parents=True, exist_ok=True)
        with open(lockFilePath, 'w') as f:
            f.write("{}".format(os.getpid()))

    mainWin = MainWindow(app, isBatchRMOB, isBatchReport, verboseLog)
    if os.name == 'nt':
        myappid = 'GABB.Echoes.DataBrowser'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app.installEventFilter(mainWin)
    mainWin.show()

    if isBatchRMOB or isBatchReport:
        mainWin.postInit()
        try:
            os.unlink(lockFilePath)
        except FileNotFoundError:
            pass
    else:
        ret = app.exec_()
        try:
            os.unlink(lockFilePath)
        except FileNotFoundError:
            pass
        sys.exit(ret)


if __name__ == '__main__':
    main()
